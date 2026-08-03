import cv2
from paddleocr import PaddleOCR
from extractor import extraer_datos


ocr = PaddleOCR(
    lang="es"
)


def capturar_imagen():

    camara = cv2.VideoCapture(0)

    nombre_ventana = (
        "CAMARA - ESPACIO: capturar | ESC: salir"
    )

    while True:

        ret, frame = camara.read()

        if not ret:

            print("No se pudo acceder a la cámara")

            camara.release()
            cv2.destroyAllWindows()

            return None

        cv2.imshow(
            nombre_ventana,
            frame
        )

        tecla = cv2.waitKey(1) & 0xFF

        # ESPACIO = capturar
        if tecla == 32:

            ruta = "captura.jpg"

            cv2.imwrite(
                ruta,
                frame
            )

            print("\nImagen capturada")

            camara.release()
            cv2.destroyAllWindows()

            return ruta

        # ESC = salir
        elif tecla == 27:

            print("\nCancelado")

            camara.release()
            cv2.destroyAllWindows()

            return None


def mejorar_imagen(ruta_original):

    imagen = cv2.imread(
        ruta_original
    )

    gris = cv2.cvtColor(
        imagen,
        cv2.COLOR_BGR2GRAY
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    mejorada = clahe.apply(
        gris
    )

    _, binaria = cv2.threshold(
        mejorada,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imwrite(
        "captura_mejorada.jpg",
        mejorada
    )

    cv2.imwrite(
        "captura_binaria.jpg",
        binaria
    )

    return [
        ruta_original,
        "captura_mejorada.jpg",
        "captura_binaria.jpg"
    ]


def leer_imagen(ruta):

    print("\n")
    print("=" * 50)
    print(f"ANALIZANDO: {ruta}")
    print("=" * 50)

    resultado = ocr.predict(
        ruta
    )

    textos = []

    for r in resultado:

        textos.extend(
            r["rec_texts"]
        )

    for texto in textos:

        print(texto)

    return textos


# 1. Abrir cámara y tomar foto
ruta = capturar_imagen()
# 2. Solo continuar si realmente se tomó una foto
if ruta:
    textos = leer_imagen(ruta)
    
    datos = extraer_datos( textos)
    print(datos)