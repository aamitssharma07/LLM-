import pandas as pd

# Read the Excel file and extract the grocery items
file_path = 'Aisle-Mapping.xlsx'
data = pd.read_excel(file_path)

# Ensure the column name matches the one in your file
grocery_list = data['Grocery ITEM'].tolist()

# Dictionary with keywords as keys and aisle categories as values
keyword_to_aisle = {
    "wine": "Alcohol",
    "beer": "Alcohol",
    "vodka": "Alcohol",
    "whiskey": "Alcohol",
    "diapers": "Baby",
    "baby food": "Baby",
    "formula": "Baby",
    "bread": "Bakery",
    "cake": "Bakery",
    "muffin": "Bakery",
    "pastry": "Bakery",
    "flour": "Baking",
    "sugar": "Baking",
    "baking powder": "Baking",
    "yeast": "Baking",
    "juice": "Beverages",
    "soda": "Beverages",
    "tea": "Beverages",
    "coffee": "Beverages",
    "water": "Beverages",
    "chocolate": "Candy",
    "candy": "Candy",
    "gum": "Candy",
    "sweets": "Candy",
    "soup": "Canned Goods",
    "canned": "Canned Goods",
    "beans": "Canned Goods",
    "tomatoes": "Canned Goods",
    "cereal": "Cereal",
    "oats": "Cereal",
    "granola": "Cereal",
    "ketchup": "Condiments",
    "mustard": "Condiments",
    "mayo": "Condiments",
    "sauce": "Condiments",
    "vinegar": "Condiments",
    "milk": "Dairy",
    "cheese": "Dairy",
    "yogurt": "Dairy",
    "butter": "Dairy",
    "frozen": "Frozen",
    "ice cream": "Frozen",
    "frozen pizza": "Frozen",
    "soil": "Garden",
    "plant": "Garden",
    "fertilizer": "Garden",
    "cleaner": "Household",
    "detergent": "Household",
    "paper towels": "Household",
    "chicken": "Meat",
    "beef": "Meat",
    "pork": "Meat",
    "steak": "Meat",
    "bacon": "Meat",
    "miscellaneous": "Misc",
    "other": "Misc",
    "organic": "Organic",
    "pasta": "Pasta & Grains",
    "rice": "Pasta & Grains",
    "quinoa": "Pasta & Grains",
    "noodles": "Pasta & Grains",
    "shampoo": "Personal Care",
    "soap": "Personal Care",
    "toothpaste": "Personal Care",
    "lotion": "Personal Care",
    "dog food": "Pet",
    "cat food": "Pet",
    "pet": "Pet",
    "apple": "Produce",
    "banana": "Produce",
    "carrot": "Produce",
    "lettuce": "Produce",
    "broccoli": "Produce",
    "tomato": "Produce",
    "spinach": "Produce",
    "vegetable": "Produce",
    "vegetables": "Produce",
    "fish": "Seafood",
    "shrimp": "Seafood",
    "salmon": "Seafood",
    "tuna": "Seafood",
    "chips": "Snacks",
    "crackers": "Snacks",
    "nuts": "Snacks",
    "popcorn": "Snacks",
    "pretzels": "Snacks",
    "salt": "Spices",
    "pepper": "Spices",
    "spice": "Spices",
    "herbs": "Spices",
    "seasoning": "Spices"
}

# Initialize dictionaries to hold items for each aisle and "Other"
aisle_items = {aisle: [] for aisle in set(keyword_to_aisle.values())}
aisle_items["Other"] = []

# Function to map grocery items to aisles based on keywords
def map_grocery_items(grocery_list, keyword_to_aisle, aisle_items):
    for item in grocery_list:
        assigned = False
        for keyword, aisle in keyword_to_aisle.items():
            if keyword in item.lower():
                aisle_items[aisle].append(item)
                assigned = True
                break
        if not assigned:
            aisle_items["Other"].append(item)

# Map the grocery items to aisles
map_grocery_items(grocery_list, keyword_to_aisle, aisle_items)

# Print the items in each aisle
for aisle, items in aisle_items.items():
    print(f'Aisle: {aisle}')
    print(f'Top 5 items: {items[:5]}')
