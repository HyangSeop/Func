def root_ex(a,b,c):
    x_1 =( -b + (b**2-4*a*c)**0.5)/(2*a)
    x_2 =( -b - (b**2-4*a*c)**0.5)/(2*a)

    return x_1, x_2


a = int(input("이차항의 계수"))
b = int(input("일차항의 계수"))
c = int(input("상수항"))

x = root_ex(a,b,c)
print(x)

