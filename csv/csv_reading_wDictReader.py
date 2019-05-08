import csv

""" Read data with DictReader"""
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj)
    for line in reader:
        print(line['first_name'], line['last_name'])

if __name__ ==  "__main__":
    try:
        with open("data.csv", "r") as file_obj:
            csv_dict_reader(file_obj)
    except IOError:
        print("Can't open the file!!")
