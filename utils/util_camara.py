import flet as ft
from utils.camara_nopc import take_foto
from utils.camara_pc import capturar_imagen

def capturar_imagenes(page: ft.Page):

    if page.platform == ft.PagePlatform.ANDROID:
        return take_foto(page)

    else:
        return capturar_imagen()