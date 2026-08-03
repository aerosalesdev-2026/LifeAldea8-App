import flet as ft

try:
    from flet_camera import Camera
except ImportError:
    Camera = None


def take_foto(page: ft.Page):
    if Camera is None:
        page.snack_bar = ft.SnackBar(
            ft.Text("Cámara no disponible en versión web")
        )
        page.snack_bar.open = True
        page.update()
        return None

    camara = Camera(
        width=400,
        height=500,
    )

    async def iniciar(e):
        await camara.initialize()

    async def tomar(e):
        foto = await camara.take_picture()
        print(foto)

    page.add(
        camara,
        ft.Row(
            [
                ft.ElevatedButton("Iniciar", on_click=iniciar),
                ft.ElevatedButton("Foto", on_click=tomar),
            ]
        )
    )