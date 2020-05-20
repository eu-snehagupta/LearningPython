#Task:
#In order to do the assignment we need to create files and folders, for this just run the file create_files_for_assgmnt4.py like
#python create_files_for_assgmnt4.py. this would create a folder named assignment4 and inside the folder 4 files.
#Question 1: Write code in the below block to create one more directory inside directory assignment4
# names the directory "assignment-your-name"
#Question 2: write code to create a text file name "new_pizza.txt" read the date from the file , pizza.txt at assignment4/pizza.txt 
# and write the same data to the new file you created ("new_pizza.txt") increase the amount of each pizza type by 10, before writing it to
# the new file. e.g. pizza-0 5 changes to pizza-0 15. The new text files should be create inside the directory directory_name_2
#Question 3: complete the function read_csv_to_dict(file_path), here file_path is the path of file, assignment4/products.csv
# write code to read the file at location file_path and copy the data into a dictionary final_dict
#Question 4: complete the function create_file_append_data ,which reads all the file fruit.txt, pizza.txt and vegetables.txt
# then it creates a new text file with all the data written into it. Create a file name "all_data_combined.txt" at directory_name_2
  

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
    final_dict = {}
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for r in reader:
                final_dict[r["Product"]] ={"Quantity":r["Quantity"], "Available":r["Available"]}
    return final_dict
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