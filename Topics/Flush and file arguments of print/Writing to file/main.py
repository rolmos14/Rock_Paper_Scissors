f_name = "test.txt"
my_string = "A string to be written to a file!"

with open(f_name, "w") as file:
    print(my_string, file=file)
