import os
from string import digits

def rename_files():
	# get file names from the folder
	file_list = os.listdir("/Users/ejchung/ej/programming_foundations_with_python/prank")
	# save current path
	saved_path = os.getcwd()
	# change current file path
	os.chdir("/Users/ejchung/ej/programming_foundations_with_python/prank")

	remove_digits = str.maketrans('','', digits)
	# for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(remove_digits))
	# change current path back to original
	os.chdir(saved_path)

rename_files()