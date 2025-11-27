#configuracion del programa
SERVER_URL="https://api.ejemplo.com"
MAX_RETRIES = 3
TIMEOUT=10


import requests,json,time


class apiClient:

  def __init__(self):
    self.session = requests.Session()
    self.session.timeout = TIMEOUT


  def get_data(self,id):
    url = f"{SERVER_URL}/data/{id}"

    for i in range(MAX_RETRIES):
      try:
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

      except requests.exceptions.RequestException as e:
        if i == MAX_RETRIES-1: raise
        time.sleep(2**i)

    return None


def main():
  client=apiClient()
  datos = client.get_data(42)
  print(datos)