from unittest import TestCase
import json

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from QueryEBIOLSExtended import QueryEBIOLSExtended as QEBIEx


def get_from_test_file(key):
    f = open('query_desc_test_data.json', 'r')
    test_data = f.read()
    try:
        test_data_dict = json.loads(test_data)
        f.close()
        return test_data_dict[key]
    except ValueError:
        f.close()
        return None


class QueryEBIOLSExtendedTestCase(TestCase):
    def test_get_anatomy_description(self):
        desc = QEBIEx.get_anatomy_description('UBERON:0004476')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('UBERON:0004476'))
        desc = QEBIEx.get_anatomy_description('CL:0000038')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('CL:0000038'))

    def test_get_phenotype_description(self):
        desc = QEBIEx.get_phenotype_description('GO:0042535')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('GO:0042535'))

    def test_get_bio_process_description(self):
        desc = QEBIEx.get_bio_process_description('HP:0011105')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('HP:0011105'))

    def test_get_cellular_component_description(self):
        desc = QEBIEx.get_cellular_component_description('GO:0005573')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('GO:0005573'))

    def test_get_molecular_function_description(self):
        desc = QEBIEx.get_molecular_function_description('GO:0004689')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('GO:0004689'))
