n = 3

map = []
for i in range(n):
    map.append([])
    for k in range(n):
        map[i].append(" ")

def draw(sign,where):
    where = int(where)
    column = int((where / n)-0.0000001)
    row = (where % n)-1
    map[column][row] = sign
    return map

while True:
    ox = input("O/X: ")
    where = input("where(1-{}): ".format(n*n))
    try:
        draw(ox,where)
    except:
        print("*******try again!********")
        
    for i in map:
        print(i)
        
    # win column
    
    for i in range(n):
        tmpnum = map[i][0]
        if tmpnum == " ":
            continue
        else:
            for k in range(n):
                a = -1
                if map[i][k] != tmpnum:
                    break
                else:
                    a+=1
            if a == 0:
                print("***********{} win!************".format(tmpnum))
                break
            
            
    # win row
    
    for i in range(n):
        tmpnum = map[0][i]
        if tmpnum == " ":
            continue
        else:
            for k in range(n):
                a = -1
                if map[k][i] != tmpnum:
                    break
                else:
                    a+=1
            if a == 0:
                print("***********{} win!************".format(tmpnum))
                break
