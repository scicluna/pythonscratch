# name = input("What's your name? ")

# to write a file
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# to write a file
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
