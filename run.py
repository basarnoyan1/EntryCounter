#!/usr/bin/env python
from entrycounter import EntryCounter
from argparse import ArgumentParser

# make dict from args
parser = ArgumentParser(description="EntryCounter")
parser.add_argument('--config_path', dest='config_path', default="settings.ini", help='path to settings.ini')
args = parser.parse_args()

# start app
entrycounter = EntryCounter()
entrycounter.go_config(config_path=args.config_path)
