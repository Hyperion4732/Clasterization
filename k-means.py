f = open('/test1.txt')
elements = []
for line in f:
    elem = line.split()
    for i in range(len(elem)):
        elem[i] = int(elem[i])
    elements.append(elem)
print(elements)