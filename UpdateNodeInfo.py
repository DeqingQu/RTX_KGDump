from neo4j.v1 import GraphDatabase
import json

class Neo4jConnection(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_anatomical_node_count(self):
        with self._driver.session() as session:
            print(session.write_transaction(self._get_anatomical_node_count))

    def get_anatomical_node(self):
        with self._driver.session() as session:
            return session.write_transaction(self._get_anatomical_node)

    @staticmethod
    def _get_anatomical_node_count(tx):
        result = tx.run("MATCH (n:anatomical_entity) RETURN count(n)")
        return result.single()[0]

    @staticmethod
    def _get_anatomical_node(tx):
        result = tx.run("MATCH (n:anatomical_entity) RETURN n LIMIT 25")
        return result.single()[0]

if __name__ == '__main__':

    f = open('user_pass.json', 'r')
    userData = f.read()
    f.close()
    user = json.loads(userData)

    obj = Neo4jConnection("bolt://localhost:7687", user['username'], user['password'])
    obj.print_anatomical_node_count()
    # print(obj.get_anatomical_node())
    obj.close()
