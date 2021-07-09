
def best_emp(work_hours):

    max_hrs = 0
    emp_month =''
    min_hrs=0
    worst_emp=''


    for emp_name,hrs_worked in work_hours:
        if (emp_month =='' and worst_emp =='') :
            max_hrs=hrs_worked
            min_hrs=hrs_worked
            emp_month=emp_name
            worst_emp=emp_name


        print(emp_name,hrs_worked)

        if hrs_worked>=max_hrs:
            max_hrs=hrs_worked
            emp_month=emp_name
        elif hrs_worked<min_hrs:
            min_hrs=hrs_worked
            worst_emp = emp_name
    return  max_hrs,emp_month,min_hrs,worst_emp


work_hours=[('Abby',10),('Billy',3000),('Cathy',500),('D',1)]
max_hrs,emp_month,min_hrs,worst_emp=best_emp(work_hours)
print(f'Employee of the month is {emp_month} is with max_hrs {max_hrs}')
print(f'Worst employee of the month is {worst_emp} is with min_hrs {min_hrs}')
