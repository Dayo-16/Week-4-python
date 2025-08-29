# File Read & Write Challenge

input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the file to write to: ")

try:
    with open(input_file, "r") as file:
        content = file.read()

    modified_content = content.upper()

    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"✅ Modified content written to {output_file}")

except FileNotFoundError:
    print("⚠️ The file you entered does not exist.")
except PermissionError:
    print("⚠️ Error: You don’t have permission to read or write this file.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
