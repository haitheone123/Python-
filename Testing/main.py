#bai 10
import math
a=float(input())
triangle_area = ((a**2)*math.sqrt(3))/4
triangle_half_perimeter = (3*a)/2
circle_area = ((triangle_area / triangle_half_perimeter)**2)*3.14
remainder_area = triangle_area - circle_area
print(round(remainder_area,2)

#bai 11
import math
a=float(input())
triangle_area = ((a**2)*math.sqrt(3))/4
circle_area = ((((a**3)/(4*triangle_area))**2)*3.14)
remainder_area = circle_area - triangle_area
print(round(remainder_area,2))

