## Assignment
Create a command line application that parses a CSV file and filters the data per user input.

The CSV will contain three fields: `first_name`, `last_name`, and `dob`. The `dob` field will be a date in YYYYMMDD format.

The user should be prompted to filter by `first_name`, `last_name`, or birth year. The application should then accept a name or year and return all records that match the value for the provided filter. 

Example input:
```
first_name,last_name,dob
Bobby,Tables,19700101
Ken,Thompson,19430204
Rob,Pike,19560101
Robert,Griesemer,19640609
```

## How-To
1. This is a python3 application that looks for csv files in the same directory the python3 file is at. To run it, just type python3 ScoirChallenge.py and follow the prompts that it asks.

## Assumptions
1. This application does assume that CSV files have a valid header and the CSV files follow the same format as the example input
