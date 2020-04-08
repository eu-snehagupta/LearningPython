# ###TASK1-
# # Coronavirus is at its peak and Jerry wants to help his community; he gets a list of addresses from the municipality which has the name and address being string and Income being a float number.
# # From this data which Jerry got from the municipality, he needs to extract all persons whose income is less than Rs 10,000/month. So that he can distribute free food to all of them. 
# # Using list comprehension, write code to output a list with family having income <= 10,000.
# ##########################################
# input_list1 = [ 
#                 ("Rishi", "Bhilwandi-24", 100000.50), 
#                 ("Ramesh", "Hawai Mahal-12", 1900.45),
#                 ("Ram", "Kothaguda-24", 100030.50), 
#                 ("Rohini", "Gachibowli", 200000.50),
#                 ("Rashi", "Begumpet", 150000.50), 
#                 ("Rinki", "Miyapur", 45000.50),
#                 ("Pink", "Mahavir nagar-23", 1530.50), 
#                 ("Daniel", "Char minar", 50000.50), 
#                 ("Prince", "Hitech city", 750000.50),
#                 ("Kiara", "Kandivali", 9500.50), 
#                 ("Ritu", "Silicon Hill", 250000.50),
#                 ("Piku", "Patia", 7000.50), 
#                 ("Mohit", "Kormangla", 9900.50),
#                 ("Anu", "Bellandur", 5500.50)
#             ]
# # for elements in input_list1:
# #     if elements[2]<=10000.00:
# #         print(elements[0] +", " +elements[1])
# new_list1 = [elements for elements in input_list1 if elements[2]<10000]
# print("Low income groups are: ", new_list1)

# ###TASK2(a)-
# #There is a list of lists where you need to get the index of the list whose sum is even.
# ######################################
# input_list2 = [[1,4,6,3], [6,2,1,42], [2,6,4,4] ]
# evenindex = []
# for elements in input_list2:
#     if (sum(elements) % 2 == 0):
#         evenindex.append(input_list2.index(elements))
# print("Even Index of the input list are: ", evenindex)

# ###TASK2(b)-
# # There is a book rack with multiple shelves. Each shelf has books and we represent each shelf by python list data structure. 
# # We know that there are the same books kept in multiple shelves and also multiple copies of the same book in a single shelf. 
# # Calculate the total number of unique books in the whole rack.
# input_list3 = [ ["yellow", "blue" ,"yellow", "green"], ["green", "green", "green", "green"], ["yellow", "grey", "yellow", "green"], ["yellow", "grey", "pink", "green"], ["black", "grey", "yellow", "black"] ]
# new_list2 =[]
# for elements in input_list3:
#     for subelements in elements:
#         isElement = subelements in new_list2
#         if isElement == False:
#             new_list2.append(subelements)
# # print(new_list2)
# print("No of unique books in the rack are: {} which are: {} ".format(len(new_list2), new_list2))



