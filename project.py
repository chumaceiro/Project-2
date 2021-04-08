

import csv


def reader():
    csv_fd = open("sales_records.csv", 'r')
    csv_reader = csv.reader(csv_fd)
    return csv_reader



def compute_profit():
    csv_reader = reader()
    
    for row in range(1, len(csv_reader)):
        total_profit = float(row[8]) - float(row[9])
        print(total_profit)

if __name__ == "__main__":
    compute_profit()
