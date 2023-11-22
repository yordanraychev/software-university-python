file_path = input().split("\\")
file_name_and_extension = file_path[-1]
filename, extension = file_name_and_extension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
