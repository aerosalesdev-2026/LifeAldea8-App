import re

def extraer_codigo(textos):

    # El OCR puede omitir ceros.
    # Formato real: XX-XXXXXXXX

    patron = r"(?<!\d)(\d{2})-(\d+)(?!\d)"

    for texto in textos:

        coincidencia = re.search(
            patron,
            str(texto)
        )

        if coincidencia:

            familia = coincidencia.group(1)

            numero = coincidencia.group(2)

            # Completar con ceros a la izquierda
            # hasta llegar a 8 dígitos

            numero = numero.zfill(8)

            return f"{familia}-{numero}"

    return None


def extraer_lote(textos):

    for i, texto in enumerate(textos):

        texto = str(
            texto
        ).strip()

        # Caso:
        # Lote/Lot:B000700526
        # LOTELOT:B000700526
        coincidencia = re.search(
            r"LOTE\s*/?\s*LOT\s*:?\s*([A-Z0-9]+)",
            texto,
            re.IGNORECASE
        )

        if coincidencia:

            lote = coincidencia.group(1)

            # Evitar devolver "Codigo" como lote
            if lote.upper() not in [
                "CODIGO",
                "CODE"
            ]:

                return lote

        # Caso:
        # LOTELOT
        # B000700526 Codigo/Code:...
        if re.search(
            r"LOTE\s*/?\s*LOT",
            texto,
            re.IGNORECASE
        ):

            if i + 1 < len(textos):

                siguiente = str(
                    textos[i + 1]
                ).strip()

                coincidencia = re.match(
                    r"([A-Z0-9]+)",
                    siguiente,
                    re.IGNORECASE
                )

                if coincidencia:

                    return coincidencia.group(1)

    return None


def extraer_cantidad_caja(textos):

    for i, texto in enumerate(textos):

        texto = str(texto).strip()

        # Ejemplos:
        # 12 UND
        # 12Unid.
        # 12 Unld.
        coincidencia = re.search(
            r"\b(\d+(?:\.\d+)?)\s*[A-Z]{2,6}\.?\b",
            texto,
            re.IGNORECASE
        )

        if coincidencia:

            numero = float(
                coincidencia.group(1)
            )

            # Evitar capturar otros números
            # que no sean cantidades
            if numero > 0:

                return numero

        # Caso:
        # Cantidad:
        # 50.00
        if re.search(
            r"canti\s*dad",
            texto,
            re.IGNORECASE
        ):

            for siguiente in textos[i + 1:i + 4]:

                coincidencia = re.search(
                    r"^\s*(\d+(?:\.\d+)?)\s*"
                    r"[A-Z]{2,6}\.?\s*$",
                    str(siguiente),
                    re.IGNORECASE
                )

                if coincidencia:

                    return float(
                        coincidencia.group(1)
                    )

    return None


def extraer_bulto(textos):

    patron = r"(?<!\d)(\d{1,2})\s*/\s*(\d{1,2})(?!\d)"

    for texto in textos:

        texto = str(
            texto
        ).strip()

        coincidencia = re.fullmatch(
            patron,
            texto
        )

        if coincidencia:

            bulto_actual = int(
                coincidencia.group(1)
            )

            total_bultos = int(
                coincidencia.group(2)
            )

            # Validar que tenga sentido
            if (
                bulto_actual <= total_bultos
                and total_bultos > 1
            ):

                return {
                    "bulto_actual": bulto_actual,
                    "total_bultos": total_bultos
                }

    return {
        "bulto_actual": None,
        "total_bultos": None
    }
    
def extraer_vencimiento(textos):

    for i, texto in enumerate(textos):

        texto = str(texto).strip()

        # Fecha en el mismo texto
        coincidencia = re.search(
            r"(?:Vencim|Due\s*D).*?"
            r"(0?[1-9]|1[0-2])[-/](20\d{2})",
            texto,
            re.IGNORECASE
        )

        if coincidencia:

            mes = coincidencia.group(1).zfill(2)

            anio = coincidencia.group(2)

            return f"{mes}-{anio}"

        # Fecha en el texto siguiente
        if re.search(
            r"Vencim|Due\s*D",
            texto,
            re.IGNORECASE
        ):

            for siguiente in textos[i + 1:i + 3]:

                coincidencia = re.search(
                    r"(?<!\d)(0?[1-9]|1[0-2])[-/](20\d{2})(?!\d)",
                    str(siguiente)
                )

                if coincidencia:

                    mes = coincidencia.group(1).zfill(2)

                    anio = coincidencia.group(2)

                    return f"{mes}-{anio}"

    return None

def extraer_datos(textos):

    bulto = extraer_bulto(
        textos
    )

    return {

        "tipo": "caja",

        "codigo": extraer_codigo(
            textos
        ),

        "lote": extraer_lote(
            textos
        ),

        "cantidad_caja": extraer_cantidad_caja(
            textos
        ),
        "fecha_vencimiento": extraer_vencimiento(
            textos
        ),

        "bulto_actual": bulto[
            "bulto_actual"
        ],

        "total_bultos": bulto[
            "total_bultos"
        ]

    }

