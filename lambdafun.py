#area of shapes

#area of square
area_square=lambda square_side:square_side*square_side
print("Area of square: ",area_square(5))

#area of rectangle
area_rec=lambda rec_length,rec_breadth: rec_length*rec_breadth
print("Area of rectangle: ",area_rec(10,20))

#area of triangle

tri_area=lambda tri_height,tri_breadth: 0.5*tri_height*tri_breadth
print("Area of triangle: ",tri_area(20,10))

#area of circle

circle_area=lambda radius:3.14*radius*radius
print("Area of circle: ",circle_area(4))

#area of pentagon

pent_area=lambda perimeter,height:0.5*perimeter*height
print("Area of pentagon: ",pent_area(50,40))

#area or hexagon

hex_area=lambda side:(3*1.732*side*side)/2
print(f"Area of hexagon: {hex_area(5):.2f}")