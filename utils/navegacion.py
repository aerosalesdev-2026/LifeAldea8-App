import modulos.login as login
import flet as ft
import asyncio

def ir_login(page):
    page.clean()
    page.appbar = None
    page.overlay.clear()
    page.data.clear()
    page.add(login.crear_login(page))
    page.update()
    



def cerrar_aplicacion(page: ft.Page):
    asyncio.create_task(page.window.close())
    
def lista_colores():
    NO_PERMITIDOS = [
        "TRANSPARENT",
        "WHITE",
        "BLACK",
        "SURFACE",
        "SURFACE_CONTAINER",
        "SURFACE_TINT",
        "SHADOW",
        "SCRIM",
        "OUTLINE",
        "OUTLINE_VARIANT",
        "INVERSE",
        "ON_",
        "PRIMARY_FIXED",
        "SECONDARY_FIXED",
        "TERTIARY_FIXED",
    ]

    TONOS_PERMITIDOS = (
        "_300",
        "_400",
        "_500",
        "_600",
        "_700",
    )

    COLORES_CARDS = [
        getattr(ft.Colors, nombre)
        for nombre in dir(ft.Colors)
        if (
            nombre.isupper()
            and nombre.endswith(TONOS_PERMITIDOS)
            and not any(p in nombre for p in NO_PERMITIDOS)
        )
    ]
    return COLORES_CARDS
def pasar(ruta,page):
    
        page.route = ruta
        page.on_route_change(None)
        
      