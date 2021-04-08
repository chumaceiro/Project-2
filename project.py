import csv


# def reader():
#     csv_fd = open("testing.csv", 'r')
#     csv_reader = csv.reader(csv_fd)
#     return csv_reader

# def dictreader():
#     csv_fd = open("testing.csv", 'r')
#     csv_reader = csv.DictReader(csv_fd)
#     return csv_reader


# def compute_profit():
#     x = open('tesing.csv')
#     f = x.readlines()
#     a = []
#     for i in f:
#         a.append(i.split(',')) 

#     b = a[1:]
#     for i in b:
#         c.append((float(i[8])-float(i[9])))

#     d = 0
#     with open('testing.csv', 'r') as c:
#         reader = csv.reader(c)
#         extended_rows = []
#         for row in reader:
#             row.append(str(c[d]))
#             extended_rows.append(row)
#             d += 1
#         with open('extended.csv', 'a') as e:
#             writer = csv.writer(e)
#             writer.writerows(extended_rows)
    


# def get_unique_country_per_region(region):
#     csv_dreader = dictreader()
#     country_list = {}
#     for row in csv_dreader:
#         temp_row = []
#         if row['region'] == region:
#             temp_row.append(row['region'])

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
    return result

def item_shipped_within(days):
    pass

def item_type_unit_sold():
    with open("sales_records.csv", 'r') as reader:
        csv_reader = csv.reader(reader)
        temp_dic = {}
        for row in csv_reader:
            temp_dic[row[2]] = int(row[7])
        
        return temp_dic


                
            

if __name__ == "__main__":
    print(count_unique_item_types())
    print(item_type_unit_sold())
