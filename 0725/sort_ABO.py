def count_blood(L):
    ABO_dict={}
    for i in set(L):
        ABO_dict[i]=L.count(i)
    return ABO_dict

print(count_blood(['A','B','A','O','AB','AB','O','A','B','O','B','AB']))