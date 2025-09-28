#Area calculation of rectagle

rectangles=[(15,20),(3,5),(5,6)]
area=[]
r_area=[]
r_area_lamda=[(x,y,x*y) for (x,y) in rectangles]


for (x,y) in rectangles:
    area.append(x*y)
    r_area.append((x,y,x*y))

print(area)
print(r_area)
print(r_area_lamda)

#lamda