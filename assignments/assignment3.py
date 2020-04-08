###TASK1-
# Coronavirus is at its peak and Jerry wants to help his community; he gets a list of addresses from the municipality which has the name and address being string and Income being a float number.
# From this data which Jerry got from the municipality, he needs to extract all persons whose income is less than Rs 10,000/month. So that he can distribute free food to all of them. 
# Using list comprehension, write code to output a list with family having income <= 10,000.
##########################################
print("******************") 
input_list1 = [ 
                ("Rishi", "Bhilwandi-24", 100000.50), 
                ("Ramesh", "Hawai Mahal-12", 1900.45),
                ("Ram", "Kothaguda-24", 100030.50), 
                ("Rohini", "Gachibowli", 200000.50),
                ("Rashi", "Begumpet", 150000.50), 
                ("Rinki", "Miyapur", 45000.50),
                ("Pink", "Mahavir nagar-23", 1530.50), 
                ("Daniel", "Char minar", 50000.50), 
                ("Prince", "Hitech city", 750000.50),
                ("Kiara", "Kandivali", 9500.50), 
                ("Ritu", "Silicon Hill", 250000.50),
                ("Piku", "Patia", 7000.50), 
                ("Mohit", "Kormangla", 9900.50),
                ("Anu", "Bellandur", 5500.50)
            ]
# for elements in input_list1:
#     if elements[2]<=10000.00:
#         print(elements[0] +", " +elements[1])
new_list1 = [elements for elements in input_list1 if elements[2]<10000]
print("Low income groups are: ", new_list1)

###TASK2(a)-
#There is a list of lists where you need to get the index of the list whose sum is even.
######################################
print("******************") 
input_list2 = [[1,4,6,3], [6,2,1,42], [2,6,4,4] ]
evenindex = []
for elements in input_list2:
    if (sum(elements) % 2 == 0):
        evenindex.append(input_list2.index(elements))
print("Even Index of the input list are: ", evenindex)

###TASK2(b)-
# There is a book rack with multiple shelves. Each shelf has books and we represent each shelf by python list data structure. 
# We know that there are the same books kept in multiple shelves and also multiple copies of the same book in a single shelf. 
# Calculate the total number of unique books in the whole rack.
############################
print("******************") 
input_list3 = [ ["yellow", "blue" ,"yellow", "green"], ["green", "green", "green", "green"], ["yellow", "grey", "yellow", "green"], ["yellow", "grey", "pink", "green"], ["black", "grey", "yellow", "black"] ]
new_list2 =[]
for elements in input_list3:
    for subelements in elements:
        isElement = subelements in new_list2
        if isElement == False:
            new_list2.append(subelements)
print("No of unique books in the rack are: {} which are: {} ".format(len(new_list2), new_list2))

###TASK3-
#Rajiv wants to go for a Europe trip, and needs to do his shopping before departure. 
#His friend Pathak gave him a python dictionary with key as store name and value as list and list of tuples with items that he needs to buy from that store.
#Rajiv thought he would only buy 2 of the non essential items (any two).
#write a method which takes this dictionary as an input and returns the total number of items Rajiv needs to buy before his trip.
####################################
print("******************") 
import random
input_dictionary =   {
                        "Essential": 
                            {
                                "Decathlon": ["Winter Jacket", "Hiking Shoes", "Windcheater", "Socks"] ,
                                "Levis":     ["Jeans", "Tshirt", "Shirt"] ,
                                "Haldiram":  [("Dal Makhani", 10), ("Rajma Chawal", 5), ("Paneer Peas", 10)],
                                "ICICI": ["InternationaL Card", "Euros"]
                            },
                        "Non Essential":
                            { 
                                "Apple": ["Ipad", "Headphone", "Battery", "Charger"]
                            }
                    }  
essential_list = []
nonessential_list = []
for category,options in input_dictionary.items():
    if category == "Essential":
        for stores,objects in options.items():
            for elements in objects:
                essential_list.append(elements)
    elif category == "Non Essential":
        for stores,objects in options.items():
            for elements in objects:
                nonessential_list.append(elements)
nonessential_list = random.sample(nonessential_list, 2)
print("No of item to buy are: {} \n& \nBuy list: {}".format(len(essential_list + nonessential_list),(essential_list + nonessential_list)))


