file = open('yua.txt', 'r')
print("Reading first line...")
print(file.readline())
file.close
file = open('yua.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close
file = open('yua.txt', 'r')
print("Looping through lines")
for line in file:
    print(line)
file.close