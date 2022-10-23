from pprint import pprint
import Weather
import pandas as pd
import numpy as np
import random


def choose_random_elements_from_CSV(s):
    """
    this function returns random cities from csv file
    :param s: desired cities to return
    :return: random s cities from csv
    """
    print(f"Choosing random {s} cities and getting info about current temperature and humidity in that city")
    filename = "worldcities.csv"
    n = 623  # number of records in file (excludes header)
    skip = sorted(random.sample(range(1, n + 1), n - s))  # the 0-indexed header will not be included in the skip list
    df = pd.read_csv(filename, skiprows=skip)
    df = df["city"].tolist()

    return df


def transform_data_into_desired_format(data_list):
    current_city = 0
    failed_city = 0
    data_dictionary = {}
    for elem in data_list:

        try:
            data_dictionary[elem] = Weather.Weather(city=elem).get_data()
            current_city += 1
            print(f"generated data for city:{elem}, generated data of {current_city} cities")
        except:
            failed_city += 1
            print(f"failed to generated data for city:{elem}, failed to generate data of {failed_city} cities")

    print("Data generated ready to cluster")
    return data_dictionary


def transform_data_into_raw_format(data_list):
    raw_data = []
    current_city = 0
    failed_city = 0
    for elem in data_list:

        try:
            raw_data.append(Weather.Weather(city=elem).get_raw_data())
            current_city += 1
            print(f"generated data for city:{elem}, generated data of {current_city} cities")
        except:
            failed_city += 1
            print(f"failed to generated data for city:{elem}, failed to generate data of {failed_city} cities")

    print("Data generated ready to cluster")
    raw_data = np.array(raw_data)
    return raw_data
