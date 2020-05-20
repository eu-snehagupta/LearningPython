#Task 1:
#You have given four list of dictionaries Input data.
#process all the dictionaries in data, to craete one dictionary with only unique keys i.e.
#if A has dict {"milk": 2 } and C has { "milk": 1} , the find sict will have only one 
#{ "milk": 3}.
#Then write the final dictionary to a csv file using DictWriter

import csv
newdata_ = dict()

A = [{"coke": 1 }, {"milk": 2 }, {"curd": 3 }, { "MILK": 1}, {"juice": 3 } ]
B = [{"orange": 1 }, {"papaya": 2 }, {"pineapple": 3 }, { "apple": 1}, {"papaya": 3 } ]
C = [{"jeans": 1 }, {"shirt": 2 }, {"jeans": 3 }, { "milk": 1}, {"SHIRT": 3 } ]
D = [{"HISTORY": 1 }, {"history": 2 }, {"maths": 3 }, { "civics": 1}, {"maths": 3 } ]
data = [A, B, C, D]

def process_dict_lists(data=data):
    for elements in data:
        for subelements in elements:
            for key, value in subelements.items():
                key_ = key.lower()
                newdata_[key_] =  (newdata_[key_] if key_ in newdata_.keys() else 0) + value
    return(newdata_)
def write_dict_csv(newdata_):
    filetowrite = open("assignment5(i)_datafile.csv", "w")
    writer = csv.DictWriter(filetowrite, newdata_.keys())
    writer.writeheader()
    writer.writerow(newdata_)
    filetowrite.close()

if __name__ == "__main__":
    newdata_ = process_dict_lists()
    write_dict_csv(newdata_)


