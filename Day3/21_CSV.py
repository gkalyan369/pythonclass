import csv

rows = ""
with open('Nifty_2016.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    rows = [next(data) for i in range(5)]
    print(type(data))
    for row in data:
        # print(','.join(row))
        print(row)


with open('Nifty_2017.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(5):
        data_writer.writerow(rows[i])




# Dict Writer
with open('names.csv', 'w', newline='') as csvfile:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

    writer.writeheader()
    writer.writerow({'first_name': 'Raju', 'last_name': 'Ramchandani'})
    writer.writerow({'first_name': 'Pallavi', 'last_name': 'K'})
    writer.writerow({'first_name': 'Vikram', 'last_name': 'Kamath'})


# Dict Reader
with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
