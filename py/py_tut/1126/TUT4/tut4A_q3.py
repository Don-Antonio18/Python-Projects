def fun(a,b):
    if ( b ==0):
        return 0
    if (b % 2 == 0):
        return fun(a + a, b // 2)
    return fun (a + a, b //2 ) + a

print (fun(10,10))