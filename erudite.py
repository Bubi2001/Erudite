import time
import random
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description='Script to generate Custom ILA parameters, set ILA to start working, read data and process it to wave format.', \
                                epilog='', add_help=True, exit_on_error=True)

parser.add_argument('-t', '--time-limit', action='store', dest='time limit', type=int, help='Optional, time limit per question in seconds.')
parser.add_argument('-l', '--log-results', action='store_true', help='Save results in a separate file.')
parser.add_argument('-q', '--question-amount', action='store', dest='question amount', type=int, help='Required, number of questions to ask.', required=True)
parser.add_argument('-v', '--version', action='version', version='%(prog)s version: v0.1')

arguments = parser.parse_args()

cli_args = vars(arguments)

if (cli_args['time limit']):
    time_lim = cli_args['time limit']
else:
    time_lim = None