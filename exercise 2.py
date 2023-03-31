
#exercise2
file = open("C:\\Users\\ASUS\\Desktop\\text.txt", "r")

def revword(word):
    word=word[::-1].lower()
    return word
def countword(file):
    lst=[]
    for line in file:
        lst.append(line.rstrip().split())
    for i in range(1,len(lst)):
        lst[0][0]=lst[0][0].lower()
        for j in range(len(lst[i])):
            lst[i][j]=revword(lst[i][j])
    counter=0
    for k in lst:
        for z in range(len(k)):
            if k[z]==lst[0][0]:
                counter+=1
    return lst[0][0],counter

print(countword(file))

