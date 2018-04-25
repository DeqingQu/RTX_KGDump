import unittest
import json
import random

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from Neo4jConnection import Neo4jConnection
from QueryEBIOLSExtended import QueryEBIOLSExtended
from QueryOMIMExtended import QueryOMIM


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


class UpdateNodesInfoDescTestCase(unittest.TestCase):

    def test_update_anatomy_nodes_desc(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_anatomy_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from API
            node_id = nodes[i]
            desc = QueryEBIOLSExtended.get_anatomy_description(node_id)

            # retrieve data from Neo4j
            node = conn.get_anatomy_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['description'])
            self.assertEqual(node_id, node['n']['id'])
            self.assertEqual(desc, node['n']['description'])

        conn.close()

    def test_update_phenotype_nodes_desc(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_phenotype_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from API
            node_id = nodes[i]
            desc = QueryEBIOLSExtended.get_phenotype_description(node_id)

            # retrieve data from Neo4j
            node = conn.get_phenotype_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['description'])
            self.assertEqual(node_id, node['n']['id'])
            self.assertEqual(desc, node['n']['description'])

        conn.close()

    def test_update_disease_nodes_desc(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_disease_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from API
            node_id = nodes[i]
            if node_id[:4] == "OMIM":
                desc = QueryOMIM().disease_mim_to_description(node_id)
            elif node_id[:4] == "DOID":
                desc = QueryEBIOLSExtended.get_disease_description(node_id)

            # retrieve data from Neo4j
            node = conn.get_disease_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['description'])
            self.assertEqual(node_id, node['n']['id'])
            self.assertEqual(desc, node['n']['description'])

        conn.close()

    def test_update_bio_process_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_bio_process_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from API
            node_id = nodes[i]
            desc = QueryEBIOLSExtended.get_anatomy_description(node_id)

            # retrieve data from Neo4j
            node = conn.get_bio_process_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['description'])
            self.assertEqual(node_id, node['n']['id'])
            self.assertEqual(desc, node['n']['description'])

        conn.close()

if __name__ == '__main__':
    unittest.main()


