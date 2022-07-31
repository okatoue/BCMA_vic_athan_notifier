import tabula
import csv
import os

def new_times():

    # PDF from BCMA's website that includes all the athan of times for the current month
    athan_times = "https://www.thebcma.com/upload/PDF/Victoria/SalahTimes.pdf"

    # Converts PDF file into CSV file
    table = tabula.read_pdf(athan_times, pages=1, lattice = True)
    table[0].to_csv("athan.csv")

    # Extracts all the athan times from the previous CSV file into a new CSV file, the new file gets rid of all the unwanted rows
    with open("athan.csv", "r") as source:
        reader = csv.reader(source)

        with open("output.csv", "w") as result:
            writer = csv.writer(result)
            for r in reader:
                writer.writerow((r[1], r[3], r[5], r[7], r[9], r[11], r[13]))

    # Turns all needed value's into a list
    with open('output.csv') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)

        list_of_times = list(filter(lambda x: x, rows))

    # Deletes The CSV files
    os.remove("athan.csv")
    os.remove("output.csv")

    # Moves Jummah prayer time to the front of the list
    # This in turn makes the number of the day fit match the lists index

    list_of_times = list_of_times[-1:] + list_of_times[:-1]

    return list_of_times

