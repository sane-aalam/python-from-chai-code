
mylist = ["apple", "banana", "cherry"] 
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])

# Traceback (most recent call last):Error
# print(mylist[19])
mylist[0] = "tea"
print(mylist)
# remove element into list
mylist.remove("tea")
print(mylist)

mylist.insert(1,"apple")
mylist.insert(0,"apple")
mylist.insert(3,"apple")
mylist.insert(4,"apple")
print(mylist)

# Methods in python(List)
#1.sort
#2.for into list
#3.copy list
#4.join list
#5.reverse

#1.sort
integer_array = [1,3,9191,1719,5]
integer_array.sort()
print(integer_array)

#2.for into list
for current_element in integer_array:
    if(current_element == 3):
        print(current_element,"is present into list")
    else:
        print(current_element,"is not present into list")

#3.copy list
new_integer_array = integer_array.copy()
print(new_integer_array)

#4.join list

student_boys = ["Rahul","Rahoon","Amit"]
student_girls = ["Adi","Adi2","Riti"]

student_management = student_boys + student_girls
print(student_management)

#5.reverse method
integer_array.reverse()
print(integer_array)

# how to write logic of reverse, using Two pointer Algo
new_array = [1,2,3,4,5]
start = 0
end = len(new_array) - 1
print(start,end)

print("Before reverse Logic",new_array) 

while start < end:
    temp = new_array[start]
    new_array[start] = new_array[end]
    new_array[end] = temp
    start = start + 1
    end = end - 1

print("After reverse Logic",new_array)