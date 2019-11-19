from csv import DictReader,DictWriter

def cm_to_in(cm):
	return round(float(cm) * 0.393701,2)

with open("Datasets/fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("Datasets/inches_fighters.csv", "w") as file:
	headers = ("Name", "Country", "Height")
	csv_writer = DictWriter(file, fieldnames = headers, lineterminator='\n')
	csv_writer.writeheader()
	for fighter in fighters:
		csv_writer.writerow({
			"Name": fighter["Name"],
			"Country": fighter["Country"],
			"Height": cm_to_in(fighter["Height (in cm)"])
			})