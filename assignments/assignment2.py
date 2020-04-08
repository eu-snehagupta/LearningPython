###TASK1:
#function which calculate sum of the digits.
print("*******************************")
def calulation(a):
    if(a>0):
        return (a%10) + calulation(a//10)
    elif(a<0):
        a = (-a)
        return (a%10) + calulation(a//10)
    elif(a==0):
       return 0

if __name__ == "__main__":
    x = int(input("Enter the digit: "))   
    print("Sum of the digits: ", calulation(x))


###TASK2: 
# reformat string acording to their functions reverse, split, uppercase, multipleby3, strip, slicing.
print("*******************************")
def reformat_string(data, function):
    if function == "reverse":
        return data[len(data):0:-1]   
    elif function == "split":
        return data.split()
    elif function == "uppercase":
        return data.upper()
    elif function == "multipleby3":
        return data*3
    elif function == "strip":
        return data.strip() 
    elif function == "slicing":
        return data[0:4] + data [6:-1]
    else:
        print("Invalid function!")               

if __name__ == "__main__":
    data = input("Enter your string: ")
    print("These are the functions: reverse, split, uppercase, multipleby3, strip, slicing")
    function = input("Enter your function: ").lower()
    print("Your reformed string: ", reformat_string(data, function))

# ###TASK3:
# Tom and jerry are playing game with two dice. Score of the game is the sum of number shown on the two dices.
# (i)Print all the combination of dices score possible,
# (ii)One of the dice is got broken such that it does not have face showing 6 and face showing 1.
# Print the possible score like in 1) with this condition
# (iii)Some how, Tom starts cheating and every other time he throws the dice, the number on one of them is always even. 
# Print one such possible set of scores ( combination of numbers that shows on the dices) thrown by Tom in 10 consecutive trails.
print("*******************************")
import random
def allchoice():
    for i in range (0,7,1):
        for j in range (0,7,1):
            print("The outputs of {}|{} is: {}.".format(i,j,(i+j)))
def defect():
    for i in range (2,6,2):
        for j in range (0,7,1):
            print("The outputs of {}|{} is: {}.".format(i,j,(i+j)))    
def cheat():
    i=random.choice([2,4,6])
    j=random.choice([1,2,3,4,5,6])
    print("The outputs of {}|{} is: {}.".format(i,j,(i+j))) 

def handle(choice):
    if choice==1:
        allchoice()
    elif choice==2:
        defect()
    elif choice==3:
        cheat()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    print("1-all cobinations,,2-with defect,,3-cheating problem")
    choice=int(input("Enter your choice: "))
    handle(choice)
    