import unittest
from UpdateNodesInfoTests import UpdateNodesInfoTestCase
from tests.Neo4jConnectionTests import Neo4jConnectionTestCase
from tests.QueryBioLinkExtendedTests import QueryBioLinkExtendedTestCase
from tests.QueryMyChemTests import QueryMyChemTestCase
from tests.QueryMyGeneExtendedTests import QueryMyGeneExtendedTestCase
from tests.QueryReactomeExtendedTests import QueryReactomeExtendedTestCase


class UpdateModuleTestSuite(unittest.TestSuite):
    def suite(self):
        suite = unittest.TestSuite()

        suite.addTest(UpdateNodesInfoTestCase())
        suite.addTest(Neo4jConnectionTestCase())
        suite.addTest(QueryBioLinkExtendedTestCase())
        suite.addTest(QueryMyChemTestCase())
        suite.addTest(QueryMyGeneExtendedTestCase())
        suite.addTest(QueryReactomeExtendedTestCase())

        return suite


if __name__ == '__main__':
    unittest.main()