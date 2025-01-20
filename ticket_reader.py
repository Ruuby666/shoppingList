import json
import re
from collections import defaultdict


# Function to read products from the products.json file
def load_products():
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
# Read the ticket in ASCII format from ticket.txt
def read_ticket():
    products_db = load_products()
    products_find = defaultdict(int)

    with open("ticket.txt", "r", encoding="utf-8") as file:
        for linea in file:
            linea = linea.strip()
            match = re.match(r"(\d+)\s*x\s+([^\d]+)\$", linea)  # Busca líneas con "2 x Producto" o "2x Producto"
            if match:
                cantidad = int(match.group(1))
                print(cantidad)
                product = match.group(2).strip()
                print(product)
                if product in products_db:
                    products_find[product] += cantidad

    return products_find

# Generate the shopping list
def generate_shopping_list():
    products = read_ticket()
    products_db = load_products()
    shopping_list = defaultdict(lambda: [0, ""])  # {Ingrediente: [Cantidad, Unidad]}

    for producto, cantidad_pedida in products.items():
        if "ingredientes" in products_db[producto]:  
            for i, ingrediente in enumerate(products_db[producto]["ingredientes"]):
                cantidad_original = products_db[producto]["cantidad"][i]
                match = re.match(r"([\d.]+)\s*(\w+)", cantidad_original)  # Extraer número y unidad
                
                if match:
                    valor = float(match.group(1)) * cantidad_pedida
                    unidad = match.group(2)
                    shopping_list[ingrediente][0] += valor  # Sumar cantidad
                    shopping_list[ingrediente][1] = unidad  

    return shopping_list 

# Shows the shopping list
def show_shopping_list():
    shopping_list = generate_shopping_list()
    
    print("\n🛒 **Lista de Compras:**")
    for ingrediente, (cantidad, unidad) in shopping_list.items():
        print(f"   - {cantidad} {unidad} de {ingrediente}")

if __name__ == "__main__":
    show_shopping_list()