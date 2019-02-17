import datetime

if __name__ == "__main__":
    filename = "generated_dummy_data_2019-02-17T08:52:20_corrupted.csv"
    #load_corrupted data from file
    with open(filename, 'r') as f:
        lines = f.readlines()

    #Load error log for writing in append mode
    with open("error_log","a") as fw:
        for i, line in enumerate(lines):
            readings = line.strip().split(",")
            if "err" in line:
                #Convert "err" string to numerical value to be uniquely identified
                new_readings = [-1 if s == "err" else float(s) for s in readings]
                error_message = "{}: Corrupt Data Error: Sensor {} sent corrupt data on {}\n".format( \
                    datetime.datetime.now().replace(microsecond=0).isoformat(),i,filename.split("_")[3])

                print new_readings
                fw.write(error_message)