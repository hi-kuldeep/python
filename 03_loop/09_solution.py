items = ["apple" , "banana" , "orange" , "apple" , "mango"]

# APPROACH 1: Inefficient Approach
# Time Complexity: O(n^2) - because list.count() scans the entire list of size n, and we repeat this for up to n elements.
# Space Complexity: O(1) - no extra data structures are used.
# Note: The check must be strictly > 1, as any element in the list will have a count of at least 1.
for item in items:
    if items.count(item) > 1:
        print(item + " is duplicated")
        break

# APPROACH 2: Optimized Approach (Recommended)
# Time Complexity: O(n) - set lookup and insertion take O(1) time on average, scanning the list once.
# Space Complexity: O(n) - uses a set to store unique elements in memory.
unique_item = set()
for item in items:
    if item in unique_item:
        print(item + " is duplicated")
        break
    unique_item.add(item)