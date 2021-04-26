num = input("Please enter positive number:")

while not num.isdigit() :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    num = input("Please enter positive number:")

armstrong = []
for i in num:
    armstrong.append(int(i)**len(num))
if sum(armstrong) == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
