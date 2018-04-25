''' This module defines the class UpdateNodesInfo. UpdateNodesInfo class is designed
to retrieve the node properties and update the properties on the Graphic model object.
The available methods include:

    update_anatomy_nodes : retrieve data from BioLink and update all anatomy nodes
    update_phenotype_nodes : retrieve data from BioLink and update all phenotype nodes
    update_microRNA_nodes : retrieve data from MyGene and update all microRNA nodes
    update_pathway_nodes : retrieve data from Reactome and update all pathway nodes
    update_protein_nodes : retrieve data from MyGene and update all protein nodes
    update_disease_nodes : retrieve data from BioLink and update all disease nodes

Example of method name used from other packages.
    example of get_nodes_mtd_name : get_anatomy_nodes
    example of get_entity_mtd_name : get_anatomy_entity
    example of update_nodes_mtd_name : update_anatomy_nodes

How to run this module
        $ cd [git repo]/code/reasoningtool/kg-construction
        $ python3 UpdateNodesInfo.py
'''

# BEGIN config.json format
# {
#   "url":"bolt://localhost:7687"
#   "username":"xxx",
#   "password":"xxx"
# }
# END config.json format

__author__ = 'Deqing Qu'
__copyright__ = 'Oregon State University'
__credits__ = ['Deqing Qu', 'Stephen Ramsey']
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = ''
__email__ = ''
__status__ = 'Prototype'

from Neo4jConnection import Neo4jConnection
import json
from QueryEBIOLSExtended import QueryEBIOLSExtended
from QueryOMIM import QueryOMIM

