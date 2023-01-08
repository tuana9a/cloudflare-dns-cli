import requests
import argparse
import json

from cloudflarednscli.configs import cfg

parser = argparse.ArgumentParser(prog="cloudflare insert dns")

parser.add_argument("dns_name", help="Name of dns record", type=str)

parser.add_argument("dns_content", help="Content of dns record", type=str)

parser.add_argument("-t",
                    "--type",
                    help="Type of dns record",
                    required=False,
                    type=str,
                    default="A",
                    choices=["A", "AAAA", "CNAME", "MX", "TXT"])

parser.add_argument("-p",
                    "--proxied",
                    help="Proxied status",
                    action="store_const",
                    const=True)


def run(parent_args: argparse.Namespace):
    args = parser.parse_args(parent_args.remains)

    name = args.dns_name
    content = args.dns_content
    type = args.type
    proxied = args.proxied

    response = requests.post(f"{cfg.base_url}/zones/{cfg.zone_id}/dns_records",
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
