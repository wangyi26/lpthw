from sys import argv

script, wangyi = argv
prompt = '>'

print(f"Hi {wangyi},I'm the [script] script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me [wangyi]?")
likes = input(prompt)

print(f"Where do you live {wangyi}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright,so you said {likes} about liking me.
You live in {lives}.Npt sure where that is.
And you have a (computer) computer.Nice
""")
