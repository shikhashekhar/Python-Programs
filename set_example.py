# s={"shikha","suraj","shikha",2,3,5,2,4,7,6}
# print (s)

# for i in s:
#     print(i)

# # myset = set() # to create an empty set
# # print (type(myset))

# # mydict = {} # to create an empty dictionary 
# # print (type(mydict))

# #Set methods

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# print(cities.union(cities2))
# print(cities.update(cities2))

# print(cities.intersection(cities2))
# print(cities.intersection_update(cities2))
# print(cities.symmetric_difference(cities2))
# print(cities.symmetric_difference_update(cities2))
# print(cities.difference(cities2))
# print(cities.difference_update(cities2))

# print(cities.isdisjoint(cities2)) #both sets are disjoint and it will return true if both are two different sets
# print(cities.issuperset(cities2)) # all the elements of other set 2 should be present in set 1 then it will return true else false

# print(cities2.issubset(cities)) #all values should be present in the main set

#add: to add a single item to the set
#update: to update a set with the values of other
#remove()/discard() : to remove items from the list
#if we try to remove using remove method it will raise and error but discard method will not raise any error

#pop(): removes last element but we don't don't know which elements get removed as sets are unordered
#del() : we can delete entire set using the del keyword
#clear(): if we want to delete all items of the set and get an empty set the  we use clear method
