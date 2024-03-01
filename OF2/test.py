import numpy as np
R = 1
r = 1
H = 3
Lf = 3
Lw = 3
n= 64

vertices = np.zeros((n,3))
angle_increment = 2 * np.pi / (n//8)

for i in range((n//4)-1):
    angle = i * angle_increment
    if i <= 8:
        for j in range(3):
            if j == 0:
                vertices[i, j] = r* np.cos(angle)
            if j == 1:
                vertices[i, j] = r* np.sin(angle)
            else:
                vertices[i, j] = -.5
    else:
        for j in range(3):
            if j == 0:
                vertices[i, j] = (r+R)* np.cos(angle)
            if j == 1:
                vertices[i, j] = (r+R)* np.sin(angle)
            else:
                vertices[i, j] = -.5

for i in range(31,(n//4)-1, -1):
    for j in range(3):
        vertices[i, j] = (r+R+Lw) + vertices[i, j]
        if j == 1:
            vertices[i, j] = vertices[i, j]
        else:
            vertices[i, j] = -.5
    

print(vertices)