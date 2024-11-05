import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

###############################################################################
class TableDB:
    def __init__(self):
        self.table_database = []
        
    def insert(self, table):
        self.table_database.append(table)
        
    def search(self, table_name):
        for item in self.table_database:
            if item == table_name:
                return item
            return None
    
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table
        
    def filter(self, condition):
        filter_list = []
        for item in self.table_name:
            if condition(item):
                filter_list.append(item)
        return filter_list
    
    def aggregate(self, aggregation_function, aggregation_key):
        value = []
        for item in self.table_name:
            value.append(float(item[aggregation_key]))
        return aggregation_function(value)
    
    def __str__(self):
        pass