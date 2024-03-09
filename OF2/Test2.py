import re

# Define the file path



# Function to replace values in the blockMeshDict file
def replace_values():
    with open("/Users/treygower/Desktop/blockMeshDict1.example", "r") as file:
            data = file.readlines()
    print(data)
    block = ""
    new_values = ""
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


        #Finds Pattern for a given block
        for i in range(len(data)):
            if f'   // block {block}\n' == data[i]:
                print('Current Block Data:\n' + data[i+1])
                print(f'Enter desired grading along x or y for block {block}')
                x = input('x grade: ')
                y = input('y grade: ')
                new_values = f'{x} {y} {1}'
                grade_pattern = r'\(\s*(\d+)\s+(\d+)\s+(\d+)\s*\)'
                # Search for the pattern in the line
                match = re.search(grade_pattern, data[i+1])
                dim = match.groups()
                pat = f'({dim[0]} {dim[1]} 1)'
                break
        # Go through the file again and replace all matching patterns
        for j in range(len(data)):
            data[j] = re.sub(pat, new_values, data[j])


            

    # Write the modified content back to the file
    with open("/Users/treygower/Desktop/blockMeshDict123_updated.txt", "w") as file:
        file.writelines(data)

# Call the function
replace_values()
