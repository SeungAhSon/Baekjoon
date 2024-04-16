def solution(my_string):
    my_string = "".join([i if i.isdigit() else " " for i in my_string]).split()
    return sum([int(i) for i in my_string])