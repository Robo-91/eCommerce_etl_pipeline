import os
from pathlib import Path

folder_path = Path("C:/Users/Robert/OneDrive/Desktop/S_Data")

print(folder_path)
print(os.listdir(folder_path))

def hello():
    return 'Hello World'