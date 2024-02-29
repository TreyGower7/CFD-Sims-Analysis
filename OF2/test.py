import math

def generate_cylinder_vertices(radius, height, num_segments):
    vertices = []

    # Add south pole vertex
    vertices.append([0, 0.5, -0.5])

    # Calculate angle increment
    angle_increment = 2 * math.pi / (num_segments//8)

    # Generate vertices around the circumference
    for i in range(num_segments//8):
        angle = i * angle_increment
        x = (radius/2) * math.cos(angle)
        y = (radius/2) * math.sin(angle)
        z = -0.5 
        vertices.append([x, y, z])

    # Add north pole vertex
    vertices.append([0, 0.5, -0.5 + height])

    return vertices

radius = 1
height = 1.0
num_segments = 64
cylinder_vertices = generate_cylinder_vertices(radius, height, num_segments)
print("Cylinder Vertices:")
for vertex in cylinder_vertices:
    print(vertex)