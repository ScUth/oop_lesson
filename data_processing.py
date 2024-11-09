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
        for item in self.table:
            if condition(item):
                filter_list.append(item)
        return filter_list
    
    def aggregate(self, aggregation_function, aggregation_key):
        value = []
        for item in self.table:
            value.append(float(item[aggregation_key]))
        return aggregation_function(value)
    
    def __str__(self):
        pass
    
tbdb = TableDB()

cities_table = Table('Cities.csv', cities)
countries_table = Table('Countries.csv', countries)
tbdb.insert(cities_table)
tbdb.insert(countries_table)

print("The average temperature of all the cities:")
avfa = cities_table.aggregate(lambda num : sum(num) / len(num), 'temperature')
print(avfa)

print('All the cities in Italy :')
ait = cities_table.filter(lambda ct : ct['country'] == 'Italy')
print([ct['city'] for ct in ait])

print('The average temperature of all the cities in Italy :')
avit = [float(tp['temperature']) for tp in ait]
print(sum(avit) / len(avit))

print('The max temperature of all the cities in Italy :')
print(max(avit))

print('The min temperature of all the cities in Italy :')
print(min(avit))

# - print the average temperature for all the cities in Sweden
print('The average temperature of all the cities in Sweden :')
asw = cities_table.filter(lambda ct : ct['country'] == 'Sweden')
tsw = [float(ct['temperature']) for ct in asw]
print(sum(tsw) / len(tsw))

# - print the max temperature for all the cities in Sweden
print('The max temperature for all the cities in Sweden :')
tsw = [float(ct['temperature']) for ct in asw]
print(max(tsw))
