import requests
from config import API_KEY, PROJECT_ID, DATABASE

# ==========================================
# CONFIGURACIÓN WEBLITE
# ==========================================

BASE_URL = f"https://{PROJECT_ID}.sqlite.cloud/v2/weblite"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer sqlitecloud://{PROJECT_ID}.sqlite.cloud:8860?apikey={API_KEY}"
}


# ==========================================
# EJECUTAR SQL
# ==========================================

def ejecutar_sql(sql, params=None):
    respuesta = requests.post(
        f"{BASE_URL}/sql",
        headers=HEADERS,
        json={
            "database": DATABASE,
            "sql": sql,
            "params": params or []
        }
    )

    respuesta.raise_for_status()

    return respuesta.json()["data"]