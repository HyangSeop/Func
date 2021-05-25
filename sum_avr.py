
def sum_nums(*args):
    s= 0
    for i in args:
        s+=i
        
    average = s/len(args)
    return s,average
    
a,b = sum_nums(10,50,30)
print('합계는',a,", 평균: ",b)
        