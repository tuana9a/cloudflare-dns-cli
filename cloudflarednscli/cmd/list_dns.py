import requests
import argparse

from cloudflarednscli.configs import cfg
from cloudflarednscli.models.dns import DnsRecord

parser = argparse.ArgumentParser(prog="cloudflarednscli list dns")

parser.add_argument("-n", "--name", action="store_const", const=True)


def run(parent_args: argparse.Namespace = argparse.Namespace()):
    args = parser.parse_args(parent_args.remains)
    response = requests.get(f"{cfg.base_url}/zones/{cfg.zone_id}/dns_records",
                            headers={
                                "X-Auth-Email": cfg.email,
                                "Authorization": f"Bearer {cfg.access_token}",
                                "Content-Type": "application/json"
                            })
    dns_records = []

    for x in response.json()["result"]:
        dns_records.append(DnsRecord(**x))

    if (args.name):
        for x in dns_records:
            print(" ".join([x.id, x.name]))
        return

    for x in dns_records:
        print(x)