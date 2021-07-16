# Kalen 7/12/2021

helloList = ["hello"]
helloList*=50

for i in range(len(helloList)//2):
    helloList[(i*2)+1] += "!"

for i, e in enumerate(helloList):
    if "!" in e:
        helloList[i] = e[0] + "i" + "!"

print(helloList)