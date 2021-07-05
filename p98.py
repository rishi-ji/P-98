def swapFileData():
    file1 = input("Enter File Name: ")
    file2 = input("Enter File Name: ")

    
    with open(file, 'r') as a:
    dataa = a.read()

	with open(file1, 'r') as b:
    datab = b.read()

    with open(file, 'w') as a:
    a.write(datab)

    with open(file1, 'w') as b:
    b.write(dataa)

swapFileData()
