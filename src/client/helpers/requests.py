import requests

session = requests.Session()

def check_response_status(response):
    if not str(response.status_code).startswith('2'):
        raise Exception(f'ApiError(status_code={response.status_code}, response={response.text})')

def get_request(url, **args):
    response = None

    while True:
        try:
            response = requests.get(url=url, **args)

            check_response_status(response)

            break
        except Exception as e:
            print(e)

    if response.content:
        return response.json()

    return None

def get_results(url):
    results = []
    curr_page = url

    while curr_page is not None:
        try:
            response = session.get(curr_page)
            check_response_status(response)

            response_json = response.json()
            results.extend(response_json["results"])
            print(f'{len(results)}/{response_json["count"]}', curr_page)

            curr_page = response_json["next"]

        except Exception as e:
            print(e)

        if curr_page is None:
            break

    return results