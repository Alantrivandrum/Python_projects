name = input("What is your name")
year = input("What year were your born ? ")

print("Hello " + name + ", nice to meet you")
age = 2020 - int(year)

print("You are " + str(age) + " years old")

if(age < 18):
    print("You are under 18")
else:
    print("You are an adult")