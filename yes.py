def write_to_file(filename):
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Initial input written to file.")

def append_to_file(filename):
    additional_input = input("Enter additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print("Additional input appended to file.")

def read_file(filename):
    print("\nFinal content of the file:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# Main program flow
filename = 'output.txt'
write_to_file(filename)
append_to_file(filename)
read_file(filename)
