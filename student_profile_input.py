def student_profile_input():
    name = input("What is your name?")
    age = input("How old are you?")
    career_goal = input("What is your career goal?")
    tech = ("What is your favorite technology?")
    city = input("What city do you live in?")
    school = input("What school do you attend?")

    profile = {
        "name": name,
        "age": age,
        "career_goal": career_goal,
        "tech": tech,
        "school": school
    }

    return profile

student = student_profile_input()
print(f"Hello, {student['name']}")

first_name = "Stacks"
last_name = "Codex"
age = 38
career_goal = "Full Stack Dev"
tech = "AWS"
city = "PHX"
school = "Maestro University"
print(first_name + " " + last_name)

print(student["career_goal"])
print("_" * 30)
print("STUDENT PROFILE")
print("_" * 30)
print(f"Name: {first_name}")
print(f"Age: {age}")
print(f"Career Goal: {career_goal}")
print(f"Favorite Tech: {tech}")
print(f"Hometown: {city}")
print(f"University: {school}")
print("_" * 30)


print("Hello", first_name)



