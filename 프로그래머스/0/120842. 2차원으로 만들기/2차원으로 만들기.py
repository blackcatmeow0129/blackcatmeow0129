newlist=[]
def solution(num_list, n):
    for i in range(len(num_list)//n):
        newlist.append(num_list[i*n:i*n+n])
    return newlist