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
        print("Net salary: ",self.net_salary )

def read_data(file_path):
    data = {}
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for r in reader:
            print("{}".format(r["Company_name;Employee_name;Basic Salary/month;Loan acquired (10% would be deducted from the salary);Bonus as per the rating;Rating"]))    
    print (data)


# employee = Company("TCS", "Oscar", 50000, 110000, 10, "A")
# employee.calculate_net_salary()
file_path = "C://Users//Neha//Desktop//python//learningpython//assignments//assignment_7datafile.csv"
# file_path = "assignment_7datafile.csv"
read_data(file_path)


        
        
