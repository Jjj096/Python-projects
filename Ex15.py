from sys import argv

script, ex15_sample = argv

txt = open(ex15_sample)

print(f"Here's your file du:")
print(txt.read())

print("Type the ex15_sample.txt again:")
file_again = input(" text, dumb ")

txt_again = open(file_again)

print(txt_again.read())
