import csv 

  

def reading_results():
    with open ("results.csv","r") as file:
        csvreader = csv.reader (file)

        for row in csvreader: 
            print (row)

