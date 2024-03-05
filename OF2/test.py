import numpy as np
R = .1
r = .5
H = 3
Lf = 3
Lw = 3
n= 64
vertices = np.zeros((n,3))
angle_increment = 2 * np.pi / (n//8)
for i in range((n//4)-1):
    angle = i * angle_increment
    if i < 8:
            vertices[i, 0] = r* np.cos(angle)
            vertices[i, 1] = r* np.sin(angle)
            vertices[i, 2] = -.5
    else:
            vertices[i, 0] = (r+R)* np.cos(angle)
            vertices[i, 1] = (r+R)* np.sin(angle)
            vertices[i, 2] = -.5

#for i in range(31,(n//4)-1, -1):
 #   for j in range(3):
  #      vertices[i, j] = (r+R+Lw) + vertices[i, j]
   #     if j == 1:
    #        vertices[i, j] = vertices[i, j]
     #   else:
      #      vertices[i, j] = -.5
    
print(len(vertices))
print(vertices)