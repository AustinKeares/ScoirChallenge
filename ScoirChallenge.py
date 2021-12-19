#!/usr/bin/env python3
import csv
import os

def parseFileWithFilter(fileToBeParsed, userFilter, userFilterDetail):
	print()
	with open(fileToBeParsed, newline='') as file:
		reader = csv.reader(file, delimiter=' ')
		headers = str(', '.join(next(reader))).split(',')
		for row in reader:
			#if they decide to filter on dob, then check against birth year, if not, check against the names
			if (headers[int(userFilter)-1] == "dob"):
				if ', '.join(row).split(',')[int(userFilter)-1][:4] == userFilterDetail:
					print(', '.join(row))
			else:
				if ', '.join(row).split(',')[int(userFilter)-1] == userFilterDetail:
					print(', '.join(row))
	print()

#function for getting column to filter by and how to filter by that column
def getUserFilter(fileToBeParsed):
	userFilterOptions =  None

	#getting the headers from the csv file so user can select which hearder they want to filter by
	with open(fileToBeParsed, newline='') as file:
		reader = csv.reader(file, delimiter=' ')
		userFilterOptions = str(', '.join(next(reader))).split(',')

	counter = 0
	for filter in userFilterOptions:
		counter+=1
		print(f"{counter}: {filter}")

	userInputFilter = input("Input number to choose a filter: ")
	while (not validateUserNumber(userInputFilter, len(userFilterOptions))):
		userInputFilter = input("Please input a valid number to choose how to filter the file: ")

	if userFilterOptions[int(userInputFilter)-1] == 'dob':
		userInputFilterDetail = input("Please input filter for " + userFilterOptions[int(userInputFilter)-1] + " in form of a year: ")
		while (not validateYear(userInputFilterDetail)):
			userInputFilterDetail = input("Please input a valid filter for " + userFilterOptions[int(userInputFilter)-1] + " in form of a year (YYYY): ")
	else:
		userInputFilterDetail = input("Please input filter for " + userFilterOptions[int(userInputFilter)-1] + ": ")
		while (len(userInputFilterDetail) == 0):
			userInputFilterDetail = input("Please input a valid filter for " + userFilterOptions[int(userInputFilter)-1] + ": ")

	return (userInputFilter, userInputFilterDetail)

#function for picking a csv file to filter/return
def chooseFile():
	files = []
	for filename in os.listdir(os.getcwd()):
	    if filename.endswith(".csv"): 
	         files.append(filename)

	if (len(files) == 0):
		return 0

	counter = 1
	for file in files:
		print(f"{counter}: {file}")
		counter+=1

	userInput = input("Input number to choose which file to be parsed: ")
	while (not validateUserNumber(userInput, len(files))):
		userInput = input("Please input a valid number to choose which file to be parsed: ")

	return files[int(userInput)-1]

#checking if the user entered a number only respsonse that is within given range
def validateUserNumber(userNum, maxNum):
	if (not userNum.isdigit()):
		return False
	elif int(userNum) == 0 or int(userNum) > maxNum:
		return False
	else:
		return True

#check if date is 4 numbers
def validateYear(year):
	if (not year.isdigit()):
		return False
	else:
		return len(year) == 4


if __name__ == "__main__":
    fileToBeParsed = chooseFile()
    if fileToBeParsed == 0:
    	print("There are no CSV files in the directory")
    else:
    	userFilter = getUserFilter(fileToBeParsed)
    	parseFileWithFilter(fileToBeParsed, userFilter[0], userFilter[1])