import flet as ft


class Loading:

    def __init__(self, page: ft.Page):

        self.page = page
        self.ring = ft.ProgressRing()

        self.icono = ft.Icon(
            ft.Icons.CHECK_CIRCLE,
            color=ft.Colors.GREEN,
            size=90,
            visible=False,
        )
        self.lbl_titulo = ft.Text(
            "Procesando...",
            size=22,
            weight=ft.FontWeight.BOLD,
        )
        self.btn_aceptar = ft.ElevatedButton(
            "Aceptar",
            visible=False,
            on_click=lambda e:self.hide(),
        )
        self.progress = ft.ProgressBar(
            width=450,
            value=0,
        )

        self.lbl_porcentaje = ft.Text(
            "0 %",
            size=18,
            weight=ft.FontWeight.BOLD,
        )

        self.lbl_estado = ft.Text(
            "Preparando..."
        )

        self.overlay = ft.Container(
            expand=True,
            bgcolor=ft.Colors.with_opacity(
                0.45,
                ft.Colors.BLACK,
            ),
            alignment=ft.Alignment.CENTER,
            content=ft.Container(
                width=600,
                padding=30,
                border_radius=15,
                bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                    [
                        self.ring,
                        self.icono,                
                        self.lbl_titulo,
                        self.progress,

                        self.lbl_porcentaje,

                        self.lbl_estado,
                        self.btn_aceptar
                    ],
                    tight=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        )

    def show(self, titulo="Procesando..."):   
        self.ring.visible = True

        self.icono.visible = False

        self.progress.visible = True
        self.progress.value = 0

        self.lbl_porcentaje.visible = True
        self.lbl_porcentaje.value = "0 %"

        self.lbl_estado.value = "Preparando..."

        self.btn_aceptar.visible = False

        self.lbl_titulo.value = titulo

        if self.overlay not in self.page.overlay:
            self.page.overlay.append(self.overlay)

        self.page.update()

    def update(self, procesados, total):

        progreso = procesados / total

        async def actualizar():

            self.progress.value = progreso

            self.lbl_porcentaje.value = (
                f"{progreso*100:.1f}%"
            )

            self.lbl_estado.value = (
                f"{procesados} de {total} registros"
            )

            self.page.update()

        self.page.run_task(actualizar)

    def hide(self,e=None):

        if self.overlay in self.page.overlay:
            self.page.overlay.remove(self.overlay)

        self.page.update()
    
    def exito(self,titulo, mensaje):
        if self.overlay not in self.page.overlay:
            self.page.overlay.append(self.overlay)
        
        self.ring.visible = False

        self.icono.icon = ft.Icons.CHECK_CIRCLE
        self.icono.color = ft.Colors.GREEN
        self.icono.visible = True

        self.progress.visible = False
        self.lbl_porcentaje.visible = False

        self.lbl_titulo.value = titulo

        self.lbl_estado.value = mensaje

        self.btn_aceptar.visible = True

        self.page.update()  
        print(self.overlay in self.page.overlay)
            
    def error(self, mensaje):
        if self.overlay not in self.page.overlay:
            self.page.overlay.append(self.overlay)
             
        self.ring.visible = False

        self.icono.icon = ft.Icons.CANCEL
        self.icono.color = ft.Colors.RED
        self.icono.visible = True

        self.progress.visible = False
        self.lbl_porcentaje.visible = False

        self.lbl_titulo.value = "Error"

        self.lbl_estado.value = mensaje

        self.btn_aceptar.visible = True

        self.page.update() 
        
    def alert(self, mensaje):
        if self.overlay not in self.page.overlay:
            self.page.overlay.append(self.overlay)
             
        self.ring.visible = False

        self.icono.icon = ft.Icons.WARNING_AMBER
        self.icono.color = ft.Colors.YELLOW
        self.icono.visible = True

        self.progress.visible = False
        self.lbl_porcentaje.visible = False

        self.lbl_titulo.value = "Error"

        self.lbl_estado.value = mensaje

        self.btn_aceptar.visible = True

        self.page.update() 
         