from servicios.config_importacionclass import ConfigImportacion


IMPORTACIONES = {
##sapDiario ES MODELO
    "sapDiario": ConfigImportacion(

        nombre="sapDiario",

        tabla="sapDiario",

        columnas=[

            "Ubicación",
            "Lote",
            "FeCaduc/FePreferCons",
            "Ctd.",
            "Producto",
            "Descripción de producto",
            "Tipo de stocks",
            "Denominación de tipo de stocks"

        ],

         columnas_bd=[
            "ubicacion",
            "lote",
            "fecha_caducidad",
            "cantidad",
            "producto",
            "descripcion_producto",
            "tipo_stock",
            "denominacion_tipo_stock"
        ],
        campo_clave="Ubicación",
        tam_bloque=500

    ),



    "picking": ConfigImportacion(

        nombre="Picking",

        tabla="picking",

        columnas=[

            "Pedido",
            "Producto",
            "Cantidad"

        ], 
         columnas_bd=[
                    "ubicacion",
                    "lote",
                    "fecha_caducidad",
                    "cantidad",
                    "producto",
                    "descripcion_producto",
                    "tipo_stock",
                    "denominacion_tipo_stock"
                ],      
        campo_clave="Ubicación",
        tam_bloque=500
    ),



    "abastecimiento": ConfigImportacion(

        nombre="Abastecimiento",

        tabla="abastecimiento",

        columnas=[

            "Ubicación",
            "Producto",
            "Cantidad"

        ],
         columnas_bd=[
                    "ubicacion",
                    "lote",
                    "fecha_caducidad",
                    "cantidad",
                    "producto",
                    "descripcion_producto",
                    "tipo_stock",
                    "denominacion_tipo_stock"
                ],
       campo_clave=""
    )

}