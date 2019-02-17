# python_summative
A repository with answers to the AIIP python summative

## Problem 1
run `python generate_dummy_dataset.py` to print out a dummy dataset object which contain 32 data items ( ie. 1,2,3...32. ) for each sensor cluster and 16 readings for each individual item.

## Problem 2
run `python generate_dummy_dataset_stored.py` to create a new file every time the command is run. The filename as a timestamp showing when the file was created or data was received from the sensors. The file contains lines with each line representing the individual sensor cluster. Each line has 16 comma separated values for the cluster readings.

## Problem 3
run `python data_error_check.py` to read a dummy data file and create an error log of all the error in the data. Each line in the error_log provides information about sensor cluster causing errors and the date of capture of the sensor cluster data. The function also prints out the corrupt records with "err" replace with -1.
