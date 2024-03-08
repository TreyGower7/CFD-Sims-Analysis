import re

def grading(lines):
    #preserve the template
    template = lines
    blocks_change = [0,1,2,5,6,7,8,9,10,17,18,19]
    patterns = [
    r"\b(10 20 1)\b",
    r"\b(30 20 1)\b",  
    r"\b(20 30 1)\b",
    r"\b(30 30 1)\b",
    r"\b(15 30 1)\b"   
    ]
    print('Once done editing mesh grading save by typing: done or d')
    block = ""
    while block != 'done' and block != 'd':
        block = ""
        while not block.isdigit() or int(block) >= 20:
            block = input("Input the block to change grading of: ")
            if block == 'done' or block == 'd':
                break

            if not block.isdigit() or int(block) >= 20:
                print("Invalid block number. Please enter an integer less than 20.")
                continue

        if block == 'done' or block == 'd':
            break

        j = int(block)

        for i, line in enumerate(template):
            if f'   // block {j}' in line:
                print(lines[i+1])
                print(f'Enter grading along x or y for block {j}')
                x = input('x grade: ')
                y = input('y grade: ')
                formatted_grade = f'{x} {y} {1}'
                for pattern in patterns:
                    compiled_pattern = re.compile(pattern)  # Compile the pattern for efficiency
                    match = compiled_pattern.search(template[i+1])  # Check if the pattern is in the line
                    if match:
                        break

                # Replace every instance of the pattern
                for k, line in enumerate(template):
                    match = re.search(compiled_pattern, template[k])
                    if match:
                        lines[k] = compiled_pattern.sub(formatted_grade, line)
                        print(f'Grading block surrounding blocks')

    return lines


yorn = None
while yorn != 'y' or yorn != 'n':
    yorn = input('Would you like to change Resolution? (y/n): ')
    if yorn == 'y':
        with open("/Users/treygower/Desktop/blockMeshDict1.example", "r") as file:
            lines = file.readlines()
        graded = grading(lines)
        break
    if yorn == 'n':
        break
    else: 
        print('enter y or n')

with open("/Users/treygower/Desktop/blockMeshDict123_updated.txt", "w") as file:
        file.writelines(graded)