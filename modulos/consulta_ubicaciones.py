import flet as ft
import modulos.cruds_all as ca
from componentes.loading  import Loading

def consulta_ubicaciones_view(page: ft.Page):

       # ===== CONTROLES =====
    txt_busqueda = ft.TextField(
        label="Valor",
        expand=True,
        hint_text="Ingrese el dato o escanee",
    )

    btn_camara = ft.IconButton(
        icon=ft.Icons.CAMERA_ALT,
        tooltip="Escanear código",
    )

    btn_buscar = ft.ElevatedButton(
        "Buscar",
        icon=ft.Icons.SEARCH,
    )

    # ===== RESULTADOS =====

    txt_codigo = ft.TextField(
        label="Código",
        read_only=True,
        expand=True,
    )

    txt_descripcion = ft.TextField(
        label="Descripción",
        read_only=True,
        expand=True,
    )

    txt_ubicacion = ft.TextField(
        label="Ubic. Picking",
        read_only=True,
        width=220,
    )
    def limpiar():
                txt_busqueda.value=""
                txt_codigo.value=""
                txt_descripcion.value=""
                txt_ubicacion.value=""
                txt_ucaja.value=""
    ddl_tipo = ft.Dropdown(
            label="Buscar por",
            width=170,
            on_text_change=limpiar,        
            options=[
                ft.dropdown.Option( text="Código",key="codigo"), 
                ft.dropdown.Option(text="EAN",key="EAN"),                       
                ft.dropdown.Option(text="Ubicación",key="ubic_pick"),            
            ],
        )

    # txt_stock = ft.TextField(
    #     label="Stock",
    #     read_only=True,
    #     width=120,
    # )

    txt_ucaja = ft.TextField(
        label="Und/Caja",
        read_only=True,
        width=120,
    )

    estado = ft.Text(color=ft.Colors.BLUE_700)

    # ===== FUNCIONES =====

    def buscar(e):

        criterio = ddl_tipo.value
        valor = txt_busqueda.value.upper().strip()

        if valor == "":
            estado.value = "Ingrese un valor para buscar."
            page.update()
            return
        else:        
            loading = Loading(page)
        try:                   
            dato= ca.productos_crud.get_by_multi(valor,criterio)
            if dato:
                  txt_codigo.value = dato["codigo"]
                  txt_descripcion.value = dato["descripcion"]
                  txt_ubicacion.value = dato["ubic_pick"]
                  txt_ucaja.value = dato["unidades_por_caja"] 
            else:
                loading.alert("ubicacion sin producto o viceversa")      
                    
        except Exception as ex:        
                print(ex)     
                loading.error("Producto sin ubic. de picking o mal código de búsqueda")   
            
        
        estado.value = f"Consulta realizada por {criterio}."

        page.update()

    def abrir_camara(e):

        estado.value = "Función de cámara pendiente de implementar."
        page.update()

    def cambio_tipo(e):

        btn_camara.disabled = ddl_tipo.value == "Nombre"
        page.update()

    ddl_tipo.on_change = cambio_tipo
    txt_busqueda.on_submit = buscar
    btn_buscar.on_click = buscar
    btn_camara.on_click = abrir_camara

    
        
    # ===== VISTA =====

    return ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.LOCATION_SEARCHING, size=30),
                        ft.Text(
                            "Consulta de Ubicaciones",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Divider(),

                # Barra horizontal de búsqueda
               ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=ddl_tipo,
                                col={"sm":12, "md":3, "lg":2},
                            ),
                            ft.Container(
                                content=txt_busqueda,
                                col={"sm":12, "md":5, "lg":7},
                            ),
                            ft.Container(
                                content=btn_camara,
                                col={"sm":6, "md":2, "lg":1},
                            ),
                            ft.Container(
                                content=btn_buscar,
                                col={"sm":6, "md":2, "lg":2},
                            ),
                        ]
                    ),

                ft.Divider(),            
                ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    content=txt_codigo,
                                    col={"sm":12, "md":3, "lg":2},
                                ),
                                ft.Container(
                                    content=txt_descripcion,
                                    col={"sm":12, "md":5, "lg":7},
                                ),
                                ft.Container(
                                    content=txt_ubicacion,
                                    col={"sm":6, "md":2, "lg":1},
                                ),
                                ft.Container(
                                    content=txt_ucaja,
                                    col={"sm":6, "md":2, "lg":2},
                                ),
                            ]
                        ),
                # ft.Row(
                #     [
                        
                #     ]),               

                estado,
            ],
            spacing=18,
        ),
    )