import csv 

  

def reading_results():
    with open ("results.csv","r") as file:
        csvreader = csv.reader (file)

        for row in csvreader: 
            print (row)

def appending_results(data_row, csv_filename = "results.csv"):
    try:
        with open (csv_filename, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerrow(data_row)
    except FileNotFoundError:
        print (f"File {csv_filename} not found")
    except csv.Error as e:
        print (f"An error occured whilst appending to {csv_filename}:{e}") 

