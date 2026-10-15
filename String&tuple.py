#string Concatenation

Str1= "Hello "
Str2 = input ("Enter Your Name:")
result= Str1+ Str2
# Print(result)
#Concatenate 3 strings 
Str3= ", Welcome to python programming"
R= result+ Str3
print (R)

# print the first character

print("first Character:", R[0])

#print the last character

print("Last Character:", R[-1])
#print the first 5 character

print("First 5 Character:", R[5])
#print the last 11 character

print("Last 11 Character:", R[-11])
#print the string in revers

print("Reverse String:", R[::-1])

start = R.index("python")
print("word python:", R[start:start + 6])

# String methods
strM = "Python beginner tutorial"
print("Uppercase: ", strM.upper())
print("Lowercase:", strM.lower())
print("Capitalized :", strM.capitalize())
print("Count of t: ", strM.count('t'))
print("Replaced: ",strM.replace("python", "“Machine Learning"))
#Tuples
tup1=(10,20,30)
tup2= (40,50,60)
t_combine= tup1+ tup2
print("t_combine=", t_combine)
print("repeart* 3" ,t_combine * 3)
print("acces 3 elememt :" ,t_combine[2])
print("acces last 3 elememt :" ,t_combine[:3])

