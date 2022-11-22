import requests
import argparse

from cloudflare.api.v4.configs.cfg import default_credentials
from cloudflare.api.v4.configs.authorization import default_headers

parser = argparse.ArgumentParser(prog="cloudflare-update-dns")

parser.add_argument("-i", "--id", help="Id of dns", required=True, type=str)

parser.add_argument("-n",
                    "--name",
                    help="Name of dns",
                    required=True,
                    type=str)

parser.add_argument("-c",
                    "--content",
                    help="Content of dns",
                    required=True,
                    type=str)

parser.add_argument("-t",
                    "--type",
                    help="Type of dns",
                    required=False,
                    type=str,
                    default="A",
                    choices=["A", "AAAA", "CNAME", "MX", "TXT"])

parser.add_argument("-p",
                    "--proxied",
                    help="Proxied",
                    required=False,
                    type=bool,
                    default=False)


def update_dns():
    args = parser.parse_args()

    id = args.id
    name = args.name
    content = args.content
    type = args.type
    proxied = args.proxied

    response = requests.put(
        f"{default_credentials.base_url}/zones/{default_credentials.zone_id}/dns_records/{id}",
        headers=default_headers,
        json={
            "type": type,
            "name": name,
            "content": content,
            "proxied": proxied
        })

    return response.json()