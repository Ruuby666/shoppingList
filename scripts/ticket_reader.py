import json
import re
import os
import sys
from collections import defaultdict

# Function to find a file in the current folder and subfolders
def find_file(filename):
    current_directory = os.getcwd()  # Get current directory
    for root, dirs, files in os.walk(current_directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Load products from JSON file
def load_products():
    products_file = find_file("products.json")
    if products_file:
        try:
            with open(products_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"❌ Error loading 'products.json': {e}")
    else:
        print("❌ Error: The file 'products.json' not found in the current directory or subdirectories.")
    return {}

# Read one or a directory of ticket files
def read_tickets(ticket_files):
    products_db = load_products()
    products_find = defaultdict(int)

    for ticket_file in ticket_files:
        try:
            with open(ticket_file, "r", encoding="utf-8") as file:
                for linea in file:
                    linea = linea.strip()
                    match = re.match(r"(\d+)\s*x\s+([^\d]+)\$", linea)
                    if match:
                        cantidad = int(match.group(1))
                        print(cantidad)
                        product = match.group(2).strip()
                        print(product)
                        if product in products_db:
                            products_find[product] += cantidad
                        else:
                            print(f"⚠️ Warning: The product '{product}' in {ticket_file} is not defined in 'products.json'.")

        except FileNotFoundError:
            print(f"⚠️ Warning: File not found {ticket_file}")

    return products_find

# Generates a shopping list based on the meals found in the tickets
def generate_shopping_list(ticket_files):
    products = read_tickets(ticket_files)
    products_db = load_products()
    shopping_list = defaultdict(lambda: [0, ""])

    for producto, cantidad_pedida in products.items():
        if "ingredientes" in products_db.get(producto, {}):
            for i, ingrediente in enumerate(products_db[producto]["ingredientes"]):
                cantidad_original = products_db[producto]["cantidad"][i]
                match = re.match(r"([\d.]+)\s*(\w+)", cantidad_original)
                if match:
                    valor = float(match.group(1)) * cantidad_pedida
                    unidad = match.group(2)
                    shopping_list[ingrediente][0] += valor
                    shopping_list[ingrediente][1] = unidad
                    print(valor)
                    print(unidad)
                    print(ingrediente)

    return shopping_list

# Show and save the shopping list
def show_shopping_list(ticket_files):
    shopping_list = generate_shopping_list(ticket_files)

    if not shopping_list:
        print("🛒 There is no products in the shopping list.")
        return

    with open("shopping_list.txt", "w", encoding="utf-8") as file:
        file.write("🛒 **Shopping list:**\n")
        for ingrediente, (cantidad, unidad) in shopping_list.items():
            line = f"   - {cantidad} {unidad} de {ingrediente}\n"
            print(line.strip())
            file.write(line)

    print("\n✅ Shopping list saved in 'shopping_list.txt'.")

if __name__ == "__main__":
    ticket_files = sys.argv[1:]
    if ticket_files:
        show_shopping_list(ticket_files)
    else:
        print("❌ No ticket files provided.")
