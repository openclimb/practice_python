

n=int(input())
q=int(input())

box_list= [[] for j in range(q+2)]
exist_box= [set() for j in range(2*(10**5)+1)]
# print(exist_box)
for i in range(q):
    query=list(map(int,input().split()))
    # print(box_list)
    if query[0] == 1:
        i=query[1]
        j=query[2]
        box_list[j].insert(0, i)
        exist_box[i].add(j)
        
    if query[0] == 2:
        i=query[1]
        print(*sorted(box_list[i]))
    
    if query[0] == 3:
        i=query[1]
        print(*sorted(exist_box[i]))
