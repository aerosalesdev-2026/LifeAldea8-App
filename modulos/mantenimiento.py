import flet as ft
#from servicios.importar_excel import Importador,importar_inventario
from servicios.importador_base import ImportadorBase
import asyncio
from componentes.loading import Loading
from componentes.resultado import Resultado
from utils.navegacion import pasar

def mantenimiento_view(page):

    titulo = ft.Text(
        "Mantenimiento",
        size=30,
        weight=ft.FontWeight.BOLD
    )   
    
    # -----------------------------
    # Selector de archivos    
    file_picker = ft.FilePicker()
    page.services.append(file_picker)
   # file_picker.on_result = archivo_seleccionado
       
    async def abrir_archivo():
        resultado = await file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"]
        )

        if not resultado:
            return

        archivo = resultado[0]

        loading = Loading(page)

        loading.show("Importando inventario")

        await asyncio.sleep(0.1)

        impbas = ImportadorBase()

        try:

            cantidad = await asyncio.to_thread( impbas.importar, archivo.path, "sapDiario", loading )
            loading.exito(
                f"Importación completada","Se importaron {cantidad} registros correctamente."
            )


        except Exception as e:     
            print(repr(e))
            loading.hide()

        finally:

            print("")
   
                 
    def click_importar(e):
        page.run_task(abrir_archivo)    
    # -----------------------------
    btn_importar = ft.ElevatedButton(
        "Cargar productos out_SAP",
        icon=ft.Icons.UPLOAD_FILE,
        on_click=click_importar           
    )
    btn_user = ft.ElevatedButton(
        "USERS",
        icon=ft.Icons.PERSON,
        on_click=lambda e:pasar("/user",page)           
    )
    permisos = ft.Column(
        controls=[
            ft.Checkbox(label="Inventario"),
            ft.Checkbox(label="Picking"),
            ft.Checkbox(label="Abastecimiento"),
            ft.Checkbox(label="Dashboard"),
        ]
    )

    return ft.Column(
        controls=[
            titulo,
            ft.Divider(),

            ft.Text("Importación de datos"),

            btn_importar,
            ft.Text("Administración de usuarios"),

            btn_user,

            ft.Divider(),

            ft.Text("Permisos de usuario"),

            permisos,

            ft.ElevatedButton(
                "Guardar cambios"
            )
        ]
    )