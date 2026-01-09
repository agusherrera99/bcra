import requests

from typing import Dict, Optional

class BCRA:
    def __init__(self):
        self.base_url: str = "https://api.bcra.gob.ar/estadisticas/v4.0"
        self.categories_map: Optional[Dict[str, int]] = {}

    def get_category_id(self, category: str) -> Optional[int]:
        try:
            return self.categories_map[category]
        except:
            return None


class Monetarias(BCRA):
    def __init__(self):
        super().__init__()
        self.base_url: str = f"{self.base_url}/monetarias"
        
        self._set_categories_map()

    def _set_categories_map(self):
        self.categories_map['tipo_cambio_minorista'] = 4
        self.categories_map['tasa_depositos_30'] = 12
        self.categories_map["ipc_mensual"] = 27
        self.categories_map['ipc_interanual'] = 28

    def get_category_id(self, category: str):
        return self.categories_map.get(category, None)

    def get_ipc(self, from_date: Optional[str] = None):
        category_id = self.get_category_id("ipc")
        url = f"{self.base_url}/{category_id}?desde={from_date}" if from_date else f"{self.base_url}/{category_id}"

        try:
            req = requests.get(
                url,
                verify=False
            )
            if req.status_code == 200:
                return req.json()
            return None
        except Exception as e:
            print(f"Error al intentar obtener los datos del IPC: {e}")
            return None

    def get_data(self, category: str, from_date: Optional[str] = None):
        category_id = self.get_category_id(category)

        if from_date: 
            url = f"{self.base_url}/{category_id}?desde={from_date}" 
        else:
            url = f"{self.base_url}/{category_id}"

        try:
            req = requests.get(
                url,
                verify=False
            )
            if req.status_code == 200:
                data = req.json()
                return data['results'][0]['detalle'] if data else None
            return None
        except Exception as error:
            print(f"Error al intentar obtener datos: {error}")
            return None
