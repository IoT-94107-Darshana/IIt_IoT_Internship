import geometry
def function1():
    pi=3.14
    radius=float(input("enter value of radius:"))
    lenth=float(input("enetr value of lenth:"))
    width=float(input("enter value of width:"))
    print("area of circle:",geometry.area_of_circle(pi,radius))
    print("area of rectangle:",geometry.area_of_rectangle(lenth,width))
function1()