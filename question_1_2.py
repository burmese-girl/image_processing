import json
import csv
import os
from collections import OrderedDict

mypath = os.path.dirname(os.path.abspath(__file__))


def convert_CSVtoJSON_B_004():
    with open(mypath + '/Question1/Dataset/12163257_B_004_00001.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
    csvfile.close()

    data = sort_order2 = []
    json_data = {}
    with open(mypath + '/Question1/Dataset/12163257_B_004_00001_mayyi.json', 'w') as jsonfile:

        for row in rows:
            csv_data = {"x": row[0], "y": row[1], "width": row[2], "height": row[3], "tag": row[4]}
            data.append(csv_data)

        # sorted inner dictionary
        sort_order = ['x', 'y', 'width', 'height', 'tag']
        ordered = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                   for item in data]

        count = 1
        for i in range(0, len(ordered)):
            format_record = 'record_' + str(format(count, '02d'))
            dict_data = {format_record: ordered[i]}
            json_data.update(dict_data)
            sort_order2.append(format_record)
            count += 1

        # sorted outer dictionary
        ordered2 = [OrderedDict(sorted(item.items(), key=lambda item: sort_order2.index(item[0])))
                    for item in [json_data]]

        json.dump(ordered2[0], jsonfile, sort_keys=False)

    csvfile.close()


def convert_CSVtoJSON_B_007():
    with open(mypath + '/Question1/Dataset/12163257_B_007_00001.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
    csvfile.close()

    data = sort_order2 = []
    json_data = {}
    with open(mypath + '/Question1/Dataset/12163257_B_007_00001_mayyi.json', 'w') as jsonfile:

        for row in rows:
            csv_data = {"x": row[0], "y": row[1], "width": row[2], "height": row[3], "tag": row[4]}
            data.append(csv_data)

        # sorted inner
        sort_order = ['x', 'y', 'width', 'height', 'tag']
        ordered = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                   for item in data]

        count = 1
        for i in range(0, len(ordered)):
            format_record = 'record_' + str(format(count, '02d'))
            dict_data = {format_record: ordered[i]}
            json_data.update(dict_data)
            sort_order2.append(format_record)
            count += 1

        ordered2 = [OrderedDict(sorted(item.items(), key=lambda item: sort_order2.index(item[0])))
                    for item in [json_data]]

        json.dump(ordered2[0], jsonfile, sort_keys=False)

    csvfile.close()


def convert_CSVtoJSON_B_013():
    with open(mypath + '/Question1/Dataset/12163257_B_013_00001.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
    csvfile.close()

    data = sort_order2 = []
    json_data = {}
    with open(mypath + '/Question1/Dataset/12163257_B_013_00001_mayyi.json', 'w') as jsonfile:

        for row in rows:
            csv_data = {"x": row[0], "y": row[1], "width": row[2], "height": row[3], "tag": row[4]}
            data.append(csv_data)

        # sorted inner
        sort_order = ['x', 'y', 'width', 'height', 'tag']
        ordered = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                   for item in data]

        count = 1
        for i in range(0, len(ordered)):
            format_record = 'record_' + str(format(count, '02d'))
            dict_data = {format_record: ordered[i]}
            json_data.update(dict_data)
            sort_order2.append(format_record)
            count += 1

        # sorted outer
        ordered2 = [OrderedDict(sorted(item.items(), key=lambda item: sort_order2.index(item[0])))
                    for item in [json_data]]

        json.dump(ordered2[0], jsonfile, sort_keys=False)

    csvfile.close()


def convert_CSVtoJSON_B_017():
    with open(mypath + '/Question1/Dataset/12163257_B_017_00001.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
    csvfile.close()

    data = sort_order2 = []
    json_data = {}
    with open(mypath + '/Question1/Dataset/12163257_B_017_00001_mayyi.json', 'w') as jsonfile:

        for row in rows:
            csv_data = {"x": row[0], "y": row[1], "width": row[2], "height": row[3], "tag": row[4]}
            data.append(csv_data)

        # sorted inner
        sort_order = ['x', 'y', 'width', 'height', 'tag']
        ordered = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                   for item in data]

        count = 1
        for i in range(0, len(ordered)):
            format_record = 'record_' + str(format(count, '02d'))
            dict_data = {format_record: ordered[i]}
            json_data.update(dict_data)
            sort_order2.append(format_record)
            count += 1

        # sorted outer
        ordered2 = [OrderedDict(sorted(item.items(), key=lambda item: sort_order2.index(item[0])))
                    for item in [json_data]]

        json.dump(ordered2[0], jsonfile, sort_keys=False)

    csvfile.close()


def convert_CSVtoJSON_B_018():
    with open(mypath + '/Question1/Dataset/12163257_B_018_00001.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
    csvfile.close()

    data = sort_order2 = []
    json_data = {}
    with open(mypath + '/Question1/Dataset/12163257_B_018_00001_mayyi.json', 'w') as jsonfile:

        for row in rows:
            csv_data = {"x": row[0], "y": row[1], "width": row[2], "height": row[3], "tag": row[4]}
            data.append(csv_data)

        # sorted inner
        sort_order = ['x', 'y', 'width', 'height', 'tag']
        ordered = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                   for item in data]

        count = 1
        for i in range(0, len(ordered)):
            format_record = 'record_' + str(format(count, '02d'))
            dict_data = {format_record: ordered[i]}
            json_data.update(dict_data)
            sort_order2.append(format_record)
            count += 1

        # sorted outer
        ordered2 = [OrderedDict(sorted(item.items(), key=lambda item: sort_order2.index(item[0])))
                    for item in [json_data]]

        json.dump(ordered2[0], jsonfile, sort_keys=False)

    csvfile.close()


# call_methods
convert_CSVtoJSON_B_004()
convert_CSVtoJSON_B_007()
convert_CSVtoJSON_B_013()
convert_CSVtoJSON_B_017()
convert_CSVtoJSON_B_018()
