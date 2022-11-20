import sys
import requests

from cloudflare.api.v4.configs.cfg import default_credentials
from cloudflare.api.v4.configs.authorization import default_headers
from cloudflare.api.v4.models.dns import DnsRecord


def delete_dns_by_id(**kwargs):
    _, id = sys.argv
    response = requests.delete(
        f"{default_credentials.base_url}/zones/{default_credentials.zone_id}/dns_records/{id}",
        headers=default_headers)
    return response.json()