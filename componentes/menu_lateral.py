import flet as ft
import modulos.cruds_all as ca
from utils.navegacion import pasar


def crear_menu_lateral(page):
    user = page.data.get("user")
    menu_expandido = False

    contenido = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True
    )

    menu = ft.Container(
        width=60,
        bgcolor=ft.Colors.TRANSPARENT,
        animate=ft.Animation(250, ft.AnimationCurve.EASE_IN_OUT),
        border_radius=10,
        padding=10,
    )
    capa = ft.GestureDetector(
                        visible=False,
                        expand=True,                        
                    )
    def cierre(e=None):
        nonlocal menu_expandido

        menu_expandido = False
        menu.width = 60
        menu.bgcolor = ft.Colors.TRANSPARENT
        contenido.controls = []
        
        capa.visible = False  
        pasar("/home",page)      
        page.update()
    
    def cerrar_menu(e=None):
        nonlocal menu_expandido

        menu_expandido = False
        menu.width = 60
        menu.bgcolor = ft.Colors.TRANSPARENT
        contenido.controls = []        
        capa.visible = False        
        page.update()
        
    capa.on_tap = cerrar_menu      
    def cerrar_sesion(page):
        # limpiar variables de sesión si tienes
        cerrar_menu()
        page.data.clear()
        # mandar al login
        pasar("/",page) 
    def ant_pass(link,page):
        cerrar_menu()
        pasar(link, page)
    def toggle(e):
        nonlocal menu_expandido

        menu_expandido = not menu_expandido
        
        modulos=[]
        modulos=ca.rol_modulos_crud.getmodulo_by_roles(user["Roll_id"])
        ids_modulos = [item["modulo_id"] for item in modulos]
        tmodulos=ca.modulos_crud.get_all()
        if menu_expandido:
            menu.width = 220
            menu.bgcolor = ft.Colors.with_opacity(0.5, ft.Colors.BLUE)
            capa.visible = True

            controles = []

            controles.append(
                ft.ElevatedButton(
                    "🏠 Inicio",
                    on_click=lambda e: cierre()
                )
            )

            for item in tmodulos:
                    if item["idmodulo"] in ids_modulos:
                        controles.append(
                            ft.ElevatedButton(
                                item["nombre"].upper(),
                                icon=getattr(ft.Icons, item["icono"].upper()),
                                on_click=lambda e, link=item["ruta"]: ant_pass(link, page),
                            )
                        )

            controles.append(
                            ft.ElevatedButton(
                                "🚪 Cerrar sesión",
                                on_click=lambda e: cerrar_sesion(page),
                            )
                        )

            contenido.controls = controles
        else:
            cerrar_menu()

        page.update()

    menu.content = contenido

    
    return ft.Stack(
        [
            capa,
            menu
        ]
    ), toggle