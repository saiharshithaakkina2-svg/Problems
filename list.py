#Updating , adding , extend list 
# marks = [80, 75, 92]
# marksB = [78 , 28]
# marks[1] = 85
# marks.append(95)
# marks.insert(1,88)
# marks.extend(marksB)

# print(marks)

#Removing the elements

#num = [10 , 20 ,30 , 40]
#num.remove(10)
#num.pop()
#num.clear()
#nums = del num[1]
#print(nums)

#List Utility Functions
#num = [10 ,20 ,30 , 10]
#num.sort()
#num.reverse()
#nums = len(num)
#nums = min(num)
#nums = max(num)
#nums = sum(num)
#print(nums)
#matrix = [
 #   [1, 2, 3],
  #  [4, 5, 6],
   # [7, 8, 9]
#]

#print(matrix[0] )
#print(matrix[0][1])
#print(matrix[2][2] )

#matrix = [
 #   [10, 20],  
  #  [30, 40]
#]
#Outer loop:
#→ takes one row

#Inner loop:
#→ takes each value in that row

#Flow:
#row → value → process
#→ next value → next row

#for row in matrix:
 #   for value in row:
  #      print(value)


person = ("ravi" , 20 , 'tuple')    
name , age , language = person   
print(language)