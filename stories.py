### gedcom libraryß

import datetime
from datetime import date
from datetime import timedelta
import data as data

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
            
            
            
### US38 --- List of upcoming birthdays

def upcomingBirthdays(individuals):
    
     
    today = date.today()
    listBirthdays = []
    birthday = {}
    for ind in individuals:
        
        if (ind.get('Alive') == 'True' and ind.get('Birthday') != 'NA'):
            
            if (today <= datetime.strptime(ind.get('Birthday'), '%Y-%m-%d').date().replace(year=today.year) <= (today+timedelta(days=30))):
                
                birthday['Name'] = ind.get('Name')
                birthday['Birthday'] = datetime.strptime(ind.get('Birthday'), '%Y-%m-%d').date().replace(year=today.year)
                
                listBirthdays.append(birthday)
    return listBirthdays

### US39  --- List of upcoming marriage anniversaries

def marriageAnniversaries(families, individuals):
    
    today = datetime.today()
    anniversaries = []
    familyAnniv = {}
    
    for fam in families:
        
        husb = next((individual for individual in individuals if individual.get('ID') == fam.get('Husband ID')), None)
        wife = next((individual for individual in individuals if individual.get('ID') == fam.get('Wife ID')), None)
        divorced = fam.get('Divorced')
        
        if(husb.get('Alive') == True and wife.get('Alive') == True and divorced == 'NA'):
            
            if (today <= datetime.strptime(fam.get('Married'), '%Y-%m-%d').date().replace(year=today.year) <= (today+timedelta(days=30))):
                
                familyAnniv = {'Husband': husb.get('Name'),
                          'Wife': wife.get('Name'),
                          'Marriage Anniversary': (fam.get('Married')).date().replace(year = today.year)}
                
                anniversaries.append(familyAnniv)

            
    return anniversaries