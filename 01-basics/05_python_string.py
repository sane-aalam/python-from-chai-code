student_full_name = "John"
print(student_full_name)

print(student_full_name[0])
print(student_full_name[1])
print(len(student_full_name))


# access string char one by one 
s = "MyNameIsJohn"

student_name_first_char = s[0]
student_name_last_char = s[-1]
total_len = len(s)/2
# len_type = type,(total_len)
# print(len_type)
print(total_len)
# convert float to int
total_len =int(total_len)
print(total_len)
student_middle_char = s[total_len]
print(student_middle_char)


# string method
s = s.capitalize()
print(s)
# convert into uppercase
s = s.upper()
print(s)
# convert into lowercase
s = s.lower()
print(s)
# replace the old char -> new char 
s = s.replace("n","D")
print(s)

# find char present at index number
findTarget = s.find("D")
print(findTarget)

# use for loop
for ch in s:
    print(ch)

# you will learn lot of, during the course