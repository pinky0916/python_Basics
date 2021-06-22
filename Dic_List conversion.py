keys=['Navin','Kiran','Ravi']
values=[20,30,40]
data_dict=dict(zip(keys,values))
print(data_dict)

#To add values to dictionary
data_dict['Suri']=100

print(f'Modified value is : {data_dict}')


#to remove data
del data_dict['Suri']
print(f'Deleted value is : {data_dict}')


