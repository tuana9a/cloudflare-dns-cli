import requests

from cloudflare.api.v4.configs.cfg import default_credentials
from cloudflare.api.v4.configs.authorization import default_headers
from cloudflare.api.v4.models.zone import ZoneRecord


def list_zones():
    response = requests.get(f"{default_credentials.base_url}/zones",
                            headers=default_headers)
    for x in list(map(lambda x: ZoneRecord(**x), response.json()["result"])):
        print(x)
