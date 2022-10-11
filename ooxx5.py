n = int(input("邊長: "))

map = []
for i in range(n):
    map.append([])
    for k in range(n):
        map[i].append(" ")

win = False

def draw(sign,where):
    where = int(where)
    column = int((where / n)-0.0000001)
    row = (where % n)-1
    map[column][row] = sign
    return map

def draw_map(map=map):
    for i in range(len(map)):
        print(map[i])

draw_map()

while not win:
    ox = input("O/X: ")
    where = input("where(1-{}): ".format(n*n))
    try:
        draw(ox,where)
    except:
        print("*******try again!********")
        
    draw_map()
        
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
                win = True
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
                win = True
                break
            
    # win main sqare
    
    if map[0][0] != " ":
        tmpnum = map[0][0]
        a = 0
        for i in range(n):
            if map[i][i] != tmpnum:
                break
            else:
                a+=1
        if a == n:
            print("***********{} win main!************".format(tmpnum))
            win = True
            
        

    # win sub sqare
    
    if map[0][-1] != " ":
        tmpnum = map[0][-1]
        a = 0
        for i in range(n):
            if map[i][-i-1] != tmpnum:
                break
            else:
                a+=1
        if a == n:
            print("***********{} win sub!************".format(tmpnum))
            win = True
