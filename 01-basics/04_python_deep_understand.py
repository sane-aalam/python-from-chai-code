# Variables are containers for storing data values.
student_collge_name = "ANA"
student_user_id = 19191919
student_full_name = "John"
student_enroll_course = "BTech"
student_mostly_read_subject = "OS'DBMS''DSA'"
student_address = "Rampur'243501'"
student_webstie = "wwww.github.com/johnEl"
student_local_address = "Fateh Ganj,Civil Line"
student_father_name = "JohnMark"
student_youtube_channel = "AlpahTech"
#list
student_freinds_list = ["Alice", "Emma", "Michael", "Sophia"]
# Dictionary Items
student_skills = {
    "John": {
        "Programming": 90,
        "Problem Solving": 85,
        "Communication": 80,
        "Time Management": 75,
        "Leadership": 70,
    },
    "Alice": {
        "Programming": 85,
        "Problem Solving": 80,
        "Communication": 85,
        "Time Management": 90,
        "Leadership": 75,
    },
    "Emma": {
        "Programming": 80,
        "Problem Solving": 90,
        "Communication": 85,
        "Time Management": 80,
        "Leadership": 80,
    },
    "Michael": {
        "Programming": 85,
        "Problem Solving": 80,
        "Communication": 75,
        "Time Management": 85,
        "Leadership": 70,
    },
    "Sophia": {
        "Programming": 80,
        "Problem Solving": 85,
        "Communication": 90,
        "Time Management": 85,
        "Leadership": 75,
    },
}

print(student_collge_name)
print(student_address)
print(student_father_name)
print(student_freinds_list)
print(student_youtube_channel)
print(student_local_address)

john_data = student_skills["John"]
Alice_data = student_skills["Alice"]
Emaa_data = student_skills["Emma"]

print(john_data)
print(Alice_data)
print(Emaa_data)

print(john_data["Problem Solving"])
print(Alice_data["Time Management"])
print(Emaa_data["Leadership"])

if student_skills["Michael"]["Time Management"] < 84:
    print("you are good in time management")
elif student_skills["Michael"]["Communication"] < 100:
    print("you are goog into communication skills!")
else:
    print("you are not good any skills")

print("That's great, you are good in python")