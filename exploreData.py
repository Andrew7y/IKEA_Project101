# Let's first inspect the file to see what kind of data it contains.
file_path = 'C:/Users/ROG/Downloads/products_dict.p'

# Since the file has a .p extension, it might be a Python pickle file.
# Let's try loading it to check its contents.
import pickle
import json

# Attempt to load the pickle file and check its content
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# แสดงผล JSON ในรูปแบบที่สวยงาม
pretty_json = json.dumps(data, indent=4)
print(pretty_json)