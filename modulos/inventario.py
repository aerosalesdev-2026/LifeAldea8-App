import flet as ft
from componentes.loading import Loading
from ocr.ocr_service import procesar_imagen
from utils.util_camara import capturar_imagenes
import modulos.cruds_all as ca
from datetime import datetime
from zoneinfo import ZoneInfo


def inventario_view(page: ft.Page):
    user = page.data.get("user")
   
    def buscar_producto(e):

        codigo = e.control.value

        if len(codigo) == 11:

            producto = ca.productos_crud.get_by_codigo(codigo)

            if producto:

                txt_nombre.value = producto["descripcion"]
            else :
                txt_nombre.value = ""

        page.update()
    # ---------------- CAMPOS ----------------
   
    txt_codigo = ft.TextField(
        label="Código de producto",
        prefix_icon=ft.Icons.QR_CODE,
        expand=True,
        on_change=lambda e:buscar_producto(e)
    )

    txt_nombre = ft.TextField(
        label="Nombre del producto",
        prefix_icon=ft.Icons.INVENTORY,
        expand=True,
        
    )

    txt_lote = ft.TextField(
        label="Lote",
        width=300,
        prefix_icon=ft.Icons.TAG,
        
    )

    txt_vencimiento = ft.TextField(
        label="Fecha de vencimiento",
        value="MM-yyyy",
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        
    )

    txt_cantidad = ft.TextField(
        label="Cantidad",
        prefix_icon=ft.Icons.NUMBERS,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    txt_ubicacion = ft.TextField(
        label="Ubicación",
        prefix_icon=ft.Icons.LOCATION_ON,
        
    )
    # txt_observaciones = ft.TextField(
    #     label="Observaciones",
    #     prefix_icon=ft.Icons.DESCRIPTION,
    #     multiline=True,
    #     min_lines=3,
    #     max_lines=5,
    # )
    estado = ft.Text(
        "Esperando escaneo...",
        size=14,
        color=ft.Colors.ORANGE,
    )
    inventario = ft.Dropdown(
        width=300,
        label="Seleccione inventario ",
        options=[
            ft.DropdownOption(key=str(i['id']),text=i['nombre']) for i in ca.inventarios_crud.get_all()
            #ft.DropdownOption(key="2", text="Supervisor"),
                ],
            )
    # ---------------- FUNCIONES ----------------
    
    def get_form_data_cont_fis():
        valor = ca.productos_crud.get_by_codigo(txt_codigo.value)
        fecha = datetime.now(ZoneInfo("America/Lima")).strftime("%Y-%m-%d %H:%M:%S")
        return {
        "inventario_id":int(inventario.value),
        "producto_id":valor["id"],
        "ubicacion": txt_ubicacion.value,
        "lote":txt_lote.value ,
        "fecha_caducidad":txt_vencimiento.value ,
        "cantidad_fisica": txt_cantidad.value,
        "operario_id": user["id"],
        "fecha_hora":fecha
            }
   
       
    def escanear(e):

        print(
            "========== ABRIENDO CÁMARA =========="
        )

        estado.value = "Cámara abierta..."

        page.update()

        ruta =capturar_imagenes(page) 

        if ruta is None:

            estado.value = (
                "Captura cancelada"
            )

            page.update()

            return


        estado.value = (
            "Procesando imagen..."
        )

        page.update()


        datos = procesar_imagen(ruta)


        print(
            "DATOS OBTENIDOS:"
        )

        print(
            datos
        )


        txt_codigo.value = (
            datos.get("codigo")
            or ""
        )


        txt_lote.value = (
            datos.get("lote")
            or ""
        )


        txt_vencimiento.value = (
            datos.get("fecha_vencimiento")
            or ""
        )


        estado.value = (
            "Etiqueta procesada correctamente"
        )
        
        if len(txt_codigo.value)==11:
           valor=ca.productos_crud.get_by_codigo(txt_codigo.value)
           txt_nombre.value=valor[2]
          
        page.update()

  
    
    
    def guardar(e):

        print("----------------")

        print(
            "Código:",
            txt_codigo.value
        )

        print(
            "Nombre:",
            txt_nombre.value
        )

        print(
            "Lote:",
            txt_lote.value
        )

        print(
            "Vencimiento:",
            txt_vencimiento.value
        )

        print(
            "Cantidad:",
            txt_cantidad.value
        )

        print(
            "Ubicación:",
            txt_ubicacion.value
        )
                
        guardado=ca.cont_fis_crud.insert(get_form_data_cont_fis())
        loading = Loading(page)
        if guardado:
           loading.exito("","producto guardado correctamente")            
           limpiar(e)
        else:
            loading.error("error en guardado de datos")   
            
        # page.snack_bar.open = True

        # page.update()


    def limpiar(e):

        txt_codigo.value = ""

        txt_nombre.value = ""

        txt_lote.value = ""

        txt_vencimiento.value = ""

        txt_cantidad.value = ""

        txt_ubicacion.value = ""

        #txt_observaciones.value = ""

        estado.value = (
            "Esperando escaneo..."
        )

        page.update()

    # ---------------- INTERFAZ ----------------

    return ft.Container(
        expand=True,

        padding=20,

        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,

            spacing=15,

            controls=[

                ft.Text(
                    "Registro de Inventario",

                    size=26,

                    weight=ft.FontWeight.BOLD,
                ),

                ft.Card(

                    content=ft.Container(

                        padding=15,

                        content=ft.Column(

                            spacing=15,

                            controls=[

                                ft.FilledButton(

                                    "Escanear etiqueta",

                                    icon=ft.Icons.CAMERA_ALT,

                                    width=250,

                                    on_click=escanear,

                                ),

                                estado,
                                inventario,

                                txt_codigo,

                                txt_nombre,

                                ft.Row(

                                    controls=[

                                        txt_lote,

                                        txt_vencimiento,

                                    ]
                                ),

                                ft.Row(

                                    controls=[

                                        txt_cantidad,

                                        txt_ubicacion,

                                    ]
                                ),

                            ],
                        ),
                    )
                ),

                ft.Row(

                    alignment=(
                        ft.MainAxisAlignment.END
                    ),

                    controls=[

                        ft.OutlinedButton(

                            "Limpiar",

                            icon=ft.Icons.CLEAR,

                            on_click=limpiar,
                        ),

                        ft.FilledButton(

                            "Guardar",

                            icon=ft.Icons.SAVE,

                            on_click=guardar,
                        ),

                    ],
                )

            ],
        ),
    )