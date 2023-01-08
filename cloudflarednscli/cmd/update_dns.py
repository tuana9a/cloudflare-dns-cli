import requests
import argparse
import json

from cloudflarednscli.configs import cfg

parser = argparse.ArgumentParser(prog="cloudflarednscli update dns")

parser.add_argument("dns_id", help="Id of dns record", type=str)

parser.add_argument("dns_name", help="Name of dns record", type=str)

parser.add_argument("dns_content", help="Content of dns", type=str)

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
                    action="store_const",
                    const=True)


def run(parent_args: argparse.Namespace):
    args = parser.parse_args(parent_args.remains)

    id = args.dns_id
    name = args.dns_name
    content = args.dns_content
    type = args.type
    proxied = args.proxied

    response = requests.put(
        f"{cfg.base_url}/zones/{cfg.zone_id}/dns_records/{id}",
        headers={
            "X-Auth-Email": cfg.email,
            "Authorization": f"Bearer {cfg.access_token}",
            "Content-Type": "application/json"
        },
        json={
            "type": type,
            "name": name,
            "content": content,
            "proxied": proxied
        })

    print(json.dumps(response.json(), indent=2))