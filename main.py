import flet as ft
import router


async def main(page: ft.Page):
    print("FLET CONECTADO")
    page.title = "LIFE ALDEA 8"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    router.configurar_router(page)

print("ANTES DE INICIAR FLET")

ft.run(
    main,
    port=8550
)