from neo4j.v1 import GraphDatabase
import json
import requests
import sys

class Neo4jConnection(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def get_anatomical_nodes(self):
        with self._driver.session() as session:
            return session.write_transaction(self._get_anatomical_nodes)

    @staticmethod
    def _get_anatomical_nodes(tx):
        result = tx.run("MATCH (n:anatomical_entity) RETURN n.name LIMIT 5")
        return [record["n.name"] for record in result]


class QueryBioLink:
    TIMEOUT_SEC = 120
    API_BASE_URL = 'https://api.monarchinitiative.org/api/bioentity'
    HANDLER_MAP = {
        'get_bioentity': 'anatomy/{bioentity_id}'
    }

    @staticmethod
    def __access_api(handler):

        url = QueryBioLink.API_BASE_URL + '/' + handler

        try:
            res = requests.get(url, timeout=QueryBioLink.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            print(url, file=sys.stderr)
            print('Timeout in QueryBioLink for URL: ' + url, file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            print(url, file=sys.stderr)
            print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None

        return res.json()

    @staticmethod
    def get_bioentity(bioentity_id):
        handler = QueryBioLink.HANDLER_MAP['get_bioentity'].format(bioentity_id=bioentity_id)
        results = QueryBioLink.__access_api(handler)
        result_str = 'UNKNOWN'
        if results is not None:
            result_str = results
        return result_str


if __name__ == '__main__':

    f = open('user_pass.json', 'r')
    userData = f.read()
    f.close()
    user = json.loads(userData)

    conn = Neo4jConnection("bolt://localhost:7687", user['username'], user['password'])
    nodes = conn.get_anatomical_nodes()
    print(nodes)

    for node in nodes:
        print(QueryBioLink.get_bioentity(node))

    conn.close()
