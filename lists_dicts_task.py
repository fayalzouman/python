skills = ["python", "java", "django"]
cv = {}
cv["name"] = input("What is your name?")
cv["age"] = int(input("What is your age?"))
cv["experience"] = input("How many years of experience do you have?")
cv["skills"] = {}

print("1." + skills[0] + " 2." + skills[1] + " 3." + skills[2])

askill = input("Pick a skill from above")
cv["askill"] = askill

aaskill = input("Pick another skill from above")
cv["aaskill"] = aaskill

if cv["age"] <= 25:
	print("Not applicable")