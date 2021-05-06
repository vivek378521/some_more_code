
import requests
import csv
import json


def getDataFromAPI(url):
    try:
        response = requests.get(url)
        print("Call was successful")
        return response.text
    except requests.exceptions.HTTPError as error:
        print("An error has occured :")
        print(error)


def saveJSONDataToCSV(json_data, filename):
    data = json.loads(json_data)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

    return "Data saved in " +filename


if __name__ == "__main__":
    filename = input("Enter the name you want to save your csv with (without csv extension)") + ".csv"
    json_data = getDataFromAPI("https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog")
    if json_data is not None:
        print(saveJSONDataToCSV(json_data, filename))
    print("Your csv with the data is made! Bye!")

