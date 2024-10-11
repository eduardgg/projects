
def f(n, v, o, t):

    # o són els parèntesis oberts
    # t són els parèntesis tancats
    # n és el nombre dels parells de parèntesis
    # v és la string de parèntesis

    if t == n:
        mystring = ""
        for x in v:
            mystring += x
        print(mystring)
        return
    if o < n:            
        v[o+t] = '('
        f(n, v, o+1, t)
    if o > t:
        v[o+t] = ')'
        f(n, v, o, t+1)
    return


f(5, ['']*2*5, 0, 0)