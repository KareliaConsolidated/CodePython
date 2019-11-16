# Writing CSV Files Using Lists
# writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV
#========================================================================#
# from csv import writer
# with open("Datasets/cats.csv", "w") as file:
# 	csv_writer = writer(file)
# 	csv_writer.writerow(["Name", "Age"])
# 	csv_writer.writerow(["Ryu", 2])
# 	csv_writer.writerow(["Blue", 4])
#========================================================================#
from csv import writer, reader
with open('Datasets/fighters.csv') as file:
	csv_reader = reader(file)
	fighters = [[s.upper() for s in row] for row in csv_reader]
	for row in fighters:
		print(row)

with open('Datasets/screaming_fighters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)

#========================================================================#