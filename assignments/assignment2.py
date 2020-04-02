# *******TASK1:function which calculate sum of the digits**********
def cal(a):
    if(a==0):
        return 0
    else:
       return (a%10) + cal(a//10)
    
x = int(input("Enter the digit: "))
print("Sum of the digits: " +str(cal(x)))


# *******TASK2: reformat string acording to their functions**********
def reformat_string(data, function):
    if function == "reverse":
        return data[len(data):0:-1]   
    elif function == "split":
        return data.split()
    elif function == "upper case":
        return data.upper()
    elif function == "multiple by 3":
        return data*3
    elif function == "strip":
        return data.strip() 
    elif function == "slicing":
        return data[0:4] + data [6:-1]
    else:
        print("Invalid function!")               


data = input("Enter your string: ")
function = input("Enter your function: ")
print(reformat_string(data, function))

#********TASK3:(i)
for i in range (0,7,1):
    for j in range (0,7,1):
        print("The outputs of" +str(i) +"|" +str(j) +"is: " +str(i+j))

#********TASK3:(ii)
for i in range (1,6,1):
    for j in range (0,7,1):
        print("The outputs of" +str(i) +"|" +str(j) +"is: " +str(i+j))        


# #********TASK3:(iii)
# A=[]
# for i in range (0,7,2):
#     for j in range (0,7,1):
#         A= A.insert(0, i+j)   
