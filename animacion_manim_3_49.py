from manim import *

class MuroPresionAnimacion(ThreeDScene):
    def construct(self):
        # Fondo oscuro elegante
        self.camera.background_color = "#0b0f19"

        # Único texto permitido: número del ejercicio
        ejercicio_tag = Text("3.49", font_size=36, color=WHITE, weight=BOLD)
        ejercicio_tag.to_corner(UL, buff=0.6)
        punto_azul = Dot(color="#38bdf8", radius=0.07).next_to(ejercicio_tag, RIGHT, buff=0.15)
        tag_group = VGroup(ejercicio_tag, punto_azul)
        self.add_fixed_in_frame_mobjects(tag_group)
        self.play(FadeIn(tag_group, shift=DOWN*0.2), run_time=0.8)

        # Dimensiones escaladas para pantalla
        # H = 6 m -> 4.5 unidades de Manim
        # h = 5 m -> 3.75 unidades
        # b = 3.09 m -> 2.32 unidades
        scale = 0.75
        H = 6.0 * scale
        h = 5.0 * scale
        b = 3.09 * scale

        # Posicionamiento base
        y_base = -2.2
        x_wall_left = -0.5
        x_wall_right = x_wall_left + b

        # Terreno
        terreno_linea = Line(LEFT * 6 + UP * y_base, RIGHT * 6 + UP * y_base, color="#334155", stroke_width=4)
        hachurado = VGroup(*[
            Line(LEFT * 5.5 + RIGHT * i * 0.4 + UP * y_base,
                 LEFT * 5.2 + RIGHT * i * 0.4 + UP * (y_base - 0.3),
                 color="#1e293b", stroke_width=2)
            for i in range(28)
        ])
        self.play(Create(terreno_linea), Create(hachurado), run_time=1.0)

        # Muro de hormigón 2D
        muro_rect = Rectangle(
            width=b,
            height=H,
            fill_color="#64748b",
            fill_opacity=0.85,
            stroke_color="#94a3b8",
            stroke_width=2
        )
        muro_rect.move_to([x_wall_left + b / 2, y_base + H / 2, 0])

        # Masa de agua 2D
        agua_rect = Rectangle(
            width=4.0,
            height=h,
            fill_color="#0284c7",
            fill_opacity=0.6,
            stroke_color="#38bdf8",
            stroke_width=1.5
        )
        agua_rect.move_to([x_wall_left - 2.0, y_base + h / 2, 0])

        # Marcador de nivel de agua
        tri_nivel = Triangle(color="#38bdf8", fill_color="#38bdf8", fill_opacity=1).scale(0.12).rotate(PI)
        tri_nivel.move_to([x_wall_left - 1.2, y_base + h + 0.15, 0])

        self.play(FadeIn(agua_rect), FadeIn(muro_rect), FadeIn(tri_nivel), run_time=1.2)
        self.wait(0.8)

        # 1. Distribución de presión hidrostática (triángulo de flechas)
        flechas_p = VGroup()
        num_flechas = 8
        for i in range(num_flechas):
            y_i = y_base + h * (1.0 - i / (num_flechas - 1))
            ratio = i / (num_flechas - 1)
            longitud = max(0.2, ratio * 1.8)
            flecha = Arrow(
                start=[x_wall_left - longitud, y_i, 0],
                end=[x_wall_left, y_i, 0],
                buff=0,
                color="#00f0ff",
                stroke_width=3,
                max_tip_length_to_length_ratio=0.3
            )
            flechas_p.add(flecha)

        hipotenusa = Line(
            [x_wall_left, y_base + h, 0],
            [x_wall_left - 1.8, y_base, 0],
            color="#00f0ff",
            stroke_width=2
        )

        self.play(Create(hipotenusa), Create(flechas_p), run_time=1.5)
        self.wait(1.0)

        # 2. Transición de cámara a perspectiva 3D
        self.move_camera(phi=65 * DEGREES, theta=-55 * DEGREES, zoom=0.9, run_time=2.0)
        self.wait(0.8)

        # 3. Fuerza Resultante FH en el centro de presiones (h/3)
        y_cp = y_base + h / 3.0
        flecha_FH = Arrow3D(
            start=[x_wall_left - 2.4, y_cp, 0],
            end=[x_wall_left, y_cp, 0],
            color="#06b6d4"
        )
        dot_cp = Dot3D(point=[x_wall_left, y_cp, 0], color="#22d3ee", radius=0.1)

        self.play(FadeOut(flechas_p), FadeOut(hipotenusa), run_time=0.8)
        self.play(Create(flecha_FH), FadeIn(dot_cp), run_time=1.2)
        self.wait(0.8)

        # 4. Peso Propio del Muro (W) y Normal (N)
        centroide_x = x_wall_left + b / 2
        centroide_y = y_base + H / 2
        dot_cg = Dot3D(point=[centroide_x, centroide_y, 0], color="#fbbf24", radius=0.1)

        flecha_W = Arrow3D(
            start=[centroide_x, centroide_y, 0],
            end=[centroide_x, centroide_y - 2.2, 0],
            color="#f59e0b"
        )
        flecha_N = Arrow3D(
            start=[centroide_x, y_base - 0.8, 0],
            end=[centroide_x, y_base, 0],
            color="#10b981"
        )

        self.play(FadeIn(dot_cg), Create(flecha_W), Create(flecha_N), run_time=1.2)
        self.wait(0.8)

        # 5. Fuerza de Rozamiento FR en la base (hacia la izquierda)
        flecha_FR = Arrow3D(
            start=[x_wall_left + b * 0.7, y_base, 0],
            end=[x_wall_left + b * 0.7 - 1.8, y_base, 0],
            color="#f97316"
        )
        self.play(Create(flecha_FR), run_time=1.0)
        self.wait(0.8)

        # 6. Pivote de Vuelco O (esquina inferior derecha) y Arcos de Momento
        pivote_O = Dot3D(point=[x_wall_right, y_base, 0], color="#f43f5e", radius=0.13)
        self.play(FadeIn(pivote_O), run_time=0.6)

        # Retorno suave a vista frontal con todas las fuerzas
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.0, run_time=2.0)
        self.wait(2.0)
