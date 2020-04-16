import os
import csv


def create_text_files(directory_name):
    # Lets create 5 files in the directory
    file_names_textFiles = ["fruits.txt", "pizza.txt", "vegetables.txt"]

    for file_ in file_names_textFiles:
        file_path = os.path.join(directory_name, file_)
        file_item_name = os.path.splitext(file_)[0]
        with open(file_path, "w") as f:
            for i in range(5):
                f.write(file_item_name + "-" + str(i)+ " " +str((i+1)*int(len(file_item_name))))
                f.write("\n")

def create_csv_file(directory_name):
    #create a csv files with products and their availablity
    dict_to_write = [ {"Product": "Jean", "Available": True, "Quantity": 10 },
                    {"Product": "Shirt", "Available": False, "Quantity": 0 },
                    {"Product": "Belt", "Available": True, "Quantity": 100 },
                    {"Product": "Shoes", "Available": True, "Quantity": 9 }]  
    full_path_csv_file = os.path.join(directory_name, "products")
    with open(full_path_csv_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=dict_to_write[0].keys())
        writer.writeheader()
        writer.writerows(dict_to_write)



if __name__ == "__main__":
    directory_name = "assignment4"
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
        create_text_files(directory_name)
        create_csv_file(directory_name)
    else:
        print("There is already a directory named assignment4, pls remove or rename it")
