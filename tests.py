import stories
import unittest
import cs555_team4.data as data


class UserStoryTestCase(unittest.TestCase):
    
    def list_siblings(self):
        # Test case 1: Existence of siblings
        output = stories.getSiblings(data.familiesWithChildren, data.individuals)
        self.assertTrue(output.equals(data.siblings))
        
        # Test case 2: Inexistence of siblings
        outupt = stories.getSiblings(data.familiesWithoutChildren, data.individuals)
        self.assertFalse(output.equals(data.noSiblings))
        
    def list_deceased(self):
        
        output = stories.getDeceased(data.individuals)

        # Test case 1: Existence of deaths
        self.assertTrue(output.equals(data.listDeceased))
        
        # Test case 2: Inexistence of siblings
        self.assertFalse(output.equals(data.noDeceased))
        

if __name__ == '__main__':
    unittest.main()
