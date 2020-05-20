#Task:
#In the attached csv file "assignment7_datafile.csv" you would find some details about companies, employees and their salaries
#Create a class called Company with attributes company_name, employee_name, salary, loan_acquired, bonus and rating.
#your class will have a method called calculate_net_salary which does salary calculations based on the data in the csv file.
#For eg: Calculate Salary for Oscar : 50000-( 10% of 110000)+(10% of 50000) = 44000. DOn't forget to have a constructer of your
#class.
#Loop through the data in csv file and using this class create objects corresponding to each company in the csv file, 
#call the function calculate_net_salary on each of this object to get the salary, keep on saving the employee name and 
#salary in a dictionary declared globaly.
#Output: Create a dictionay with employees name as a key and net salary as a value, print this disctionary.


import os
import csv
class Company:
    def __init__(self,company_name,employee_name,basic_salary,loan_acquired,bonus,rating):
        self.company_name = company_name
        self.employee_name = employee_name
        self.basic_salary = basic_salary
        self.loan_acquired = loan_acquired
        self.bonus = bonus
        self.rating = rating

    def calculate_net_salary(self):
        self.net_salary = self.basic_salary- ((10 * self.loan_acquired)/100) +((self.bonus * self.basic_salary)/100)
        return self.net_salary

def read_data(file_path):
    # finaldict = {}
    data = []
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for r in reader:
            for key, value in r.items():
                for elements in r:
                    print(key)
            #     data.append(key)
            # print(data)

        #   employee = Company(data)
        #   Employee_Salary = employee.calculate_net_salary()
        #   finaldict[r["Employee_name"]] = Employee_Salary
        #   print(finaldict)    
        


# employee = Company("TCS", "Oscar", 50000, 110000, 10, "A")
# employee.calculate_net_salary()
file_path = "C://Users//Neha//Desktop//python//learningpython//assignments//assignment7_datafile.csv"
# file_path = "assignment_7datafile.csv"
read_data(file_path)


        
        
