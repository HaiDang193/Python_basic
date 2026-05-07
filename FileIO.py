user_input = int(input("Nhap so: "))
with open("FileIO.txt" , "w") as file:
    for i in range(user_input):
        file.write(f"{user_input - i}\n")


numbers = []
with open("FileIO.txt" , "r") as file:
    numbers = file.read().split()

for i in range(len(numbers)):
    print(f"Line {i+1}: {numbers[i]}")