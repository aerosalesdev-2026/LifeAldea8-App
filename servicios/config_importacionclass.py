from dataclasses import dataclass

@dataclass
class ConfigImportacion:

    nombre: str
    tabla: str
    columnas: list[str]
    columnas_bd: str
    campo_clave: str
    tam_bloque: int = 500