class UpdateNodesInfo:

    GET_QUERY_CLASS = {
        'anatomy': 'QueryBioLinkExtended',
        'phenotype': 'QueryBioLinkExtended',
        'microRNA': 'QueryMyGeneExtended',
        'pathway': 'QueryReactomeExtended',
        'protein': 'QueryMyGeneExtended',
        'disease': 'QueryBioLinkExtended',
        'chemical_substance': 'QueryMyChem',
        'bio_process': 'QueryBioLinkExtended'
    }

    @staticmethod
    def __update_nodes(node_type):

        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        get_nodes_mtd_name = "get_" + node_type + "_nodes"
        get_nodes_mtd = getattr(conn, get_nodes_mtd_name)
        nodes = get_nodes_mtd()
        print(len(nodes))

        from time import time
        t = time()

        nodes_array = []
        for i, node_id in enumerate(nodes):
            node = dict()
            node['node_id'] = node_id
            query_class_name = UpdateNodesInfo.GET_QUERY_CLASS[node_type]
            query_class = getattr(__import__(query_class_name), query_class_name)
            get_entity_mtd_name = "get_" + node_type + "_entity"
            get_entity_mtd = getattr(query_class, get_entity_mtd_name)
            node['extended_info_json'] = get_entity_mtd(node_id)
            nodes_array.append(node)
            print(node_type + " node No. %d : %s" % (i, node_id))

        print("api pulling time: %f" % (time() - t))

        nodes_nums = len(nodes_array)
        chunk_size = 10000
        group_nums = nodes_nums // chunk_size + 1
        for i in range(group_nums):
            start = i * chunk_size
            end = (i + 1) * chunk_size if (i + 1) * chunk_size < nodes_nums else nodes_nums
            update_nodes_mtd_name = "update_" + node_type + "_nodes"
            update_nodes_mtd = getattr(conn, update_nodes_mtd_name)
            update_nodes_mtd(nodes_array[start:end])

        print("total time: %f" % (time() - t))

        conn.close()

    @staticmethod
    def update_anatomy_nodes():
        UpdateNodesInfo.__update_nodes('anatomy')

    @staticmethod
    def update_phenotype_nodes():
        UpdateNodesInfo.__update_nodes('phenotype')

    @staticmethod
    def update_microRNA_nodes():
        UpdateNodesInfo.__update_nodes('microRNA')

    @staticmethod
    def update_pathway_nodes():
        UpdateNodesInfo.__update_nodes('pathway')

    @staticmethod
    def update_protein_nodes():
        UpdateNodesInfo.__update_nodes('protein')

    @staticmethod
    def update_disease_nodes():
        UpdateNodesInfo.__update_nodes('disease')

    @staticmethod
    def update_chemical_substance_nodes():
        UpdateNodesInfo.__update_nodes('chemical_substance')

    @staticmethod
    def update_bio_process_nodes():
        UpdateNodesInfo.__update_nodes('bio_process')

    @staticmethod
    def update_anatomy_nodes_desc():
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        rf = open("result_output.txt", 'a')

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_anatomy_nodes()
        print("anatomy: %d"%len(nodes), file=rf)

        from time import time
        t = time()

        nodes_array = []
        for i, node_id in enumerate(nodes):
            node = dict()
            node['node_id'] = node_id
            node['desc'] = QueryEBIOLSExtended.get_anatomy_description(node_id)
            nodes_array.append(node)

        print("anatomy api pulling time: %f" % (time() - t), file=rf)

        nodes_nums = len(nodes_array)
        chunk_size = 10000
        group_nums = nodes_nums // chunk_size + 1
        for i in range(group_nums):
            start = i * chunk_size
            end = (i + 1) * chunk_size if (i + 1) * chunk_size < nodes_nums else nodes_nums
            conn.update_anatomy_nodes_desc(nodes_array[start:end])

        print("total time: %f" % (time() - t), file=rf)

        conn.close()

    @staticmethod
    def update_phenotype_nodes_desc():
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        rf = open("result_output.txt", 'a')

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_phenotype_nodes()
        print("phenotype: %d"%len(nodes), file=rf)

        from time import time
        t = time()

        nodes_array = []
        for i, node_id in enumerate(nodes):
            node = dict()
            node['node_id'] = node_id
            node['desc'] = QueryEBIOLSExtended.get_phenotype_description(node_id)
            nodes_array.append(node)

        print("phenotype api pulling time: %f" % (time() - t), file=rf)

        nodes_nums = len(nodes_array)
        chunk_size = 10000
        group_nums = nodes_nums // chunk_size + 1
        for i in range(group_nums):
            start = i * chunk_size
            end = (i + 1) * chunk_size if (i + 1) * chunk_size < nodes_nums else nodes_nums
            conn.update_phenotype_nodes_desc(nodes_array[start:end])

        print("total time: %f" % (time() - t), file=rf)

        conn.close()

    @staticmethod
    def update_disease_nodes_desc():
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        rf = open("result_output.txt", 'a')

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_disease_nodes()
        print("disease: %d"%len(nodes), file=rf)

        from time import time
        t = time()

        nodes_array = []
        for i, node_id in enumerate(nodes):
            node = dict()
            node['node_id'] = node_id
            if node_id[:4] == "OMIM":
                node['desc'] = QueryOMIM().disease_mim_to_description(node_id)
            elif node_id[:4] == "DOID":
                node['desc'] = QueryEBIOLSExtended.get_disease_description(node_id)
            nodes_array.append(node)

        print("disease api pulling time: %f" % (time() - t), file=rf)

        nodes_nums = len(nodes_array)
        chunk_size = 10000
        group_nums = nodes_nums // chunk_size + 1
        for i in range(group_nums):
            start = i * chunk_size
            end = (i + 1) * chunk_size if (i + 1) * chunk_size < nodes_nums else nodes_nums
            conn.update_disease_nodes_desc(nodes_array[start:end])

        print("total time: %f" % (time() - t), file=rf)

        rf.close()

        conn.close()

    @staticmethod
    def update_bio_process_nodes_desc():
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        rf = open("result_output.txt", 'a')

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_bio_process_nodes()
        print("bio_process: %d"%len(nodes), file=rf)

        from time import time
        t = time()

        nodes_array = []
        for i, node_id in enumerate(nodes):
            node = dict()
            node['node_id'] = node_id
            node['desc'] = QueryEBIOLSExtended.get_bio_process_description(node_id)
            nodes_array.append(node)

        print("api pulling time: %f" % (time() - t), file=rf)

        nodes_nums = len(nodes_array)
        chunk_size = 10000
        group_nums = nodes_nums // chunk_size + 1
        for i in range(group_nums):
            start = i * chunk_size
            end = (i + 1) * chunk_size if (i + 1) * chunk_size < nodes_nums else nodes_nums
            conn.update_bio_process_nodes_desc(nodes_array[start:end])

        print("total time: %f" % (time() - t), file=rf)

        rf.close()

        conn.close()

if __name__ == '__main__':

    # UpdateNodesInfo.update_anatomy_nodes()
    # UpdateNodesInfo.update_phenotype_nodes()
    # UpdateNodesInfo.update_microRNA_nodes()
    # UpdateNodesInfo.update_pathway_nodes()
    # UpdateNodesInfo.update_protein_nodes()
    # UpdateNodesInfo.update_disease_nodes()
    # UpdateNodesInfo.update_chemical_substance_nodes()
    # UpdateNodesInfo.update_bio_process_nodes()
    UpdateNodesInfo.update_anatomy_nodes_desc()
    UpdateNodesInfo.update_phenotype_nodes_desc()
    UpdateNodesInfo.update_disease_nodes_desc()
    UpdateNodesInfo.update_bio_process_nodes_desc()

