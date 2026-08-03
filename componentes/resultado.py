import flet as ft


class Resultado:

    def __init__(self, page):

        self.page = page

        self.icono = ft.Icon(
            ft.Icons.CHECK_CIRCLE,
            size=90,
        )

        self.titulo = ft.Text(
            size=24,
            weight=ft.FontWeight.BOLD,
        )

        self.mensaje = ft.Text(
            size=16,
            text_align=ft.TextAlign.CENTER,
        )

        self.btn = ft.ElevatedButton(
            "Aceptar",
            on_click=self.cerrar
        )

        self.contenedor = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                [
                    self.icono,
                    self.titulo,
                    self.mensaje,
                    self.btn,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            )
        )


    def mostrar_exito(self, mensaje):

        self.icono.name = ft.Icons.CHECK_CIRCLE
        self.icono.color = ft.Colors.GREEN

        self.titulo.value = "Importación completada"

        self.mensaje.value = mensaje

        self.abrir()


    def mostrar_error(self, mensaje):

        self.icono.name = ft.Icons.ERROR
        self.icono.color = ft.Colors.RED

        self.titulo.value = "Error en la operación"

        self.mensaje.value = mensaje

        self.abrir()


    def abrir(self):

        self.page.dialog = self.contenedor
        self.contenedor.open = True
        self.page.update()


    def cerrar(self, e):

        self.contenedor.open = False
        self.page.update()