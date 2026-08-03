import flet as ft
import modulos.cruds_all as ca
from utils.navegacion import cerrar_aplicacion


def crear_login(page):

    ndocumento = ft.TextField(
        label="N° de Documento",
        width=300,
        autofocus=True,
    )

    def loginn(e):
        user = ca.users_crud.get_by_multi( ndocumento.value,"DNI")

        if user:
           page.data = {"user": user}

           page.route = "/home"
           page.on_route_change(None)

        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario no encontrado"))
            page.snack_bar.open = True
            page.update()

    login_card = ft.Card(
        content=ft.Container(
            width=400,
            padding=30,
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.WAREHOUSE, size=60),
                    ft.Text("LIFE ALDEA 8", size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("Sistema de Gestión de Almacén"),
                    ft.Divider(),
                    ndocumento,
                    ft.ElevatedButton(
                        "INGRESAR",
                        width=300,
                        on_click=loginn,
                    ),
                    ft.ElevatedButton(
                        "SALIR",
                        width=300,
                        icon=ft.Icons.EXIT_TO_APP,                        
                        on_click=lambda e: cerrar_aplicacion(page),
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
        )
    )

    return login_card