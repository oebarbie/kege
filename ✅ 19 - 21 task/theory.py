def f(a,b,m):
    if a+b>=55: return m%2==0
    if m==0: return 0
    h = [f(a+2,b,m-1),f(a,b+2,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

# при любом ходе учитывается и так
# при предыдущем проигрышном all -> any

# '!=' 
# '==' если выигрывает 1 игрок
