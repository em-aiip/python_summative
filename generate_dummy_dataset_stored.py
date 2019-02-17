import datetime
import random

if __name__ == "__main__":
    #Open data file for storage of cluster sensor readings
    with open("generated_dummy_data_{}.csv".format(datetime.datetime.now().replace(microsecond=0).isoformat(),), 'w') as f:
        sensor_cluster_data = {}
        #loop through the 32 sensor cluster
        for i in range(1, 33):
            #Generate the 16 readings for each cluster
            readings = [str(random.random()) for j in range(1, 17)]
            sensor_cluster_data[i + 1] = readings

            f.write(",".join(readings)+"\n")