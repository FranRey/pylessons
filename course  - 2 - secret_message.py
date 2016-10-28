import os

mypath = "./prank/"

def rename_files(path):
	# Get list of images
	image_filenames = os.listdir(path)

	#print(image_filenames)

	# Create translation tables for the renaming of the filename
	translation_table = str.maketrans("0123456789","          ")
	
	# Rename the files
	for image_filename in image_filenames:
		new_filename = image_filename.translate(translation_table).strip()
		# print("Renaming " + image_filename + " to " + new_filename)
		os.rename(path + image_filename, path + new_filename)

print("Decoding Secret Message")
rename_files(mypath)
print("Decoded!!")