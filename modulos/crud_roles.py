import conecxion 
import flet as ft

# 🔗 CONEXIÓN


# 🧠 CRUD - FUNCIONES
    
def create_role(nombre, descripcion):
    conecxion.cursor.execute(
        "INSERT INTO roles (nombre, descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conecxion.conn.commit()


def get_roles():   # 👈 AQUÍ está definida
    conecxion.cursor.execute("SELECT id, nombre, descripcion FROM roles")
    return conecxion.cursor.fetchall()


def update_role(role_id, nombre, descripcion):
    conecxion.cursor.execute(
        "UPDATE roles SET nombre=?, descripcion=? WHERE id=?",
        (nombre, descripcion, role_id)
    )
    conecxion.conn.commit()


def delete_role(role_id):
    conecxion.cursor.execute(
        "DELETE FROM roles WHERE id=?",
        (role_id,)
    )
    conecxion.conn.commit()
###############
#get general
def call_table(nom_tabla):
    conecxion.cursor.execute("SELECT id, nombre, descripcion FROM roles")
