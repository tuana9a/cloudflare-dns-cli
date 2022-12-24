import requests

from cloudflarednscli.configs import cfg
from cloudflarednscli.models.zone import ZoneRecord


def run(parent_args):
    response = requests.get(f"{cfg.base_url}/zones",
                            headers={
                                "X-Auth-Email": cfg.email,
                                "Authorization": f"Bearer {cfg.access_token}",
                                "Content-Type": "application/json"
                            })
    for x in list(map(lambda x: ZoneRecord(**x), response.json()["result"])):
        print(x)
