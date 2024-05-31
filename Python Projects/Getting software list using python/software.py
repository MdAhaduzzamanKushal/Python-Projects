def process_bat_file(file_path, output_file):
    try:
        with open(file_path, 'r') as file:
            with open(output_file, 'w') as out_file:
                lines = file.readlines()
                for line in lines:
                    # Find the last index of '\'
                    last_backslash_index = line.rfind('\\')
                    if last_backslash_index != -1:  # If '\' is found
                        out_file.write(line[last_backslash_index + 1:].strip() + '\n')  # Write to output file
    except FileNotFoundError:
        print("File not found.")

# Example usage: Provide the path to the batch file and the output file
batch_file_path = r"F:\Security mind pro\Assignment\Python Projects\Getting software list using python\soft_list.bat"
output_file_path = "Final.txt"
process_bat_file(batch_file_path, output_file_path)
