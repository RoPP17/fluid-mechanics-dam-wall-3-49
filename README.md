# Simulación Interactiva 2D/3D - Ejercicio 3.49 (Mecánica de Fluidos)

Aplicación web 3D interactiva y cinemática en tiempo real para la visualización y análisis pedagógico de empujes hidrostáticos, distribución de presiones, estabilidad al deslizamiento y vuelco, y mecanismos de falla estructural en muros de retención / presas de gravedad de hormigón.

---

## 📌 Enunciado del Ejercicio 3.49

> Con referencia a la Figura 3.40, calcular la anchura del muro de hormigón necesaria para prevenir que el muro no sufra ningún deslizamiento. El peso específico del hormigón es de $23.6\text{ kN/m}^3$ y el coeficiente de rozamiento entre la base del muro y el terreno de cimentación es $0.42$. Utilícese $1.5$ como coeficiente de seguridad contra el deslizamiento. ¿Estará también asegurado contra el vuelco?
>
> **Solución teórica**: $b = 3.09\text{ m}$; Sí (asegurado contra vuelco, $FS_{vuelco} \approx 3.31$).

---

## 🚀 Características de la Simulación

### 1. Apartado de Estática y Equilibrio (Modo 3.49)
* **Visualización 2D / 3D**: Transición suave entre el corte ortogonal técnico y la perspectiva 3D isométrica orbitable en 360°.
* **Prisma de Presiones Volumétrico**: Muestra visualmente la integración de la cuña hidrostática sobre el ancho unitario de fondo ($L = 1\text{ m}$).
* **Fuerza Resultante de Empuje ($F_H$)**: Vector en magenta neón aplicado rigurosamente en el centro de presiones ($h/3 = 1.667\text{ m}$).
* **Separación Vectorial Clara**:
  * Vector peso propio ($W$) en ámbar/oro aplicado en el centroide geométrico del muro ($b/2, H/2$).
  * Vector normal del suelo ($N$) en verde esmeralda desplazado hacia la zona de compresión excéntrica de la base.
  * Vector de rozamiento estático ($F_R$) a ras de la interfaz suelo-hormigón.
* **Momentos Elevados sobre el Piso**:
  * Momento volcador horario ($M_{\text{volc}}$) en rojo sobre el cuadrante superior exterior del pie del muro ($O$).
  * Momento estabilizador antihorario ($M_{\text{est}}$) en verde en el cuadrante superior interior.
* **Tipografía Matemática**: Fracción vertical $\frac{h}{3}$ y subíndices de alta legibilidad con cero solapamientos.
* **Exploración Paramétrica**: Control deslizante en vivo para modificar el ancho $b$ ($1.0\text{ m} \le b \le 4.5\text{ m}$) observando la transición de inestabilidad/deslizamiento ($b < 2.06\text{ m}$) a equilibrio seguro ($b = 3.09\text{ m}$).

### 2. Apartado de Falla Estructural (Pared Delgada)
* Sección independiente con modelo de flexión en pared delgada ($b = 0.55\text{ m}$).
* Simulación física de concentración de tensiones de tracción en la cara húmeda inferior, iniciación y propagación de grieta diagonal, rotura en dos bloques, vuelco violento del fragmento superior y desborde dinámico de la masa de agua.
* Modo cámara lenta y restauración instantánea.

---

## ⌨️ Atajos de Teclado

| Tecla | Acción |
| :---: | :--- |
| **`Espacio`** | Play / Pausa en Modo Cinemático (o disparar rotura en Modo Falla) |
| **`T`** | Alternar entre Modo Estática 3.49 y Modo Falla por Pared Delgada |
| **`V`** | Alternar entre vista ortogonal 2D y perspectiva 3D orbitable |
| **`1` a `6`** | Salto directo a fases mecánicas (Geometría, Presión, Prisma 3D, $F_H$, Peso/Fricción, Momentos) |
| **`H`** | Ocultar / Mostrar todas las etiquetas y la interfaz HUD |
| **`R`** | Reiniciar simulación al estado de diseño inicial |

---

## 🛠️ Tecnologías

* **Three.js** (WebGL 3D acelerado por hardware)
* **OrbitControls**
* **HTML5 / CSS3** con Glassmorphism y tipografía matemática adaptativa
* **Manim Community Edition** (script complementario en Python)
