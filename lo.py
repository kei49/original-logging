import logging
import sys
import argparse
import os
from datetime import date

#parser = argparse.ArgumentParser(description='add log')
#parser.add_argument('-m', required=True, help='Content of logs(memos)')
#args = parser.parse_args()

def lo():
    month = date.today().strftime('%Y%m')
    home_dir = os.path.expanduser('~')
    filename = home_dir + '/.log/life/' + month + '.log'
    logging.basicConfig(filename=filename, format='%(asctime)s %(message)s', level=logging.INFO)
    message = ' '.join(sys.argv[1:])
    logging.info(message)
    
if __name__ == '__main__':
    lo()
