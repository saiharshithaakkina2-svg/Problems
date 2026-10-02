# craete a set
#duplicates are removed automatically

numbers = {10,20,30 , 30,40}
print(numbers)

fruits = {"apple", "banana", "mango"}

print(fruits)

numbers = set([1, 2, 3, 4])

print(numbers)

#we canot acess the indexes 
#nums = {10, 20, 30}

#print(nums[0])  error

# Loop Through a Set
numbers = {10, 20, 30}

for i in numbers:
    print(i)

#adding the element 
numbers.add(50)
numbers.update([40,60,80])
numbers.remove(30)
numbers.discard(200) #if not exist it safly excute without passing an error
print(numbers)

num = {10, 20,500, 30}

num.pop() # remove the  first element of list
num.clear()

print(num)

# checking exexst in or not
n = {10, 20, 30}

if 20 in n:
    print("Found")

# return a no.of unique elements

print(len(n))

# union :combine 2 sets 
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b) #a|b
result = a.intersection(b) # return common values
result = a.difference(b) # first set that are not in the second.
result = a.symmetric_difference(b)  #exist in either set, but not in both.

print(result)