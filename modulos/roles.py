from tkinter import dialog

import flet as ft
import crud_roles as con

def main(page: ft.Page):

    page.title = "Panel de Roles"
    dialog_text = ft.Text("")
    page.data = {"role_id_delete": None}
    page.scroll = "auto"
    dialogx = ft.AlertDialog(
        title=ft.Text("Confirmación"),
        content=dialog_text,
        actions=[
            ft.TextButton("Cancelar",on_click=lambda e:close_dialog()),
            ft.TextButton("Eliminar",on_click=lambda e:do_delete(e)),
        ],
        )
    page.overlay.append(dialogx)
        
    def add_role(e):
        con.create_role(nombre.value, descripcion.value)
        nombre.value = ""
        descripcion.value = ""
        refresh_table()
 #/////////////////////////////////////////////       
    def refresh_table():
        rows = []

        for r in con.get_roles():
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(r[0]))),
                        ft.DataCell(ft.Text(r[1])),
                        ft.DataCell(ft.Text(r[2])),

                        ft.DataCell(
                            ft.Row([
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=ft.Colors.BLUE,
                                    on_click=lambda e, r=r: edit_role(r)
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ft.Colors.RED,
                                    on_click= lambda e, role_id=r[0],role_name=r[1]: confirm_delete(page, role_id,role_name) 
                                ),
                            ])
                        )
                    ]
                )
            )

        table.rows = rows
        page.update()
#/////////////////////////////////////////////
    def confirm_delete(page, role_id,cargo):
        page.data["role_id_delete"]=role_id
        dialog_text.value = f"¿Seguro que deseas eliminar el rol '{cargo}'?"
        dialogx.open=True
        page.update()
       
 #/////////////////////////////////////////////      
    def close_dialog():
        dialogx.open=False
        page.update()
#/////////////////////////////////////////////
    def do_delete(e):

        con.delete_role(page.data["role_id_delete"])
        dialogx.open = False
        refresh_table()
        page.update()

        
       # page.dialog = dialogclear
       
        #dialog.open = True
        #page.update()
#/////////////////////////////////////////////sfdsfdsfdsf
    def edit_role(role):
        nombre.value = role[1]
        descripcion.value = role[2]
        role_id.value = role[0]
        page.update()

    def save_edit(e):
        con.update_role(role_id.value, nombre.value, descripcion.value)
        refresh_table()

    # UI inputs
    role_id = ft.TextField(visible=False)
    nombre = ft.TextField(label="Nombre rol")
    descripcion = ft.TextField(label="Descripción")

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Descripción")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[]
    )

    page.add(
      ft.Column(
        [
            ft.Text(
                "CRUD ROLES - ADMIN PANEL",
                size=22,
                weight=ft.FontWeight.BOLD
            ),

            # Inputs centrados
            ft.Container(
                content=ft.Column(
                    [
                        nombre,
                        descripcion,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.Alignment.CENTER
            ),

            # Botones centrados en fila
            ft.Container(
                content=ft.Row(
                    [
                        ft.ElevatedButton("Agregar", on_click=add_role),
                        ft.ElevatedButton("Guardar cambios", on_click=save_edit),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ),

            ft.Divider(),

            # Tabla centrada
            ft.Container(
                content=table,
                alignment=ft.Alignment.CENTER
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    )

    refresh_table()

ft.app(target=main)  
  