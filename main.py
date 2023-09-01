def create_text_file(file_name, content):
    try:
        with open(file_name, "w") as file:
            file.write(content)
    except Exception as e:
        pass

def code_to_binary():
    try:
        with open("code.txt", "r", encoding='utf-8') as file:
            normal_code = file.read()

        if not normal_code.strip():
            print("Put your code into normal_code.txt and restart the program.")
            input()
            quit()
            return None

        binary_code = ''.join(format(ord(char), '08b') for char in normal_code)

        binary_code_with_spaces = ' '.join([binary_code[i:i+8] for i in range(0, len(binary_code), 8)])
        modified_binary = binary_code_with_spaces.replace("11", "+")

        create_text_file('binary_code.txt', modified_binary)

        return modified_binary
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

a = code_to_binary()

if a is not None:
    with open("output.txt", "w") as file:
        file.write(f"exec(''.join(chr(int(b.replace('+', '11'), 2)) for b in '{a}'.split()))")

print('Payload created successfully, get the code in output.txt')
input()
