# Cau 1
name = 'Tran Thanh Hiep'
for i in name:
    print(i, end=' ')

print()

# Cau 2
sum_odd = 0
for i in range(1, 10):
    if i % 2 != 0:
        print(i, end=' ')
        sum_odd += i
# Cau 3a
print(sum_odd)

print()

# Cau 3b
sum_1_to_6 = 0
for i in range(1, 6):
    sum_1_to_6 += i
print(sum_1_to_6)

print()

# Cau 4
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k, v in mydict.items():
    print(k, end=" ")
print()
for k, v in mydict.items():
    print(v, end=" ")
print()
for k, v in mydict.items():
    print(f"{k}: {v}")

print()

# Cau 5
courses = [131, 141, 142, 212]
names = ['Maths', 'Physics', 'Chem', 'Bio']
for i in range(len(courses)):
    print(f'{names[i]}: {courses[i]}')

print()

# Cau 6
count = 0
my_str = 'jabbawocky'
vowels = ['u', 'e', 'o', 'a', 'i']
for i in range(len(my_str)):
    for vowel in vowels:
        if my_str[i] == vowel:
            count += 1
print(len(my_str) - count)

print()

# Cau 7
while True:
    try:
        a = int(input("Enter a number: "))
        if a in range(-2, 3):
            break
        else:
            print('Out of range. Try again')
    except:
        print("That's not a number")
try:
    print(10 / a)
except:
    print("Can’t divided by zero")

print()

# Cau 8
ages = [23, 10, 80]
names = ["Hoa", "Lam", "Nam"]
people = list(zip(ages, names))
people.sort(key=lambda x: x[0])
print(people)

print()

# Cau 9
f = open('firstname.txt', 'r')
print(f.read())
