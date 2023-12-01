import numpy as num
from module import Employee, ReceivedInvoice, IssuedInvoice
from datetime import datetime
import csv

EmployeeList = []
ReceivedInvoiceList = []
IssuedInvoiceList = []

with open('data/Employees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        EmployeeList.append(Employee(row['name'], row['surname'], row['salary']))

with open('data/ReceivedInvoice.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ReceivedInvoiceList.append(ReceivedInvoice(row['date'], row['amount']))

with open('data/IssuedInvoice.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        IssuedInvoiceList.append(IssuedInvoice(row['date'], row['amount']))

BaseExpenses = 0
Income = 0
MonthlyExpenses = []
Months = list(range(1,13))
MonthlyIncome = []
Bilans = []

for Employee in EmployeeList:
    BaseExpenses =+ int(Employee.salary)


for month in Months:
    monthly = BaseExpenses
    for ReceivedInvoice in ReceivedInvoiceList:
        d = datetime.strptime(ReceivedInvoice.date, '%Y-%m-%d')
        if (d.month == month):
            monthly =+ int(ReceivedInvoice.amount)
    MonthlyExpenses.append(monthly)

print(MonthlyExpenses)

for month in Months:
    monthly = 0
    for IssuedInvoice in IssuedInvoiceList:
        d = datetime.strptime(IssuedInvoice.date, '%Y-%m-%d')
        if (d.month == month):
            monthly =+ int(IssuedInvoice.amount)
    MonthlyIncome.append(monthly)

print(MonthlyIncome)
Bilans = num.subtract(MonthlyIncome,MonthlyExpenses)
print(Bilans)