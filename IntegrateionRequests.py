import requests
import sys
import json


class mydict(dict):
    def __str__(self):
        return json.dumps(self)

class IntegrationRequests:
    TIMEOUT_SEC = 120

    @staticmethod
    def __get_api(handler, url_suffix):

        url = handler + url_suffix

        try:
            res = requests.get(url, timeout=IntegrationRequests.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            print(url, file=sys.stderr)
            print('Timeout in IntegrationRequests for URL: ' + url, file=sys.stderr)
            return None
        except BaseException as e:
            print(url, file=sys.stderr)
            print('%s received in IntegrationRequests for URL: %s' % (e, url), file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            print(url, file=sys.stderr)
            print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None
        return res.json()

    @staticmethod
    def __post_api(handler, url_suffix, payload):

        url = handler + url_suffix
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=UTF-8"
        }

        try:
            res = requests.post(url, data=json.dumps(payload), headers=headers, timeout=IntegrationRequests.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            print(url, file=sys.stderr)
            print('Timeout in IntegrationRequests for URL: ' + url, file=sys.stderr)
            return None
        except BaseException as e:
            print(url, file=sys.stderr)
            print('%s received in IntegrationRequests for URL: %s' % (e, url), file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            print(url, file=sys.stderr)
            print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None
        return res.json()

    @staticmethod
    def Query_Xray():

        #   get request
        url = "http://rtx.ncats.io/api/rtx/v1/"
        url_suffix = "result/2"
        response = IntegrationRequests.__get_api(url, url_suffix)
        print(response)

        #   post request
        url_suffix = "query"
        payload = {
            "bypass_cache": "false",
            "known_query_type_id": "Q3",
            "max_results": 100,
            "original_question": "What proteins does IBUPROFEN target?",
            "restated_question": "What proteins are the target of IBUPROFEN",
            "terms": {
                "chemical_substance": "CHEMBL521",
                "rel_type": "directly_interacts_with",
                "target_label": "protein"
            }
        }
        response = IntegrationRequests.__post_api(url, url_suffix, payload)
        print(mydict(response))

        #   post request from ROBOKOP
        url = "http://robokop.renci.org:6011/api/query"
        url_suffix = ""
        payload = {
            "bypass_cache": "true",
            "known_query_type_id": "Q3",
            "terms": {
                "chemical_substance": "CHEMBL:CHEMBL521"
            },
            "max_results": 100,
            "original_question": "What proteins does IBUPROFEN target?",
            "restated_question": "What proteins are the target of IBUPROFEN"
        }
        response = IntegrationRequests.__post_api(url, url_suffix, payload)
        print(mydict(response))


if __name__ == '__main__':
    IntegrationRequests.Query_Xray()
