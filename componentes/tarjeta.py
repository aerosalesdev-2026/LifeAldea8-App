import flet as ft


def tarjeta(
    titulo: str,
    icono,
    color,
    on_click=None,
):

    return ft.Container(
        height=180,
        border_radius=15,
        bgcolor=color,
        ink=True,
        padding=15,
        animate=ft.Animation(
            200,
            ft.AnimationCurve.EASE_IN_CIRC,
        ),
        on_click=on_click,

        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Icon(
                    icon=icono,
                    size=55,
                    color=ft.Colors.WHITE,
                ),

                ft.Text(
                    value=titulo,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
    )