# import modulos.conecxion 
# import flet as ft 

# ###CREAR CRUDS GENERALES###

import modulos.conecxion as conexion


class CRUD:

    def __init__(self, table):
        self.table = table

    # ==========================
    # OBTENER_TODO
    # ==========================

    def get_all(self):

        sql = f"""
        SELECT * 
        FROM {self.table}
        """

        return conexion.ejecutar_sql(sql)

    # ==========================
    # BUSCAR POR ID
    # ==========================

    def get_by_id(self, id):

        sql = f"""
        SELECT *
        FROM {self.table}
        WHERE id = {id}
        """

        data = conexion.ejecutar_sql(sql)

        return data[0] if data else None

    # ==========================
    # BUSCAR CODIGO
    # ==========================

    def get_by_codigo(self,codigo):

        sql = f"""
        SELECT *
        FROM {self.table}
        WHERE codigo = '{codigo}'
        """

        data = conexion.ejecutar_sql(sql)

        return data[0] if data else None

    # ==========================
    # BUSQUEDA MULTIPLE
    # ==========================

    def get_by_multi(self,valor,columna):

        sql=f"""
        SELECT *
        FROM {self.table}
        WHERE {columna} = '{valor}'
        """


        data=conexion.ejecutar_sql(sql)

        return data[0] if data else None

    # ==========================
    # INSERTAR
    # ==========================

    def insert(self,data:dict):

        columnas=", ".join(data.keys())


        valores=", ".join(
            [
                f"'{v}'"
                for v in data.values()
            ]
        )
        sql=f"""
        INSERT INTO {self.table}
        ({columnas})
        VALUES
        ({valores})
        """
        conexion.ejecutar_sql(sql)

        return True
    # ==========================
    # ACTUALIZAR
    # ==========================
    def update(self,id,data:dict):
        campos=", ".join(
            [
                f"{k}='{v}'"
                for k,v in data.items()
            ]
        )


        sql=f"""
        UPDATE {self.table}
        SET {campos}
        WHERE id={id}
        """


        conexion.ejecutar_sql(sql)

        return True

    # ==========================
    # ELIMINAR
    # ==========================

    def delete(self,id):

        sql=f"""
        DELETE FROM {self.table}
        WHERE id={id}
        """

        conexion.ejecutar_sql(sql)

        return True

    # ==========================
    # MODULOS POR ROL
    # ==========================

    def getmodulo_by_roles(self,id):

        sql=f"""
        SELECT *
        FROM rol_modulos
        WHERE rol_id={id}
        """

        return conexion.ejecutar_sql(sql)

    # ==========================
    # LIMPIAR TABLA
    # ==========================

    def limpiar_tabla(self,tabla):

        sql=f"""
        DELETE FROM {tabla}
        """

        conexion.ejecutar_sql(sql)

        return True

users_crud = CRUD("users")
roles_crud = CRUD("roles")
modulos_crud = CRUD("modulos")
rol_modulos_crud = CRUD("rol_modulos")
sapDiario_crud = CRUD("sapDiario")
cont_fis_crud = CRUD("conteos_fisicos")
productos_crud = CRUD("productos")
inventarios_crud = CRUD("inventarios")    