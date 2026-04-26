# Ask for user's name
name = input("Whats your name? ") . strip() . title()

first, last = name.split(" ")

print(f"Hello, {last}")
