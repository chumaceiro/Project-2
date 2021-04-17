import csv
from datetime import datetime
import sys
import arrow

# Function 1:
def compute_profit():
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    list_ = []
    for row in csv_reader:
        x = float(row['total_revenue']) - float(row['total_cost']) #nichole
        row['total_profit'] = str(x)
        list_.append(row)
    

    csv_fd.close()
    csv_id = open("sales_records.csv", 'w')
    keys = list(list_[0].keys())
    csv_writer = csv.DictWriter(csv_id, fieldnames=keys)
    csv_writer.writeheader()
    csv_writer.writerows(list_)

# Function 2:
def get_unique_country_per_region(regions):
    number_dict = {}
    country_dict = {}
    for i in regions:
        number_dict.update({i:0})
        country_dict.update({i:[]})
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    for row in csv_reader:
        number_dict[row['region']]+=1
        country_dict[row['region']].append(row['country'])
    csv_fd.close()
    return f'{number_dict} and {country_dict}'

def get_regions():
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.reader(csv_fd)
    x = csv_fd.readlines()[1:]
    regions = []
    csv_fd.close()
    for i in x:
        regions.append(i[0:i.index(',')])
    return set(regions)


# Function 4:
def priority_by_region(region):
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    priority_dict = {'L':0,'M':0,'H':0}
    for row in csv_reader:
        if row['region'] == region:
            priority_dict[row['order_priority']]+=1
    csv_fd.close()
    return priority_dict

#Function 5:
def item_type_unit_sold():
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    item_dict = {}
    x = get_item_types()
    for i in x:
        item_dict.update({i:0})
    for row in csv_reader:
        item_dict[row['item_type']]+=1
    csv_fd.close()
    return item_dict

# Util:
def get_item_types():
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)
    x = []
    for row in csv_reader:
        x.append(row['item_type'])
    csv_fd.close()
    return set(x)

# Function 6:
def item_shipped_within(days):
    csv_fd = open("sales_records.csv", 'r')
    order_id_list = []
    dates = []
    csv_reader = csv.DictReader(csv_fd)
    order_id_list = []
    for row in csv_reader:
        if calculate_days(row['ship_date'],row['order_date']) < days:
            order_id_list.append(row['order_id'])
    no_of_orders = len(order_id_list)
    return f'{order_id_list} and {no_of_orders}'
                    
#UTIL 6
def calculate_days(date_1,date_2):
    start_date = datetime.strptime(date_1, "%m/%d/%Y")
    end_date = datetime.strptime(date_2, "%m/%d/%Y")
    return abs((end_date-start_date).days)

        
  
# Function 7:        
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
    
    return country_revenue

# UTIL 7:
def get_countries():
    x = open("sales_records.csv", 'r')
    a = []
    csv_r = csv.DictReader(x)
    for row in csv_r:
        a.append(row['country'])
    return list(set(a))
    
# Function 8:
def convert_date(date_):
    new_date_1=arrow.get(date_,'M/D/YYYY')
    return new_date_1

def profit_between_days(day_1, day_2):
    csv_fd=open('sales_records.csv','r')
    csv_reader=csv.DictReader(csv_fd)
    item_revenue_dict = {}
    day_1_conv = convert_date(day_1)
    day_2_conv = convert_date(day_2)
    for row in csv_reader:
        profit = row['total_profit']
        item_type = row['item_type']
        order_date = row['order_date']
        order_date_conv = convert_date(order_date) 
        if order_date_conv > day_1_conv and order_date_conv < day_2_conv:
            item_revenue_dict[item_type]=profit
    
    return item_revenue_dict

# Function 9:
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
   

def profit_by_country(country):
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.DictReader(csv_fd)

    profit_dict = {}
    for i in country:
        profit_dict.update({i:0})

    for row in csv_reader:
        for i in country:
            if row["country"] == i:
                profit_dict[i] += float(row["total_profit"])

    return profit_dict
 

def top_5_profitable_items():
    y = csv.DictReader(open("sales_records.csv", 'r'))
    a = {}
    for row in y:
        a.update({row['order_id']:float(row['total_profit'])})
    b = list(a.values())
    b.sort()
    b.reverse()
    c = b[:5]
    order_id_list = []
    for i in a:
        for j in c:
            if a[i] == j:
                order_id_list.append(i)
    return order_id_list
            
             

def get_unique_order_ids():
    x = open("sales_records.csv", 'r')
    csv_r = csv.DictReader(x)
    y = []
    for i in csv_r:
        y.append(i['order_id'])
    return list(set(y))
    

if __name__ == "__main__":
    # Function 1:
    compute_profit()

    #Function 2:
    print(get_unique_country_per_region(get_regions()))

    # Function 3:
    print(profit_by_country(get_countries()))

    #Function 4: 
    print(priority_by_region('Europe'))

    #Function 5:
    print(item_type_unit_sold())

    #Function 6:
    print(item_shipped_within(10))

    #Function 7:
    print(country_revenue_item_type(get_countries()))

    #Function 8:
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)
    print(profit_between_days('5/13/2015', '5/15/2015'))

    #Function 9: 
    print(count_unique_item_types())

    #Function 10:
    print(top_5_profitable_items())
