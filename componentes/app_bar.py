import flet as ft
import modulos.cruds_all as ca

def crear_app_bar(page, usuario, abrir_menu):
    roles=ca.roles_crud.get_by_id(usuario['Roll_id'])
    return ft.AppBar(
        leading=ft.IconButton(
            icon=ft.Icons.MENU,
            tooltip="Menú",
            on_click=abrir_menu,
        ),

        title=ft.Row(
            controls=[
                ft.Container(expand=True),

                ft.Text(
                    f"👤 {roles['nombre']+" "+usuario['Nombres']}",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Container(expand=True),

                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.WAREHOUSE),
                        ft.Text(
                            "LIFE ALDEA 8",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),
                    
                    ],
                    #on_click=lambda e: pasar("/home",page) ,                    
                    spacing=5,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),

        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        center_title=False,
    )