import sys

def format_output(output_text):
    result_text = ''
    line_text = ''
    count_text = 0
    for letter in output_text:
        line_text += letter
        count_text += 1
        if count_text == 5:
            result_text += line_text + ' '
            line_text = ''
            count_text = 0
    if line_text:
        result_text += line_text + '\n'
    return result_text

def encode_text(plain_text, shift_value):
    letters = [char.upper() for char in plain_text if char.isalpha()]
    encoded = []
    for char in letters:
        ascii_val = ord(char)
        new_val = ascii_val + shift_value
        if new_val > ord('Z'):
            final_val = (new_val - ord('Z')) % 26
            if final_val == 0:
                final_val = 26
            new_val = final_val + ord('A') - 1
        encoded.append(chr(new_val))
    return format_output(''.join(encoded))

args = sys.argv
if len(args) < 2:
    print("Please provide a shift value as a command line argument.")
    sys.exit(1)

shift_value = int(args[1])
for line_text in sys.stdin:
    result_text = encode_text(line_text.strip(), shift_value)
    sys.stdout.write(result_text)