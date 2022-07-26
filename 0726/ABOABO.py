blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
ABO_dict={}
for i in ['A','B','AB','O']:
    ABO_dict[i]=blood_types.count(i)
print(ABO_dict)
