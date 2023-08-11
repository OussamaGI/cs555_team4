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

### US12 --- Parents age check

def parentsAge(families, individuals):
    
    results= []
    father = True
    ### Checking for Father age difference
    for f in families:
        
        husb = next((individual for individual in individuals if individual.get('ID') == f.get('Husband ID')), None)
        
        if(husb .get('Age')< 0):
            
            print('US12: Husband ID '+ f.iloc[f]['Husband ID'] +' has invalid age')
            
            results.append('US12: Husband ID '+ f.iloc[f]['Husband ID'] +' has invalid age')
            
        elif(f.get('Children')!= 'NA'):
            
            for c in f.get('Children'):
                
                child = next((individual for individual in individuals if individual.get('ID') == c), None)
                
                if(0 < husb.get('Age') - child.get('Age') < 80):
                    father = True
                else:
                    father = False
                
            if father == False:
                print('US12: Father ' + f.iloc[f]['Husband ID'] + ' is 80 years older than his child or an invalid age')
                
                results.append('US12: Father ' + f.iloc[f]['Husband ID'] + ' is 80 years older than his child or an invalid age')
            else:
                print('US12: Father ' + f.iloc[f]['Husband ID'] + ' is 80 years younger than his childs')
                
                results.append('US12: Father ' + f.iloc[f]['Husband ID'] + ' is 80 years younger than his childs')
                
    
    mother = True    
    ### Checking for Mother age difference
    for f in families:
        
        mother = next((individual for individual in individuals if individual.get('ID') == f.get('Wife ID')), None)
        
        if(mother.get('Age')< 0):
            
            print('US12: Wife ID '+ families.iloc[f]['Wife ID'] +' has invalid age')
            
            results.append('US12: Wife ID '+ families.iloc[f]['Wife ID'] +' has invalid age')
        
        elif(f.get('Children') != 'NA'):
            
            for c in families.iloc[f]['Children']:
                
                child = next((individual for individual in individuals if individual.get('ID') == c), None)
                
                if(0 < mother.get('Age') - child.get('Age') < 60):
                    mother = True
                else:
                    mother = False
                
            if mother == False:
                print('US12: Mother ' + families.iloc[f]['Wife ID'] + ' is 60 years older than her child or an invalid age')
                
                results.append('US12: Mother ' + families.iloc[f]['Wife ID'] + ' is 60 years older than her child or an invalid age')
            else:
                print('US12: Mother ' + families.iloc[f]['Wife ID'] + ' is 80 years younger than her childs')
                
                results.append('US12: Mother ' + families.iloc[f]['Wife ID'] + ' is 80 years younger than her childs')
                
    return father, mother
            
            
### US16: All males of a family should have the same last name

def lastNameCheck(families, individuals):
    
    
    errors = []
    for f in families:
        
        lastName = []
        husband = next((individual for individual in individuals if individual.get('ID') == f.get('Husband ID')), None)
        husbandName = husband.get('Name').split(' ')[1]
        
        lastName.append(husbandName)
        
        if(f.get('Children') != 'NA'):
            
            for c in f.get('Children'):
                
                child = next((individual for individual in individuals if individual.get('ID') == c), None)
                
                if(child.get('Gender') == 'M'):
                    
                    lastName.append(child.get('Name').split(' ')[1])
                    
    
        if(len(set(lastName)) != 1):
            
            errors.append('US16: Error: Family ' + families.iloc[f]['ID'] +' does not have the same last name for males')
            
            return False
        else:
            errors.append('US16: Error: Family ' + families.iloc[f]['ID'] +' does have the same last name for males')
            
            return True