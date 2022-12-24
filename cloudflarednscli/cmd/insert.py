import argparse
import importlib

parser = argparse.ArgumentParser(prog="cloudflarednscli insert")

parser.add_argument("target", help="DNS", type=str, choices=["dns"])

parser.add_argument("remains",
                    type=str,
                    nargs=argparse.REMAINDER,
                    help="Child opts")


def run(parent_args: argparse.Namespace):
    args = parser.parse_args(parent_args.remains)
    m = importlib.import_module(f"cloudflarednscli.cmd.insert_{args.target}")
    m.run(args)