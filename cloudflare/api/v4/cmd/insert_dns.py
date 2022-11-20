import sys
import requests

from cloudflare.api.v4.configs.cfg import default_credentials
from cloudflare.api.v4.configs.authorization import default_headers
from cloudflare.api.v4.models.dns import DnsRecord


def insert_new_dns():
    name: str = sys.argv[1]
    content: str = sys.argv[2]

    if (len(sys.argv) >= 4):
        record_type = sys.argv[3]
    else:
        record_type = "A"

    if (len(sys.argv) >= 5):
        proxied = bool(sys.argv[4])
    else:
        proxied = False

    response = requests.post(
        f"{default_credentials.base_url}/zones/{default_credentials.zone_id}/dns_records",
        headers=default_headers,
        json={
            "type": record_type,
            "name": name,
            "content": content,
            "proxied": proxied
        })

    # return list(map(lambda x: DnsRecord(**x), response.json()["result"]))
    return response.json()
