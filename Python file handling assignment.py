import os

def read_and_write_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Check if the file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The file '{input_file}' does not exist.")

        # Read the content of the file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask for the output file name
        output_file = input("Enter the name of the file to write to: ")

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: You do not have permission to read or write to the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()