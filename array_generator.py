import numpy as np
import random
import string
import os

# Generate an array of 100 random words
random_words_array = np.array([''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))) for _ in range(1000000)])

# Get the absolute path of the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Save the array in a binary file in the same folder as the script
file_path = os.path.join(current_directory, 'random_words_array.npy')
np.save(file_path, random_words_array)

print(f"File saved in: {file_path}")
