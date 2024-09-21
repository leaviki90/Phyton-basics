#9.	Fruit or Vegetable
# Read a product name entered by the user
product = input("Enter a product name: ")

# Check the product type using pattern matching
match product:
    # Case for fruits
    case "banana" | "apple" | "kiwi" | "cherry" | "lemon" | "grapes":
        print("fruit")
    # Case for vegetables
    case "tomato" | "cucumber" | "pepper" | "carrot":
        print("vegetable")
    # Default case for unknown products
    case _:
        print("unknown")

# Old code for reference
# product = input()
# if product in ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]:
#     print("fruit")
# elif product in ["tomato", "cucumber", "pepper", "carrot"]:
#     print("vegetable")
# else:
#     print("unknown")



