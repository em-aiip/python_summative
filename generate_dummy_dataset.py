import random

if __name__ == "__main__":
    #Object to hold all cluster readings
    sensor_cluster_data = {}

    # loop for the 32 sensor clusters
    for i in range(0, 32):
        print i
        #Generate the 16 readings for each cluster
        readings = [str(random.random()) for j in range(1, 17)]
        sensor_cluster_data[i+1] = readings

    print sensor_cluster_data