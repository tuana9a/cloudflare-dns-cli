import argparse
import importlib
import configparser

from cloudflarednscli.configs import cfg

parser = argparse.ArgumentParser()

parser.add_argument("-c",
                    "--config",
                    help="Config file",
                    type=str,
                    required=False,
                    default="default.ini")

parser.add_argument("which_module",
                    help="Module to load",
                    type=str,
                    choices=["insert", "update", "delete", "list"])

parser.add_argument("remains",
                    type=str,
                    nargs=argparse.REMAINDER,
                    help="Child opts")

config_parser = configparser.ConfigParser()


def main():
    args = parser.parse_args()
    config_parser.read(args.config)
    for section in config_parser.sections():
        cfg.email = config_parser[section]["email"]
        cfg.zone_id = config_parser[section]["zone_id"]
        cfg.access_token = config_parser[section]["access_token"]

    m = importlib.import_module(f"cloudflarednscli.cmd.{args.which_module}")
    m.run(args)