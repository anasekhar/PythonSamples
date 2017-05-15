"""
   sorting multiple dicts in a list
"""

def dict_sort(dic_list):
    return sorted(dic_list, key=lambda y: y['name'])

ll = [{'name': 'Rajesh', 'age': 49},{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age':10},{'name': 'Ganesh', 'age': 24}]

out = dict_sort(ll)

print out
