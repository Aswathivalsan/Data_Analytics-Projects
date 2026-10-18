age_list =[24,25,26,27,28]
print("age_list : ",age_list)

name_list = ["anu","ammu","appu","meenu","manu"]
print("name_list: ", name_list)

name_list.append("yazhini")
print("append: ",name_list)

age_list.insert(2,30)
print("Insert: ",age_list)

age_list.pop(-1)
print("Pop : ",age_list)

age_list.extend([29,30,26])
print("Extend : ",age_list)

age_list.sort(reverse=True)
print("Descending Order: ",age_list)

print("Maximum Age: ",max(age_list))
print("minimum Age: ", min(age_list))
print("Sum of all Ages: ", sum(age_list))

'''Accessing List Elements'''

print("First Elements: ", age_list[0])

print("Last Elements: ", age_list[-1])

print("Index 2 to 4", age_list[2:5])

name_list.reverse()
print("Reverse order of name_list: " ,name_list)

student_mark= {
    "john": 65,
    "sona": 87,
    "asw" : 95,
    "abi" : 77,
    "nila" : 58
    }
print("student_mark :" ,student_mark)

print("Access the mark of student: ", student_mark["asw"])
student_mark["Janani"] = 80
print("Add student : ", student_mark)

student_mark["abi"]= 82
print("Update the mark of abi: ",student_mark)

student_mark.keys()
print("Keysf the dictionary : ", student_mark)

student_mark.values()
print(" values of the dictionary :",student_mark)

student_mark.items()
print(" Items of the dictionary :",student_mark)

my_set= {'a','e','i','o','u','a','a','i'}
print("my_set: ",my_set)
print(" Explanation A set stores only unique values. Duplicate values are automatically removed. Therefore, only five vowels are displayed.")

'''my_set[4]='s'
print(my_set)'''

print(" Sets are unordered collections of unique elements.Sets do not support indexing. Therefore, we cannot change an element using my_set[4]. This code raises a TypeError")

set1= {1, 3, 5, 7, 9}
print("set1: " ,set1)
set2= {2, 3, 5, 8, 10}
print("set2: ",set2)


print("Union " ,set1.union(set2))
print("Intersection ",set.intersection(set2))

score= int(input("Enter your score(0 to 10) :") )    
if score < 0 or score > 10:
    print("Invalid score! Enter a score between 0 and 10.")
elif score > 7:
    print("Performance Category: Above Average")
    print("Excellent! Keep up the good work.")
elif score >= 4:
    print("Performance Category: Average")
    print("Good effort! Keep practising to improve.")
else:
    print("Performance Category: Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")
