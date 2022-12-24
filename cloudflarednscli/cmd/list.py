import argparse
import importlib

parser = argparse.ArgumentParser(prog="cloudflarednscli list")

parser.add_argument("target",
                    help="DNS or ZONE",
                    type=str,
                    choices=["dns", "zone"])

parser.add_argument("remains",
                    type=str,
                    nargs=argparse.REMAINDER,
                    help="Child opts")


def run(parent_args: argparse.Namespace):
    args = parser.parse_args(parent_args.remains)
    m = importlib.import_module(f"cloudflarednscli.cmd.list_{args.target}")
    m.run(args)