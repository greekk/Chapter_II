import csv

def csv_reader(file_obj):
    """ Read a csv file """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2019-04-17.csv"
    try:
        with open(csv_path) as f_obj:
            csv_reader(f_obj)
    except IOError:
        print("File can't open!!")

