# add_1 = lambda x: x+1
def add_1(x,y):
    return x+y

add_1 = lambda x,y: x+y # Useful when using as argument

result = add_1(1,7)
print(result)

my_numbers = [1,2,3,4,5,6,7,8,9,10]

def square(x):  # Redundantly defined
    return x ** 2

# squares = list(map(square,my_numbers))

squares = list(map(lambda x:x**2,my_numbers))
print("Map Results:",squares)

evens = list(filter(lambda x:x%2==0,my_numbers))
print("Filter Results:",evens)

values = [(1,'a',"hello"),(2,'a',"world"),(3,'c',"ok")]

sorted_values = sorted(values, key=lambda x:x[1]+x[2])

print("Sort Results",list(sorted_values))

from functools import reduce

numbers = [1,2,3,4,5]
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15

# Using reduce to sum the list without initializer
sum_of_numbers = reduce(lambda acc,x: acc+x,numbers)
print("Sum Using Reduce and lambda:",sum_of_numbers)

# Using reduce to find the maximum value
max_value = reduce(lambda acc, x: acc if acc > x else x, numbers)
print("Maximum Values using Reduce and lambda:",max_value)

fancy_comp = {x:(lambda x:x*x)(x) for x in range(5)}

print("Fancy way to use lambda:",fancy_comp)