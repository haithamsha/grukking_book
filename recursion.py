def count_down(i):
    print(i)
    #base case
    if i <= 1:
        return
    else:
        #recursive case
        count_down(i-1)


# count_down(10)

#factorial
def fac(i):
    #base case
    if(i == 1):
        return 1
    else:
        return i * fac(i -1)


print(fac(3))     