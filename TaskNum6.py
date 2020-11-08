def sqrtP(a,p,eps) :
    x = a
    temp = 1 / p * ((p - 1) * x + a / power(x,p - 1))
    n = 1
    while abs(temp - x) > eps  :
        x = temp
        temp = 1 / p * ((p - 1) * x + a / power(x,p - 1))
        n += 1
    return x, n
a = float(input('Введите число : '))
p = int(input('Введите степень : '))
eps = 0.1
for i in range(5) :
    eps /= 10.
    num, n = sqrtP(a,p,eps)
    print('{:f} {:f} {}'.format(eps,num,n))
