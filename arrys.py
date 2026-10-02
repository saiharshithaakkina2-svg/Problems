#find the second heighist number

s = 11 ,50 ,1 ,49 ,10

firstlarge = 0

for i in range(len(s)):
    if s[i] > firstlarge:
        secondlarge = firstlarge
        firstlarge = s[i]
    elif s[i] > secondlarge:
        secondlarge = s[i]    
print(firstlarge , secondlarge)
      



