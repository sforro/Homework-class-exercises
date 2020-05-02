numbers = []
count = 0
while True:
    if count >= 3:
        break
    number = input("Enter a number: ")
    try:
        number = int(number)
    except:
        print("That was not a number")
        continue
    # We have a proper number
    numbers.append(number)
    count += 1
numbers.sort()
# check if not triangle
if numbers[0] + numbers[1] < numbers[2]:
    print("it's not a triangle")
    exit()
# check if equilateral
if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
    print(" it is an equilateral triangle")
# check if isosels
if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
    print("isosceles")
# check if right angle
if numbers[2] ** 2 == numbers[0] ** 2 + numbers[1] ** 2:
    print("right angle")
# check if obtue
if numbers[2] ** 2 > numbers[0] ** 2 + numbers[1] ** 2:
    print("obtuse angle")
if numbers[2] ** 2 < numbers[0] ** 2 + numbers[1] ** 2:
    print("acute angle")

# calculate the semi perimeter
sp = numbers[0] + numbers[1] + numbers[2] / 2

# calculate area
area = (sp * (sp - numbers[0]) * (sp - numbers[1]) * (sp - numbers[2])) ** 0.5
print("The area of the triangle is %0.2f" % area)
