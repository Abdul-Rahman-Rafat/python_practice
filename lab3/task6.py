import random, os, csv

def Random_Data_Generator():
    n = int(input("Enter number of random values you need: "))
    s, e = map(int, input("Enter the start and end of the random values like (1,100): ").split(","))

    file_exists = os.path.isfile("random_numbers.csv")

    with open("random_numbers.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["index", "value"])

        for i in range(1, n + 1):
            val = random.randint(s, e)
            writer.writerow([i, val])

    with open("random_numbers.csv", "r") as file:
        print(file.read())


