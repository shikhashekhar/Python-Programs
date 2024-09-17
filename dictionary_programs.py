info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  
#Dictionary methods
#update() -> updtae() method updtaes the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
#clear() -> used to remove items from the dictionary and give an empty dictionary
#pop() -> removes the key-value pair whose key is passed as a parameter
#popitem() -> removes the last key-value pair from the dictionary
# del -> we can also use the del keyword to remove a dictionary item
# If key is not provided del keyword will delete the dictionary entirely

# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}

# # ep1.update(ep2)
# # ep1.clear()
# # ep1.pop(122)
# ep1.popitem()
# del ep1[122]
# print(ep1) 
