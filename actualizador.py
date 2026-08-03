import requests
import version,os


URL_VERSION = "https://github.com/aerosalesdev-2026/LifeAldea8-Updates/releases/download/v1.0.0/version.json"


def comprobar_actualizacion():

    try:
        r = requests.get(
            URL_VERSION,
            timeout=10
        )

        datos = r.json()

        if datos["version"] != version.VERSION:
            return datos

    except Exception as e:
        print(e)

    return None

def descargar_apk(page, url):

    try:

        carpeta = page.get_directory_path()

        ruta = os.path.join(
            carpeta,
            "LifeAldea8_update.apk"
        )


        respuesta = requests.get(
            url,
            stream=True,
            timeout=60
        )


        with open(ruta, "wb") as archivo:

            for bloque in respuesta.iter_content(
                1024
            ):
                archivo.write(bloque)


        return ruta


    except Exception as e:

        print(
            "Error descargando APK:",
            e
        )

        return None