
''' This module defines the class GenerateMetabolitesTSV. GenerateMetabolitesTSV class is designed
to generate the metabolites.tsv file.

The format of the metabolites.tsv looks like the following:

metabolite  KEGG:C00022 Pyruvate    generic

'''


__author__ = 'Deqing Qu'
__copyright__ = 'Oregon State University'
__credits__ = ['Deqing Qu', 'Stephen Ramsey']
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = ''
__email__ = ''
__status__ = 'Prototype'


import requests


class GenerateMetabolitesTSV:

    @staticmethod
    def generate_metabolites_tsv():
        r = requests.get('http://rest.kegg.jp/list/compound')
        filename = 'metabolites.tsv'
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(1024):
                fd.write(chunk)

if __name__ == '__main__':
    GenerateMetabolitesTSV.generate_metabolites_tsv()