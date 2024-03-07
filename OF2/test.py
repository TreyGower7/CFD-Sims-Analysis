import re

# Sample input text, replace it with your actual input method
text = """
   // block 1
   hex (1 9 10 2 33 41 42 34) (10 20 1) simpleGrading ( 2.00000e+00  1.00000e+00 1.0)

   // block 2
   hex (2 10 11 3 34 42 43 35) (10 20 1) simpleGrading ( 2.00000e+00  1.00000e+00 1.0)

   ...
   
   // block 9
   hex (9 17 18 19 41 49 50 51) (30 30 1) simpleGrading ( 4.00000e+00  4.00000e+00 1.0)
"""
def grading(lines):
    blocks_change = [0,1,2,5,6,7,8,9,10,17,18, 19]
    pattern = [r"\b(10 20 1)\b", r"\b30 20 1)\b", r"\b(20 30 1)\b", r"\b(30 30 1)\b"]
    for j in range(len(blocks_change)):
        for i, line in enumerate(lines):
            k = i+1
            if f'   // block {j}' in line:
                if j <= 5:
                    pat = pattern[0]
                #Blocks 8 9 and 19
                if j == 7 or j == 11:
                    pat = pattern[1]
                #Blocks 10 and 17
                if j == 8 or j == 9:
                    pat = pattern[2]
                #Blocks 18
                if j == 10 or j == 6:
                    pat = pattern[3]
                
                match = re.search(pat, lines[k])
                if match:
                    print(f'Enter grading x, y, z for block {j}')
                    print(f"Current grading is {str(pat)}")
                    x = input('x grade: ')
                    y = input('y grade: ')
                    z = input('z grade: ')
                    formatted_grade = f'{x} {y} {z}'
                    formatted_text = re.sub(pat, formatted_grade, lines[k])
                    #print("Found:", match.group())
                    lines[k]= formatted_text
                    break
        '''
        for match in re.finditer(pattern, text):
            start_index = match.start()  # Start index of the match
            end_index = match.end()    # End index of the match
            print(f"Found '{match.group()}' from {start_index} to {end_index}")
        '''
    return lines


yorn = None
while yorn != 'y' or yorn != 'n':
    yorn = input('Would you like to change Resolution? (y/n): ')
    if yorn == 'y':
        with open("/Users/treygower/Desktop/blockMeshDict1.example", "r") as file:
            lines = file.readlines()
        graded = grading(lines)
        break1
    if yorn == 'n':
        break
    else: 
        print('enter y or n')

with open("/Users/treygower/Desktop/blockMeshDict123_updated.txt", "w") as file:
        file.writelines(graded)