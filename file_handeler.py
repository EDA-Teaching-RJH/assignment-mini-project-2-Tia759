import csv 
def save_result(): 
    file = open("results.csv","a","newline=")
    writer = csv.writer(file)
