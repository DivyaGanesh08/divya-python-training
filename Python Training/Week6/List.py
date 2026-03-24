#list

#reverse a list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)   

#Find the 2nd largest element in list

my_list = [10, 20, 30, 40, 50]
my_list.sort()
print(my_list[-2]) 

#remove duplicates from list
my_list = [1, 2, 2, 3, 4, 4]
my_list = list(set(my_list))
print(my_list)  
