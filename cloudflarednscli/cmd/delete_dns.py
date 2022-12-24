import sys
import requests
import json
import argparse

from cloudflarednscli.configs import cfg

parser = argparse.ArgumentParser(prog="cloudflare delete dns")

parser.add_argument("dns_id", help="Id of dns record", type=str)


def run(parent_args: argparse.Namespace):
    args = parser.parse_args(parent_args.remains)
    id = args.dns_id

    response = requests.delete(
        f"{cfg.base_url}/zones/{cfg.zone_id}/dns_records/{id}",
        headers={
            "X-Auth-Email": cfg.email,
            "Authorization": f"Bearer {cfg.access_token}",
            "Content-Type": "application/json"
        })
    print(json.dumps(response.json(), indent=2))