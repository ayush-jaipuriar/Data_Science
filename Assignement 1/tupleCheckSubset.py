tuple1 = (1,2,3,4,5)
tuple2 = (1,2,3,4,5,6,7,8,9,10)
#I convert tuple to set and then use the built in issubset() function to check if tuple1 is subset of tuple2
check = set(tuple1).issubset(tuple2)
print(check)
