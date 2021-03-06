with open('input.txt', 'r') as my_file:
    # Some action performed with the file, the read() method explained later.
    print(my_file.read(), '\n')


# Open the file input1.txt in read mode using the with statement
with open('input.txt', 'r') as file:
    print(file.read())


outfile = open('outfile.txt', 'w') # opening the file in write mode (using `w` argument)
outfile.write('Hello World')  # writing to the file, the write() method is explained later.
outfile.close()
