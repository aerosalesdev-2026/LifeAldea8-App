import flet as ft
from flet_camera import Camera


def take_foto(page: ft.Page):

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


