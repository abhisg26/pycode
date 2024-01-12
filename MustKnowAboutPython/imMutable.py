# Immutable types
# str
# int
# float
# bool
# bytes
# tuple

# Mutable types
# list
# set
# dict

## Tuples
# x = (1,2)

# y=x # it makes a copy of y

# x=(1,2,3) # Overwrite x
# # x[0]=1 # Will throw error as tuple is immutable

# print(x,y)

## Lists
x = [1,2]
y = x # x and y are storing the reference to the same object

x[0]=100 # this operation is allowed since lists are mutables

print(x,y)

def get_largest_numbers(numbers,n):
    numbers.sort()  # sorts the list in place because list is mutable object

    return numbers[-n:]

nums = [2,3,4,1,34,123,321,1]

print(nums)
largest = get_largest_numbers(nums,2)
print(largest)
print(nums)

