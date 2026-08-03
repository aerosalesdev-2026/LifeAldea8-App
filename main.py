import flet as ft
import router
import actualizador


async def main(page: ft.Page):
    print("FLET CONECTADO")
    page.title = "LIFE ALDEA 8"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # Revisar actualización
    nueva_version = actualizador.comprobar_actualizacion()


    if nueva_version:

        def actualizar(e):

            ruta_apk = actualizador.descargar_apk(page,nueva_version["apk"])

            print("APK descargado:", ruta_apk)


        dialog = ft.AlertDialog(

            title=ft.Text(
                "Nueva actualización disponible"
            ),

            content=ft.Text(
                nueva_version["mensaje"]
            ),

            actions=[

                ft.ElevatedButton(
                    "Actualizar",
                    on_click=actualizar
                )

            ]

        )


        page.dialog = dialog

        dialog.open = True

        page.update()



    # Continuar con la app
    if not nueva_version:
     router.configurar_router(page)

print("ANTES DE INICIAR FLET")

ft.run(
    main,
    view=ft.AppView.WEB_BROWSER,
    port=8550
)