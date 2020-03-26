def calculate_chickens(no_last_day,d_rate,b_rate,current_day):
    total_death = (no_last_day*d_rate)/100
    total_birth = (no_last_day*b_rate)/100
    
    if current_day=="monday" or current_day=="wednesday":
        further_death = (no_last_day*5)/100
        
    elif current_day=="tuesday" or current_day=="thrusday" or current_day=="friday" or current_day=="saturday" or current_day=="sunday":
        further_death = 0
    else:
        print("Invalid input")
        exit()

    count_chicken = str(no_last_day - total_death + total_birth + further_death)
    return count_chicken



no_last_day = input("Enter number of chickens last day: ")
d_rate = input("Enter rate of death of chickens: ")
b_rate = input("Enter rate of birth of chickens: ")
current_day = input("Enter todays day: ").lower()
no_of_chicken_today = calculate_chickens(int(no_last_day),int(d_rate),int(b_rate),current_day)
print("Number on chicken on a current date: " +no_of_chicken_today)