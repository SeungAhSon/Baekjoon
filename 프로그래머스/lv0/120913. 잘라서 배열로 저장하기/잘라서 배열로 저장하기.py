def solution(my_str, n):
    if len(my_str)%n>0:
        return [my_str[i*n:(i+1)*n] for i in range(0, len(my_str)//n)]+[my_str[-(len(my_str)%n):len(my_str)]]
    else:
        return [my_str[i*n:(i+1)*n] for i in range(0, len(my_str)//n)]