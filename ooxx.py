n = 3

map = []
for i in range(n):
    map.append([])
    for k in range(n):
        map[i].append(" ")


while True:
    ox = input("O/X: ")
    where = input("where(1-9): ")
    where = int(where)
    column = int((where / 3)-0.1)
    row = (where % 3)-1
    try:
        map[column][row] = ox
    except:
        print("try again!")
        
    for i in map:
        print(i)