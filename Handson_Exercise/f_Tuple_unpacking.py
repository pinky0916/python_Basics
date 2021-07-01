
def emp_month(list1):
    max_hrs=0
    min_hrs=0

    for name,no_of_hours in list1:
        print(name,no_of_hours)
        if max_hrs<no_of_hours:
            max_hrs=no_of_hours
            emp_month=name
        else:
            min_hours=no_of_hours
            worst_emp=name
    return (emp_month,max_hrs,worst_emp,min_hours)
list1 = {('Abby', 7000), ('Billy', 400), ('Cassie', 800), ('Daddy', 100)}
x,y,a,b=emp_month(list1)
print(f'Employee of the month is {x} has {y} hours worked ')
print(f'Worst employee of the month is {a} has {b} hours worked ')