from pprint import pprint
from client.helpers.requests import get_request, get_results
from server.app import app
import sys
import yaml

customers_results = []
merchants_results = []
orders_results = []
transactions_results = []

def main():
    app.run(host='localhost', port=3000)

if __name__ == '__main__':
    sys.exit(main())