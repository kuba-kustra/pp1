def foo(tab):
    r = 0
    for x in tab:
        if isinstance(x, list):
            r += foo(x)
        else:
            r += x
    return r


tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
print(f'''SUMA: {foo(tab)}''')
