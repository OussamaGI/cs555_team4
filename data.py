### families


familiesWithChildren = [

    {
        'id': '@F1@',
        'Married': '1980-01-02',
        'Divorced': 'NA',
        'HusbandId': '@I1@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I2@',
        'WifeName': 'Gina /Koi/',
        'Children': {'@I3@', '@I4@'}
    },
    
    {
        'id': '@F2@',
        'Married': '1990-01-02',
        'Divorced': 'NA',
        'HusbandId': '@I5@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I6@',
        'WifeName': 'Gina /Koi/',
        'Children': {'@I7@', '@I8@'}
    }
]
    
familiesWithoutChildren = [
    
    {
        'id': '@F3@',
        'Married': '2010-01-02',
        'Divorced': 'NA',
        'HusbandId': '@I7@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I8@',
        'WifeName': 'Gina /Koi/',
        'Children': {}
    },
    
    {
        'id': '@F4@',
        'Married': '02 JAN 2010',
        'Divorced': 'NA',
        'HusbandId': '@I7@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I8@',
        'WifeName': 'Gina /Koi/',
        'Children': {}
    },
    
    
]

families = [
    
    {
        'id': '@F3@',
        'Married': '2010-01-02',
        'Divorced': 'NA',
        'HusbandId': '@I7@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I8@',
        'WifeName': 'Gina /Koi/',
        'Children': {}
    },
    
    {
        'id': '@F4@',
        'Married': '02 JAN 2010',
        'Divorced': 'NA',
        'HusbandId': '@I7@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I8@',
        'WifeName': 'Gina /Koi/',
        'Children': {}
    },
    
    {
        'id': '@F5@',
        'Married': '02 JAN 2010',
        'Divorced': 'NA',
        'HusbandId': '@I9@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I10@',
        'WifeName': 'Gina /Koi/',
        'Children': {}
    },
    
    {
        'id': '@F5@',
        'Married': '02 JAN 2010',
        'Divorced': 'NA',
        'HusbandId': '@I9@',
        'HusbandName': 'Irwin /Trout/',
        'WifeId': '@I10@',
        'WifeName': 'Gina /Koi/',
        'Children': {}
    }
]



### List of individuals

individuals = [
    
    {
        'ID': '@I1@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-12',
        'Age': '30',
        'Alive': False,
        'Death': '1970-01-15',
        'Child': '@F1@',
        'Spouse': '@F1@'
    },
    {
        'ID': '@I2@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-05',
        'Age': '48',
        'Alive': False,
        'Death': 'NA',
        'Child': '@F1@',
        'Spouse': '@F1@'
    },
    {
        'ID': '@I5@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-14',
        'Age': '83',
        'Alive': True,
        'Death': 'NA',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    {
        'ID': '@I6@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-04',
        'Age': '65',
        'Alive': False,
        'Death': '2015-03-14',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    {
        'ID': '@I7@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-14',
        'Age': '83',
        'Alive': True,
        'Death': 'NA',
        'Child': '',
        'Spouse': '@F3@'
    },
    {
        'ID': '@I8@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-04',
        'Age': '65',
        'Alive': False,
        'Death': '2010-01-02',
        'Child': '',
        'Spouse': '@F3@'
    },
    {
        'ID': '@I9@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-14',
        'Age': '83',
        'Alive': False,
        'Death': '2000-12-04',
        'Child': '',
        'Spouse': '@F5@'
    },
    {
        'ID': '@I10@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-04',
        'Age': '65',
        'Alive': False,
        'Death': '2003-06-08',
        'Child': '',
        'Spouse': '@F5@'
    }
    
]

siblings = [
    
    {
        'ID': '@I1@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-12',
        'Age': '30',
        'Alive': False,
        'Death': '1970-01-15',
        'Child': '@F1@',
        'Spouse': '@F1@'
    },
    
    {
        'ID': '@I5@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-14',
        'Age': '83',
        'Alive': True,
        'Death': 'NA',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    
    {
        'ID': '@I6@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-04',
        'Age': '65',
        'Alive': False,
        'Death': '2015-03-14',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    
    {
        'ID': '@I2@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-05',
        'Age': '48',
        'Alive': False,
        'Death': 'NA',
        'Child': '@F1@',
        'Spouse': '@F1@'
    }
    
]

noSiblings = []

listDeceased = [
    {
        'ID': '@I1@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-12',
        'Age': '30',
        'Alive': False,
        'Death': '1970-01-15',
        'Child': '@F1@',
        'Spouse': '@F1@'
    },
    {
        'ID': '@I2@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-05',
        'Age': '48',
        'Alive': False,
        'Death': 'NA',
        'Child': '@F1@',
        'Spouse': '@F1@'
    },
    
    {
        'ID': '@I6@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-04',
        'Age': '65',
        'Alive': False,
        'Death': '2015-03-14',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    {
        'ID': '@I5@',
        'Name': 'Irwin /Trout/',
        'Gender': 'M',
        'Birthday': '1940-12-14',
        'Age': '83',
        'Alive': True,
        'Death': 'NA',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    
    {
        'ID': '@I6@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-04',
        'Age': '65',
        'Alive': False,
        'Death': '2015-03-14',
        'Child': '@F2@',
        'Spouse': '@F2@'
    },
    
    {
        'ID': '@I2@',
        'Name': 'Carmen /Trout/',
        'Gender': 'F',
        'Birthday': '1955-03-05',
        'Age': '48',
        'Alive': False,
        'Death': 'NA',
        'Child': '@F1@',
        'Spouse': '@F1@'
    }
]

noDeceased = []