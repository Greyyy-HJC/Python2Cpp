from ctypes import cdll

# Load the shared library
lib = cdll.LoadLibrary("./example.so")
# Call the add function
result = lib.add(2, 3)
print(f"The result is: {result}")  # The result is: 5
