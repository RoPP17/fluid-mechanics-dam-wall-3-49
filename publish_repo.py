import subprocess
import urllib.request
import json
import os

# 1. Obtener token del Git Credential Manager
p = subprocess.Popen([r'C:\Program Files\Git\mingw64\bin\git-credential-manager.exe', 'get'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate('protocol=https\nhost=github.com\n\n')
token = ''
for line in out.splitlines():
    if line.startswith('password='):
        token = line.split('=', 1)[1].strip()

repo_name = 'fluid-mechanics-dam-wall-3-49'
headers = {
    'Authorization': f'token {token}',
    'User-Agent': 'Python/3.12',
    'Accept': 'application/vnd.github.v3+json'
}

# 2. Crear repositorio en GitHub si no existe
check_req = urllib.request.Request(f'https://api.github.com/repos/RoPP17/{repo_name}', headers=headers)
repo_exists = False
try:
    with urllib.request.urlopen(check_req) as resp:
        print('Repository already exists on GitHub.')
        repo_exists = True
except urllib.error.HTTPError as e:
    if e.code == 404:
        print('Creating repository on GitHub...')
    else:
        print('Check status:', e.code)

if not repo_exists:
    payload = json.dumps({
        'name': repo_name,
        'description': 'Simulación interactiva 2D/3D de distribución de presiones hidrostáticas, estabilidad y falla estructural - Ejercicio 3.49',
        'private': False,
        'has_issues': True,
        'has_projects': True,
        'has_wiki': False
    }).encode('utf-8')
    create_req = urllib.request.Request('https://api.github.com/user/repos', data=payload, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(create_req) as resp:
            data = json.loads(resp.read().decode())
            print('Successfully created repository:', data.get('html_url'))
    except Exception as e:
        print('Error creating repo:', e)

# 3. Inicializar y commitear localmente
cwd = r'C:\Users\andre\OneDrive\Desktop\1.Universidad\4. Cuarto Semestre\Mecánica de Fluidos II\Simulacion_3.49_Muro_Presion_3D'

subprocess.run(['git', 'init'], cwd=cwd)
subprocess.run(['git', 'branch', '-M', 'main'], cwd=cwd)
subprocess.run(['git', 'add', '.'], cwd=cwd)
subprocess.run(['git', 'commit', '-m', 'feat: simulacion interactiva 2D/3D ejercicio 3.49 Mecanica de Fluidos'], cwd=cwd)

# 4. Configurar remote y push
subprocess.run(['git', 'remote', 'remove', 'origin'], cwd=cwd)
subprocess.run(['git', 'remote', 'add', 'origin', f'https://github.com/RoPP17/{repo_name}.git'], cwd=cwd)

print('Pushing to GitHub...')
push_res = subprocess.run(['git', 'push', '-u', f'https://RoPP17:{token}@github.com/RoPP17/{repo_name}.git', 'main', '--force'], cwd=cwd, capture_output=True, text=True)
print('Push stdout:', push_res.stdout)
print('Push stderr:', push_res.stderr)

# 5. Habilitar GitHub Pages
pages_payload = json.dumps({
    'source': {
        'branch': 'main',
        'path': '/'
    }
}).encode('utf-8')
pages_req = urllib.request.Request(f'https://api.github.com/repos/RoPP17/{repo_name}/pages', data=pages_payload, headers=headers, method='POST')
try:
    with urllib.request.urlopen(pages_req) as resp:
        pdata = json.loads(resp.read().decode())
        print('GitHub Pages enabled:', pdata.get('html_url'))
except Exception as e:
    print('Pages configuration note:', e)
