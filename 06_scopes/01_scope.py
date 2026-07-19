# 1. Global Scope (The House Garden)
garden_tree = "Mango Tree"
gold_coins = 100

def living_room():
    # 2. Enclosing Scope (The Shared Living Room)
    tv_channel = "Sports"
    
    def my_bedroom():
        # 3. Local Scope (Your Private Bedroom)
        secret_diary = "Private thoughts"
        
        print("--- Inside Bedroom ---")
        print("Local secret:", secret_diary)
        print("Enclosing TV channel:", tv_channel)
        print("Global tree:", garden_tree)
        
    my_bedroom()

print("--- Running living_room() ---")
living_room()


# 4. Modifying Scope variables with 'global' and 'nonlocal'

def spend_coins():
    global gold_coins
    gold_coins -= 20

print("\n--- Testing 'global' ---")
print("Coins before spending:", gold_coins)
spend_coins()
print("Coins after spending:", gold_coins)


def home_library():
    book_genre = "Mystery"
    
    def inner_room():
        nonlocal book_genre
        book_genre = "Sci-Fi"
        
    print("\n--- Testing 'nonlocal' ---")
    print("Book genre before change:", book_genre)
    inner_room()
    print("Book genre after change:", book_genre)

home_library()
