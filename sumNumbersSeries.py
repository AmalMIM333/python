#this program take a series of numbers from the user and print the sum of these numbers

print ("Enter a series of numbers you want to add, series end if you type 0")
sum = 0
x = int(input())
while x != 0:
    sum += x
    x = int(input())
print (sum)
    
    
