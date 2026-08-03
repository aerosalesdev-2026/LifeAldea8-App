from fastapi import FastAPI, UploadFile, File
from paddleocr import PaddleOCR
import cv2
import numpy as np
import tempfile
import os

app = FastAPI()

ocr = PaddleOCR(
    use_textline_orientation=True,
    lang="en"
)

@app.post("/ocr")
async def leer(file: UploadFile = File(...)):

    contenido = await file.read()

    imagen = cv2.imdecode(
        np.frombuffer(contenido, np.uint8),
        cv2.IMREAD_COLOR
    )

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    cv2.imwrite(temp.name, imagen)

    resultado = ocr.predict(temp.name)

    os.unlink(temp.name)

    return {
        "resultado": resultado
    }