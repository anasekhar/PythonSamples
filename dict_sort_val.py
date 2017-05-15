
"""
   code to sort the dictornary by using values
"""

def sort_dict(dict_sor):
    print dict_sor.get
    return sorted(dict_sor,key=dict_sor.get)


#d = {1:11,2:2,3:4,5:7,6:9,5:6}
d = {10:2,20:3,3:30,4:30,40:5,90:9,2:25}
dict_keys = sort_dict(d)

for ele in dict_keys:
    print ele,":",d[ele]



################# Other logic ##########


def sort_dict(dict_sor,sort_type=0):
    return sorted(d.items(),key=lambda x:x[sort_type])


print "\n Sort dict uisng keys:", sort_dict(d,0)
print "\n Sort dict using values:",sort_dict(d,1)
