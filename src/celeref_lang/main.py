import argparse
import time
import logging

from . import create_app
from .version import VERSION

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description='A versatile interpreter in python to execute programs written in JSON.'
)

parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)
parser.add_argument('file', metavar='JSON_FILE', type=str, nargs='?',
                    help='Input source file to run')
parser.add_argument('-s', '--search', dest='search', type=str, nargs='?', default='',
                    help='Search list of available functions to call')


def show_functions(query: list):
    from .functions import public_functions
    for key in sorted(public_functions.keys()):
        if not query or query in key:
            print('----- [%s] -----' % key)
            doc = public_functions[key].__doc__
            doc = '\n'.join([s.strip() for s in doc.split('\n')])
            print(doc.strip())
            print('')
    exit(0)


def main():
    args = parser.parse_args()
    logger.debug(args)

    if args.search != '':
        show_functions(args.search)

    if args.file is not None:
        app = create_app(args.file)
        print('-' * 10)
        start_time = time.time()
        app.execute()
        print('\n------ %0.3f seconds ------' % (time.time() - start_time))
    else:
        parser.print_help()
