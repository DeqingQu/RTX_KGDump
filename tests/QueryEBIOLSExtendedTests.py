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


class QueryEBIOLSExtendedTestCases(TestCase):
    def test_get_anatomy_description(self):
        desc = QEBIEx.get_anatomy_description('UBERON:0004476')
        self.assertIsNotNone(desc)
        self.assertEqual(desc, get_from_test_file('UBERON:0004476'))