# Example 1: Manual File Closing with try-finally
# Ensures the file is always closed, even if an exception occurs inside try
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()


# Example 2: Pythonic Context Manager (with statement)
# Automatically handles opening and closing the file cleanly
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')
