import cv2


def capturar_imagen():

    camara = cv2.VideoCapture(0)

    if not camara.isOpened():

        print("No se pudo abrir la cámara")

        return None


    while True:

        ret, frame = camara.read()

        if not ret:

            print("No se pudo capturar imagen")

            break


        cv2.imshow(
            "Camara - Presiona ESPACIO para capturar",
            frame
        )


        tecla = cv2.waitKey(1) & 0xFF


        if tecla == 32:  # ESPACIO

            ruta = "captura.jpg"

            cv2.imwrite(
                ruta,
                frame
            )

            camara.release()

            cv2.destroyAllWindows()

            return ruta


        elif tecla == 27:  # ESC

            camara.release()

            cv2.destroyAllWindows()

            return None