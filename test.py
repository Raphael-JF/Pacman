from classes.transition import transition_2bounds
a= []
b=11
for i in range(b):
    a.append(transition_2bounds(16,48,b,'linear',i,True,True))

print(a,a[5])