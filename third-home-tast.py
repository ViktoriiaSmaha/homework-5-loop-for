N = int(input("Enter your number"))

for i in range(N):
    num_of_stars = N - i
    num_of_spaces = i
    print(num_of_spaces * " " + num_of_stars * "*")

