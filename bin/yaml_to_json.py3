#!/usr/bin/env python3
import sys
import json

import yaml
#try:
#    from yaml import CLoader as Loader, CDumper as Dumper
#except ImportError:
#    from yaml import Loader, Dumper

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
#yaml_file = parser.parse_args().input_file

yaml_file = sys.stdin

print(json.dumps(
	yaml.load(yaml_file, Loader=yaml.SafeLoader),
	separators=(',', ':'), ensure_ascii=False,
))
#		check_circular=False,
#		cls=None,
#		indent=None,
#		encoding="utf-8",
#		default=None,
#		sort_keys=False

