N = int(input("Enter your number"))

for i in range(N):
    number_of_stars = i + 1
    number_of_spaces = N - i
    print(number_of_spaces * " " + number_of_stars * "*")