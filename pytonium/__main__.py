"""
Module entrypoint. Ran with `python -m pytonium
"""

from argparse import ArgumentParser
from . import main

parser = ArgumentParser(description="Run UI tests")

parser.add_argument('-F', '--config-file', type=str, default=None, help='Name of json file containing configuration as key/value pairs')
parser.add_argument('-J', '--config-json', type=str, default=None, help='Inline json of arguments, overrides --config-file; can\'t be used '
                                                                        'with --config-args e.g. \'{"foo": "bar", "baz": "quix"')
parser.add_argument('-C', '--config-args', default='', help='Comma-delimited list of config arguments to override; can\'t be used with --config--json, e.g. foo=bar,baz=quix')
parser.add_argument('-p', '--pattern', type=str, help='Pattern to match tests', default='test*.py')
parser.add_argument('-s', '--start-directory', type=str, help='Directory to start discovery', default='.')

args = parser.parse_args()



main(pattern=args.pattern, config=args.config, start_directory=args.start_directory, config_file=args.config_file)
main('hello')