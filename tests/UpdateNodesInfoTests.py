import unittest
import json
import random

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from Neo4jConnection import Neo4jConnection
from QueryBioLinkExtended import QueryBioLinkExtended
from QueryMyGeneExtended import QueryMyGeneExtended
from QueryReactomeExtended import QueryReactomeExtended
from QueryMyChem import QueryMyChem
from QueryEBIOLSExtended import QueryEBIOLSExtended

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


class UpdateNodesInfoTestCase(unittest.TestCase):

    def test_update_anatomy_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_anatomy_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from BioLink API
            node_id = nodes[i]
            extended_info_json_from_api = QueryBioLinkExtended.get_anatomy_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_anatomy_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

        conn.close()

    def test_update_phenotype_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_phenotype_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from BioLink API
            node_id = nodes[i]
            extended_info_json_from_api = QueryBioLinkExtended.get_phenotype_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_phenotype_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

        conn.close()

    def test_update_microRNA_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_microRNA_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from MyGene API
            node_id = nodes[i]
            extended_info_json_from_api = QueryMyGeneExtended.get_microRNA_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_microRNA_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(len(json.loads(extended_info_json_from_api)), len(json.loads(node['n']['extended_info_json'])))

        conn.close()

    def test_update_pathway_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_pathway_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from Reactome API
            node_id = nodes[i]
            extended_info_json_from_api = QueryReactomeExtended.get_pathway_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_pathway_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

        conn.close()

    def test_update_protein_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_protein_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve phenotype entities from MyGene API
            node_id = nodes[i]
            extended_info_json_from_api = QueryMyGeneExtended.get_protein_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_protein_node(node_id)
            self.maxDiff = None
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(len(json.loads(extended_info_json_from_api)), len(json.loads(node['n']['extended_info_json'])))

        conn.close()

    def test_update_disease_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_disease_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from BioLink API
            node_id = nodes[i]
            extended_info_json_from_api = QueryBioLinkExtended.get_disease_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_disease_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

        conn.close()

    def test_update_chemical_substance_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_chemical_substance_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from MyChem API
            node_id = nodes[i]
            extended_info_json_from_api = QueryMyChem.get_chemical_substance_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_chemical_substance_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

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
            # retrieve data from BioLink API
            node_id = nodes[i]
            extended_info_json_from_api = QueryBioLinkExtended.get_bio_process_entity(node_id)

            # retrieve data from Neo4j
            node = conn.get_bio_process_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['id'])
            self.maxDiff = None
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

        conn.close()

    def test_update_cellular_component_desc(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_cellular_component_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from BioLink API
            node_id = nodes[i]
            desc = QueryEBIOLSExtended.get_cellular_component_description(node_id)

            # retrieve data from Neo4j
            node = conn.get_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['description'])
            self.assertEqual(node_id, node['n']['id'])
            if node['n']['description'] != "UNKNOWN":
                self.assertEqual(desc, node['n']['description'])

        conn.close()

    def test_update_molecular_function_desc(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_molecular_function_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            # retrieve data from BioLink API
            node_id = nodes[i]
            desc = QueryEBIOLSExtended.get_molecular_function_description(node_id)

            # retrieve data from Neo4j
            node = conn.get_node(node_id)
            self.assertIsNotNone(node['n']['id'])
            self.assertIsNotNone(node['n']['description'])
            self.assertEqual(node_id, node['n']['id'])
            if node['n']['description'] != "UNKNOWN":
                self.assertEqual(desc, node['n']['description'])

        conn.close()

if __name__ == '__main__':
    unittest.main()


