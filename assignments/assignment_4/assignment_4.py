import os
import csv

def create_my_text_file(directory_name_2):
    itemlist = []
    with open(os.path.join(directory_name_1, "pizza.txt"), "r") as f:
        for eachelement in f:
            element = eachelement.split()
            itemlist.append( (element[0], int(element[1])+10) )
    with open (os.path.join(directory_name_2, "new_pizza.txt"), "w") as f:
        for eachitem in itemlist:
            f.writelines( (str(eachitem[0]), " ", str(eachitem[1]), "\n") )

def read_csv_to_dict(file_path):
    file_ = open(file_path)
    reader_ = csv.DictReader(file_)
    storeinfo = []
    for r in reader_:
        storeinfo.append(r)
    file_.close()
    return storeinfo

def create_file_append_data(directory_name_2):
    itemlist = []
    readfile_names = ["fruits.txt", "pizza.txt", "vegetables.txt"]
    for elements in readfile_names:
        readfile_path = os.path.join(directory_name_1, elements)
        with open(readfile_path, "r") as f:
            for eachline in f:
                itemlist.append(eachline)
        
    with open(os.path.join(directory_name_2, "all_data_combined.txt"),"w") as f:
        for eachitem in itemlist:
            f.writelines(eachitem)
    
if __name__ == "__main__":
    directory_name_1 = "assignment4"
    directory_name_2 = "assignment-sneha"
    if not os.path.isdir(directory_name_2):    ####Task(i):
        os.mkdir(directory_name_2)
    else:
        print("There is already a directory named assignment-sneha, pls remove or rename it") 
    create_my_text_file(directory_name_2)    ####Task(ii):   
    file_path = "assignment4/products.csv"
    dict_data = read_csv_to_dict(file_path)    ####Task(iii):
    print(dict_data)
    create_file_append_data(directory_name_2)    ####Task(iv):