import flet as ft
from modulos import login, home,inventario,mantenimiento,consulta_ubicaciones,usuarios

def configurar_router(page: ft.Page):

    def route_change(e=None):        
       # print("Entró al router:", page.route)
        page.clean()
        match page.route:
            case "/":
                page.overlay.clear()
                page.appbar = None
                page.add(login.crear_login(page))
            case "/home":
                page.add(home.home_view(page))                
            case "/inventario":
                page.add(inventario.inventario_view(page))
            case "/mantenimiento":
                page.add(mantenimiento.mantenimiento_view(page))
            case "/consulta_ubi":
                page.add(consulta_ubicaciones.consulta_ubicaciones_view(page))
            case "/user":
                page.add(usuarios.usuarios_view(page))
            case _:
                page.add(ft.Text("Página no encontrada"))

        page.update()

    page.on_route_change = route_change

    # Construye la vista inicial
    route_change()