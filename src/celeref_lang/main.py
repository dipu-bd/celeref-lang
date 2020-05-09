import argparse
import time

from . import create_app
from .version import VERSION

parser = argparse.ArgumentParser(
    description='A versatile interpreter in python to execute programs written in JSON.'
)

parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)
parser.add_argument('file', metavar='JSON_FILE', type=str, nargs=1,
                    help='Input source file to run')


def main():
    args = parser.parse_args()
    app = create_app(args.file[0])
    print('-' * 10)
    start_time = time.time()
    app.execute()
    print('\n------ %0.3f seconds ------' % (time.time() - start_time))
