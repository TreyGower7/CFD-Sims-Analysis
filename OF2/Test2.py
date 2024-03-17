import re

# Input string
input_string = "arc 8 9 ( 9.23880e-01 3.82683e-01 -5.00000e-02)"

# Pattern to match 'arc 8 9'
pattern = r'arc 8 9'

# Replacement values
value1 = 333
value2 = 333

# Perform the replacement using re.search()
match = re.search(pattern, input_string)
if match:
    # Replace the matched pattern with the new values
    output_string = input_string[:match.start()] + f'arc 8 9 ( {value1:.5e} {value2:.5e} -5.00000e-02)' + input_string[match.end():]
    print(output_string)
else:
    print("Pattern 'arc 8 9' not found in the input string.")