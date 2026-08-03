import flet as ft 
import modulos.cruds_all as ca
from datetime import datetime

def usuarios_view(page):
    user = page.data.get("user")
    page.title = "Panel de Roles"
    dialog_text = ft.Text("")
    #page.data = {"role_id_delete": None}
    page.scroll = "auto"

    roles_r = ca.roles_crud.get_all()

    roles_dict = {
        rol["id"]: rol["nombre"]
        for rol in roles_r
    }

    ####
    def get_form_data_user():
        return {
            "DNI": dni.value,
            "Nombres": nombre.value,
            "Apellidos": apellidos.value,
            "Activo": int(activo.value),
            "Roll_id": int(roll.value),
            "Fecha_Registro": fecha_registro.value,
        }

    ####

    dialogx = ft.AlertDialog(
        title=ft.Text("Confirmación"),
        content=dialog_text,
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=lambda e: close_dialog()
            ),
            ft.TextButton(
                "Eliminar",
                on_click=lambda e: do_delete(e)
            ),
        ],
    )

    page.overlay.append(dialogx)


    def refresh_table():

        rows = []

        for r in ca.users_crud.get_all():

            rows.append(
                ft.DataRow(
                    cells=[

                        ft.DataCell(ft.Text(str(r["id"]))),

                        ft.DataCell(ft.Text(r["DNI"])),

                        ft.DataCell(ft.Text(r["Nombres"])),

                        ft.DataCell(ft.Text(r["Apellidos"])),

                        ft.DataCell(
                            ft.Text("SI" if r["Activo"] == 1 else "NO")
                        ),

                        ft.DataCell(
                            ft.Text(
                                roles_dict.get(
                                    r["Roll_id"],
                                    "Sin rol"
                                )
                            )
                        ),

                        ft.DataCell(
                            ft.Text(r["Fecha_Registro"])
                        ),

                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color=ft.Colors.BLUE,
                                        on_click=lambda e, r=r: Edit_usuario(r)
                                    ),

                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        icon_color=ft.Colors.RED,
                                        on_click=lambda e, role_id=r["id"], role_name=r["Nombres"]+" "+r["Apellidos"]:
                                        confirm_delete(
                                            page,
                                            role_id,
                                            role_name
                                        )
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )

        table.rows = rows
        page.update()


    #/////////////////////////////////

    def limpiar():

        user_id.value = ""
        nombre.value = ""
        apellidos.value = ""
        dni.value = ""
        activo.value = ""
        roll.value = None
        fecha_registro.value = ""

        page.update()


    #/////////////////////////////////

    def agregar_usuario(e):

        ca.users_crud.insert(
            get_form_data_user()
        )
        
        limpiar()
        refresh_table()


    #/////////////////////////////////////////////

    def Edit_usuario(user):

        user_id.value = user["id"]

        dni.value = user["DNI"]

        nombre.value = user["Nombres"]

        apellidos.value = user["Apellidos"]

        activo.value = str(user["Activo"])

        roll.value = str(user["Roll_id"])

        fecha_registro.value = user["Fecha_Registro"]
        fecha_registro.disabled=True
        page.update()


    #/////////////////////////////////////////////

    def actualizar_usuario(e):

        ca.users_crud.update(
            user_id.value,
            get_form_data_user()
        )
        fecha_registro.disabled=False 
        limpiar()
        refresh_table()


    #/////////////////////////////////////////////

    def close_dialog():

        dialogx.open = False
        page.update()


    #/////////////////////////////////////////////

    def do_delete(e):

        ca.users_crud.delete(
            page.data["role_id_delete"]
        )

        dialogx.open = False

        refresh_table()

        page.update()


    #/////////////////////////////////////////////

    def confirm_delete(page, role_id, cargo):

        page.data["role_id_delete"] = role_id

        dialog_text.value = (
            f"¿Seguro que deseas eliminar al usuari@ '{cargo}'?"
        )

        dialogx.open = True

        page.update()


    #/////////////////////////////////////////////

    def fecha_cambiada(e):

        if e.control.value:

            fecha_registro.value = (
                e.control.value.strftime("%Y-%m-%d")
            )

            page.update()


    date_picker = ft.DatePicker(
        first_date=datetime(2020, 1, 1),
        last_date=datetime.now(),
        on_change=fecha_cambiada,
    )


    page.overlay.append(date_picker)


    def abrir_calendario(e):

        date_picker.open = True

        page.update()


    #////////////////////////////    

    user_id = ft.TextField(
        visible=False
    )


    nombre = ft.TextField(
        label="Nombres"
    )


    apellidos = ft.TextField(
        label="Apellido Materno y Paterno"
    )


    dni = ft.TextField(
        label="DNI"
    )


    activo = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(
                    value="1",
                    label="Activo"
                ),
                ft.Radio(
                    value="0",
                    label="Inactivo"
                )
            ],
            width=180,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


    roll = ft.Dropdown(
        width=220,
        label="Seleccione un Rol",
        options=[
            ft.DropdownOption(
                key=str(i["id"]),
                text=i["nombre"]
            )
            for i in ca.roles_crud.get_all()
        ],
    )


    fecha_registro = ft.TextField(
        label="Fecha de registro",
        read_only=True,
        suffix_icon=ft.Icons.CALENDAR_MONTH,
        on_click=abrir_calendario,
    )


    table = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("ID")),

            ft.DataColumn(ft.Text("Documento")),

            ft.DataColumn(ft.Text("Nombres")),

            ft.DataColumn(ft.Text("Apellidos")),

            ft.DataColumn(ft.Text("Activo")),

            ft.DataColumn(ft.Text("Rol")),

            ft.DataColumn(ft.Text("Fecha de registro")),

            ft.DataColumn(ft.Text("Acciones")),

        ],

        rows=[]
    )


    refresh_table()


    return ft.Column(

        [

            ft.Text(
                "CRUD USUARIOS - ADMIN PANEL",
                size=22,
                weight=ft.FontWeight.BOLD
            ),


            ft.Container(

                content=ft.Column(

                    [

                        nombre,

                        apellidos,

                        dni,

                        ft.Row(
                            [
                                ft.Text("Estado:"),
                                activo
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),

                        roll,

                        fecha_registro,

                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),

                alignment=ft.Alignment.CENTER
            ),


            ft.Container(

                content=ft.Row(

                    [

                        ft.ElevatedButton(
                            "Agregar",
                            on_click=agregar_usuario
                        ),


                        ft.ElevatedButton(
                            "Guardar cambios",
                            on_click=actualizar_usuario
                        ),

                    ],

                    alignment=ft.MainAxisAlignment.CENTER
                )
            ),


            ft.Divider(),


            ft.Container(

                content=table,

                alignment=ft.Alignment.CENTER

            ),

        ],

        horizontal_alignment=ft.CrossAxisAlignment.CENTER

    )    
    
   