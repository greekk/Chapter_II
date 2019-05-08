import csv

def csv_writer(data, path):
    """ Write data to a csv-file """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport". split(","),
            "Jules,Dicki,Nicolasville".split(","),
            "Dedrick,Medhurst,Stiedemannberg".split(",")]
    path = "output.csv"
    csv_writer(data,path)

