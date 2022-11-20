import sys
import requests

from cloudflare.api.v4.configs.cfg import default_credentials
from cloudflare.api.v4.configs.authorization import default_headers


def update_dns():
    record_id = sys.argv[1]
    name = sys.argv[2]
    content = sys.argv[3]

    if (len(sys.argv) >= 5):
        record_type = sys.argv[4]
    else:
        record_type = "A"

    if (len(sys.argv) >= 6):
        proxied = bool(sys.argv[5])
    else:
        proxied = False

    record_type = "A"
    proxied = False
    if not record_type: record_type = "A"
    proxied = bool(proxied)
    response = requests.put(
        f"{default_credentials.base_url}/zones/{default_credentials.zone_id}/dns_records/{record_id}",
        headers=default_headers,
        json={
            "type": record_type,
            "name": name,
            "content": content,
            "proxied": proxied
        })

    return response.json()