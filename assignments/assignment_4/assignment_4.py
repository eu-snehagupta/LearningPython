    
#write imports required to do the assignment
import os

def create_my_text_file(directory_name_2):
    readfile_names = "pizza.txt"
    readfile_path = os.path.join(directory_name_1, readfile_names)
    writefile_names = "new_pizza.txt"
    writefile_path = os.path.join(directory_name_2, writefile_names)
    itemlist = []
    with open(readfile_path, "r") as f:
        for eachelement in f:
            element = eachelement.split()
            itemlist.append( (element[0], int(element[1])+10) )
    with open (writefile_path, "w") as f:
        for eachitem in itemlist:
            f.writelines( (str(eachitem[0]), " ", str(eachitem[1]), "\n") )

# def read_csv_to_dict(file_path):
#     final_dict = dict()
#     '''write code to read the file at location file_path and copy the data
#        into a dictionary final_dict'''
#     return final_dict


# def create_file_append_data(directory_name_2):
#     # create a file name "all_data_combined.txt" at directory_name_2





#     pass # remove pass once you have your code written

if __name__ == "__main__":
    directory_name_1 = "assignment4"
    directory_name_2 = "assignment-sneha"
    if not os.path.isdir(directory_name_2):
        os.mkdir(directory_name_2)
    else:
        print("There is already a directory named assignment-sneha, pls remove or rename it")
    
    create_my_text_file(directory_name_2)


    # #Question 3: complete the function read_csv_to_dict(file_path)
    # # here file_path is the path of file, assignment4/products.csv
    # file_path = "assignment4/products.csv"
    # dict_data = read_csv_to_dict(file_path)
    # print(dict_data)


    # # Question 4: complete the function create_file_append_data ,
    # # which reads all the file fruit.txt, pizza.txt and vegetables.txt
    # # then it creates a new text file with all the data written into it.
    # create_file_append_data(directory_name_2)