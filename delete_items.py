import os
import shutil

# list of items to delete
elements_to_remove = ['__pycache__', 'data/50000 Sales Records.csv', 'orders', 'statistics']

for element in elements_to_remove:
    try:
        if os.path.exists(element):
            if os.path.isfile(element):
                os.remove(element)
            elif os.path.isdir(element):
                shutil.rmtree(element)
        else:
            print(f"{element} doesn't exist")
    except Exception as e:
        print(f"Error to remove {element}: {str(e)}")

