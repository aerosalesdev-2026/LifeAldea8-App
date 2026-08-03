from paddleocr import PaddleOCR

from ocr.extractor import extraer_datos


ocr = None


def obtener_ocr():
    global ocr

    if ocr is None:
        print("Inicializando PaddleOCR...")

        ocr = PaddleOCR(
            lang="es"
        )

        print("PaddleOCR listo")

    return ocr


def procesar_imagen(ruta_imagen):

    motor_ocr = obtener_ocr()

    resultado = motor_ocr.predict(
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