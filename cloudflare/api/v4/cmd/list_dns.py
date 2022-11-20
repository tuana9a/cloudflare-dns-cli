import requests

from cloudflare.api.v4.configs.cfg import default_credentials
from cloudflare.api.v4.configs.authorization import default_headers
from cloudflare.api.v4.models.dns import DnsRecord


def list_dns_records():
    response = requests.get(
        f"{default_credentials.base_url}/zones/{default_credentials.zone_id}/dns_records",
        headers=default_headers)
    for x in list(map(lambda x: DnsRecord(**x), response.json()["result"])):
        print(x)