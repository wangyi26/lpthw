from sys import argv

script,fliename = argv

txt = open(fliename)

print(f"Here's your life {fliename}:")
print(txt.read())

print("Type the fliename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())