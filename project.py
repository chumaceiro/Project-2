import csv
from datetime import datetime


    #find a way to append to each individual row in file
#rewrite whole file he says
def compute_profit():
    csv_fd = open("sales_records_2.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    for row in csv_reader:
        x = float(row['total_revenue']) - float(row['total_cost']) #nichole
        row['total_profit'] = str(x)
        #csv.DictWriter.writerow(
        
    #csv_id = open("sales_records_2.csv", 'w')
    #csv_writer = csv.DictWriter()


def count_unique_item_types():
    unique_items = 0
    with open("sales_records.csv", 'r') as reader:
        csv_reader = csv.reader(reader)
        temp_list = []
        for row in csv_reader:
            temp_list.append(row[2])
    temp_list.remove('item_type')
    unique_items = set(temp_list)
    result = len(unique_items)
    reader.close()
    return result

def item_shipped_within(days):
    pass

def item_type_unit_sold():
    with open("sales_records.csv", 'r') as reader:
        csv_reader = csv.reader(reader)
        temp_dic = {}
        for row in csv_reader:
            temp_dic[row[2]] = int(row[7])
    reader.close()    
    return temp_dic

    #change file name
def get_unique_country_per_region(regions):
    number_dict = {}
    country_dict = {}
    for i in regions:
        number_dict.update({i:0})
        country_dict.update({i:[]})
    csv_fd = open("sales_records_2.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    for row in csv_reader:
        number_dict[row['region']]+=1
        country_dict[row['region']].append(row['country'])
    csv_fd.close()
    return f'{number_dict} and {country_dict}'
    
    #change file name
def get_regions():
    csv_fd = open("sales_records_2.csv", 'r')
    csv_reader = csv.reader(csv_fd)
    x = csv_fd.readlines()[1:]
    regions = []
    csv_fd.close()
    for i in x:
        regions.append(i[0:i.index(',')])
    return set(regions)

def profit_by_country(country):
    pass

def priority_by_region(region):
    csv_fd = open("sales_records_2.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    priority_dict = {'L':0,'M':0,'H':0}
    for row in csv_reader:
        if row['region'] == region:
            priority_dict[row['order_priority']]+=1
    csv_fd.close()
    return priority_dict

def item_type_unit_sold():
    csv_fd = open("sales_records_2.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    item_dict = {}
    x = get_item_types()
    for i in x:
        item_dict.update({i:0})
    for row in csv_reader:
        item_dict[row['item_type']]+=1
    csv.close()
    return item_dict
    
def get_item_types():
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    x = []
    for row in csv_reader:
        x.append(row['item_type'])
    csv_fd.close()
    return set(x)

def item_shipped_within(days):
    csv_fd = open("sales_records_2.csv", 'r')
    order_id_list = []
    dates = []
    csv_reader = csv.DictReader(csv_fd)
    order_id_list = []
    for row in csv_reader:
        if calculate_days(row['ship_date'],row['order_date']) < days:
            order_id_list.append(row['order_id'])
    no_of_orders = len(order_id_list)
    return f'{order_id_list} and {no_of_orders}'
            
        
#USE DATETIME CLASS
def calculate_days(date_1,date_2):
    start_date = datetime.strptime(date_1, "%m/%d/%Y")
    end_date = datetime.strptime(date_2, "%m/%d/%Y")
    return abs((end_date-start_date).days)

        
#TODO: CHANGE CSV.CLOSE() to x .close()   
        
def country_revenue_item_type(country):
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    country_revenue = {}
    x = list(get_item_types())
    items = {}
    for i in country:
        country_revenue.update({i:{}})   
    for i in country_revenue:
        for k in x:
            country_revenue[i].update({k:0})
    
    for row in csv_reader:
        country_revenue[row['country']][row['item_type']]+=float(row['total_revenue'])
    
    
    
    print(country_revenue)
    
def get_countries():
    x = open("sales_records.csv", 'r')
    a = []
    csv_r = csv.DictReader(x)
    for row in csv_r:
        a.append(row['country'])
    return list(set(a))
    
        
   
 


            

if __name__ == "__main__":
    #print(count_unique_item_types())
    #print(item_type_unit_sold())
    #print(get_unique_country_per_region(get_regions()))
    #print(compute_profit())
    #print(priority_by_region('Europe'))
    #print(get_item_types())
    #print(item_type_unit_sold())
    #print(item_shipped_within(10))
    #print(get_item_types())
    country_revenue_item_type(get_countries())
    #print(get_countries())
    
