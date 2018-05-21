
''' This module defines the class QueryBioLinkExtended. QueryBioLinkExtended class is designed
to communicate with Monarch APIs and their corresponding data sources. The
available methods include:
    * query anatomy entity by ID
'''


__author__ = 'Deqing Qu'
__copyright__ = 'Oregon State University'
__credits__ = ['Deqing Qu', 'Stephen Ramsey']
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = ''
__email__ = ''
__status__ = 'Prototype'

import xmltodict
import json


class QueryHMDB:
    @staticmethod
    def get_metabolite_desc(names):
        results = dict()
        with open('csf_metabolites.xml') as fd:
            doc = xmltodict.parse(fd.read())
            for name in names:
                notFound = True
                for metabolite in doc['hmdb']['metabolite']:
                    if metabolite['name'] == name:
                        results[name] = metabolite['description']
                        notFound = False
                if notFound:
                    results[name] = None

        return results


if __name__ == '__main__':

    def save_to_test_file(key, value):
        f = open('tests/query_desc_test_data.json', 'r+')
        try:
            json_data = json.load(f)
        except ValueError:
            json_data = {}
        f.seek(0)
        f.truncate()
        json_data[key] = value
        json.dump(json_data, f)
        f.close()

    print(QueryHMDB.get_metabolite_desc(["1-Methylhistidine", "Deoxyuridine"]))

    # print(QueryEBIOLSExtended.get_disease_description('OMIM:613573'))
