import flet as ft
import modulos.cruds_all as ca
from componentes.app_bar import crear_app_bar
from componentes.menu_lateral import crear_menu_lateral
from componentes.tarjeta import tarjeta
from utils.navegacion import lista_colores,pasar

import random

def home_view(page):

    #user = page.data["user"]
    user = page.data.get("user")
    modulos=[]
    #print(user)
    modulos=ca.rol_modulos_crud.getmodulo_by_roles(user['Roll_id'])
    ids_modulos = [item['modulo_id'] for item in modulos]

    tmodulos=ca.modulos_crud.get_all()
    menu, toggle_menu = crear_menu_lateral(page)
    # 🔥 IMPORTANTE: lo ponemos como overlay (flota encima)
    page.overlay.append(menu)
    page.appbar = crear_app_bar(page, user, toggle_menu)   
     #####
    home_cards = []
    for item in tmodulos:
        if item['idmodulo']in ids_modulos:
        
         home_cards.append(
            ft.Container(
                col={"sm": 12, "md": 6, "lg": 4, "xl": 3},
                content=tarjeta(
                    titulo=item['nombre'].upper(),
                    icono=getattr(ft.Icons, item['icono'].upper()),
                    color=random.choice(lista_colores()),
                    on_click=lambda e, mod=item['ruta']: pasar(mod,page),
                ),
            )
        )

    row = ft.ResponsiveRow(
        spacing=20,
        run_spacing=20,
        controls=home_cards,
    )
    
    return ft.Column(
    expand=True,
    spacing=30,
    scroll=ft.ScrollMode.AUTO,
    controls=[
        ft.Text(
            f"Bienvenido(a), {user['Nombres']}",
            size=30,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Text(
            "¿Qué deseas hacer hoy?",
            size=18,
            color=ft.Colors.GREY_700,
        ),
        ft.Divider(),
        row,
    ],
)
    
    