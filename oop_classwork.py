# class Line:
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         formular = ((x2 -x1)**2) + ((y2 - y1)**2)
#         dist = formular**0.5
#         return dist
    
#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         formular = (y2 - y1) / (x2 - x1)
#         slop = formular
#         return slop
        
    

# line1 = Line((3,2), (8,10))
# # print(line1.distance())
# # print(line1.slope())






# class Line:
#     def __init__(self, coor1, coor2):
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2

#     def distance(self):
#         formular = ((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)
#         dist = formular**0.5
#         return dist
    
#     def slope(self):
#         formular = (self.y2 - self.y1) / (self.x2 - self.x1)
#         slop = formular
#         return slop
        

# line1 = Line((3,2), (8,10))
# print(line1.distance())
# print(line1.slope())


# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume (self):
#         vol = 3.142 * ((self.radius)**2) * self.height
#         return round(vol, 2)

#     def surface_area(self):
#         sur_area = (2 * 3.142 * ((self.radius)**2)) + (2 * 3.142 * self.radius * self.height)
#         return round(sur_area, 2)
    

    
# line2 = Cylinder(2, 3)
# print(line2.volume())
# print(line2.surface_area())


