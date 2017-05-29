import os

def rename_file():
	file_list = os.listdir("/Users/ejchung/ej/programming_foundations_with_python/prank")
	saved_path = os.getcwd()
	print("Current working directory is: " + saved_path)
	for file in file_list:
		print(file)

rename_file()