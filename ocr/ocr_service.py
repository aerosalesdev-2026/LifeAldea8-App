from paddleocr import PaddleOCR

from ocr.extractor import extraer_datos


ocr = PaddleOCR(
    lang="es"
)


def procesar_imagen(ruta_imagen):

    resultado = ocr.predict(
        ruta_imagen
    )

    textos = []

    for r in resultado:

        textos.extend(
            r["rec_texts"]
        )

    datos = extraer_datos(
        textos
    )

    return datos