from neo4j.v1 import GraphDatabase

class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_node_count(self):
        with self._driver.session() as session:
            counter = session.write_transaction(self._get_node_count)
            print('nodes counter : %d' % counter)

    def print_relation_count(self):
        with self._driver.session() as session:
            counter = session.write_transaction(self._get_relation_count)
            print('relationships counter : %d' % counter)

    @staticmethod
    def _get_node_count(tx):
        result = tx.run("START n=node(*) RETURN count(n)")
        return result.single()[0]

    @staticmethod
    def _get_relation_count(tx):
        result = tx.run("START r=relationship(*) RETURN count(r)")
        return result.single()[0]

if __name__ == '__main__':
    obj = HelloWorldExample("bolt://localhost:7687", "neo4j", "88888888")
    obj.print_node_count()
    obj.print_relation_count()
    obj.close()