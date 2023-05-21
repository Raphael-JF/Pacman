def fonction(x,y):
    if x % 2 == 0:
        x += 1
    if y % 2 == 1:
        y += 1
    return x,y
    
def reciproque(x, y):
    if x % 2 == 1:
        x -= 1
    if y % 2 == 0:
        y += 1
    return x, y