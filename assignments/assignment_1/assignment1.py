#Assignment1:
#There is a  chicken company called “Golden chicken”. The company needs to know the total number of alive chickens available for sale each day. The number of chickens on a current day depends on following factors
#1.Number of chickens the last day
#2.Rate of death of chickens
#3.Rate of birth of chickens
#Further 5% more chicken dies on Monday and Wednesday than any other weekdays. Write a function which takes as input argument, no of chicken last day, rate of death of chicken, rate of birth of chicken and day of the week and return the total number of alive chicken. Try to break the task into multiple functions to make the code modular and more readable.


#author:sneha
#date:27_03_2020

#defines the calculation for percentage
#input:principle, rate
def calculate_percentresult(principle,rate):
    return (principle*rate)/100

#defines the calculation for no of chicken on current day
#input:no_last_day,d_rate,b_rate,current_day
def calculate_chickens(no_last_day,d_rate,b_rate,current_day):
    total_death = calculate_percentresult(no_last_day,d_rate)
    total_birth = calculate_percentresult(no_last_day,b_rate)

    if current_day=="monday" or current_day=="wednesday":
        further_death = calculate_percentresult(no_last_day,5)
    elif current_day=="tuesday" or current_day=="thrusday" or current_day=="friday" or current_day=="saturday" or current_day=="sunday":
        further_death = 0
    else:
        print("Invalid input")
        exit()

    count_chicken = str(no_last_day - total_death + total_birth - further_death)
    return count_chicken

#prints welcomescreen
def welcomescreen():
    print("********************************************")
    print("******Hi. Welcome to Golden Chicken!!*******")
    print("********************************************")

#take input informations
#output:no_last_day, d_rate, b_rate, current_day
def inputscreen():
    no_last_day = input("Enter number of chickens last day: ")
    d_rate = input("Enter rate of death of chickens in %: ")
    b_rate = input("Enter rate of birth of chickens in %: ")
    current_day = input("Enter todays day: ").lower()
    return no_last_day, d_rate, b_rate, current_day

#prints the output results
def outputscreen(no_last_day, d_rate, b_rate, current_day):
    print("Number on chicken on a current date: " + calculate_chickens(int(no_last_day), int(d_rate), int(b_rate), current_day))
    print("ThankYou")

#main
if __name__ == "__main__":
    welcomescreen()
    no_last_day, d_rate, b_rate, current_day = inputscreen()
    outputscreen(no_last_day, d_rate, b_rate, current_day)
