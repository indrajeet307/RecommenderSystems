import csv

with open("A1Ratings.csv","r") as infile:
	reader = csv.reader(infile)
	for row in reader:
		row.split(",")
		print(row)
