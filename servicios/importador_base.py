import pandas as pd
from modulos.conecxion import ejecutar_sql
import modulos.cruds_all as crud
from servicios.config_importaciones import IMPORTACIONES


class ImportadorBase:

    # -----------------------------
    # Leer Excel
    # -----------------------------
    def leer_excel(self, ruta):

        df = pd.read_excel(ruta)
        df.columns = df.columns.str.strip()
        df = df.dropna(how="all")

        # elimina filas sin ubicación
        if "Ubicación" in df.columns:
            df = df[df["Ubicación"].notna()]

        return df

    # -----------------------------
    # Validar columnas
    # -----------------------------
    def validar_columnas(self, df, columnas_requeridas):

        faltantes = [
            c for c in columnas_requeridas
            if c not in df.columns
        ]

        if faltantes:
            raise Exception(
                "Faltan las columnas:\n\n"
                + "\n".join(faltantes)
            )

    # -----------------------------
    # Limpiar valores
    # -----------------------------
    def limpiar_valor(self, valor):

        if pd.isna(valor):
            return None

        if isinstance(valor, pd.Timestamp):
            return valor.strftime("%Y-%m-%d")

        if hasattr(valor, "item"):
            return valor.item()

        return valor

    # -----------------------------
    # Convertir DataFrame
    # -----------------------------
    def dataframe_a_tuplas(self, df):

        datos = []

        for _, fila in df.iterrows():

            datos.append(
                tuple(
                    self.limpiar_valor(v)
                    for v in fila
                )
            )

        return datos

    # -----------------------------
    # Insertar por bloques
    # -----------------------------
    def insertar_masivo(
        self,
        datos,
        tabla,
        columnas_bd,
        tam_bloque,
        loading=None
    ):

        total = len(datos)
        procesados = 0

        columnas_sql = ",".join(columnas_bd)

        for i in range(0, total, tam_bloque):

            bloque = datos[i:i + tam_bloque]

            valores = []

            for fila in bloque:

                fila_sql = []

                for valor in fila:

                    if valor is None:
                        fila_sql.append("NULL")

                    elif isinstance(valor, str):
                        valor = valor.replace("'", "''")
                        fila_sql.append(f"'{valor}'")

                    else:
                        fila_sql.append(str(valor))

                valores.append(
                    "(" + ",".join(fila_sql) + ")"
                )

            sql = f"""
            INSERT INTO {tabla}
            ({columnas_sql})
            VALUES
            {",".join(valores)}
            """

            ejecutar_sql(sql)

            procesados += len(bloque)

            if loading:
                loading.update(
                    procesados,
                    total
                )

        return procesados

    # -----------------------------
    # Método principal
    # -----------------------------
    def importar(
        self,
        ruta_excel,
        modulo,
        loading=None
    ):

        if modulo not in IMPORTACIONES:

            raise Exception(
                f"No existe configuración para '{modulo}'"
            )

        config = IMPORTACIONES[modulo]

        print(f"Importando {config.nombre}")

        df = self.leer_excel(ruta_excel)

        self.validar_columnas(
            df,
            config.columnas
        )

        df = df[config.columnas]

        datos = self.dataframe_a_tuplas(df)

        # Limpiar tabla antes de importar
        crud.sapDiario_crud.limpiar_tabla(config.tabla)

        cantidad = self.insertar_masivo(
            datos,
            config.tabla,
            config.columnas_bd,
            config.tam_bloque,
            loading
        )

        return cantidad