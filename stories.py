### gedcom libraryß

import datetime
from datetime import date
from datetime import timedelta
import cs555_team4.data as data

# import Pandas as pd


import warnings
warnings.filterwarnings("ignore")


def getSiblings(families, individuals):
    
    noChildren = 0
    siblings = [item for sublist in families["Children"] for item in sublist]
    
    for family in families:
        children = family.get('Children')
        if children != {} and children != 'NA':
            for child in children:
                sibling = next((individual for individual in individuals if individual["ID"] == child), None)
                if sibling is not None:
                    siblings = siblings.append(sibling)
            
    
    orderedSiblings = siblings.sort_values(['Birthday'],ascending=True)            
    print(orderedSiblings)            
    # orderedSiblings = tabulate(orderedSiblings, headers='keys', tablefmt='psql')
    
    return orderedSiblings
    

def getDeceased(individuals):
    
    deceased = [individual for individual in individuals if individual.get('Alive') == True]
    
    return deceased
            