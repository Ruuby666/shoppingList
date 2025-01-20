import json
import re
from collections import defaultdict


# Function to read products from the products.json file
def load_products():
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Read the tickets from a list of files
def read_tickets(ticket_files):
    products_db = load_products()
    products_find = defaultdict(int)

    for ticket_file in ticket_files:
        with open(ticket_file, "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                match = re.match(r"(\d+)\s*x\s+([^\d]+)\$", linea)  # Ajustar la expresión regular
                if match:
                    cantidad = int(match.group(1))
                    product = match.group(2).strip()  # Eliminar espacios en blanco alrededor del nombre del producto
                    if product in products_db:
                        products_find[product] += cantidad

    return products_find

# Generate the shopping list
def generate_shopping_list(ticket_files):
    products = read_tickets(ticket_files)
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

def show_shopping_list(ticket_files):
    shopping_list = generate_shopping_list(ticket_files)

    with open("lista_compras.txt", "w", encoding="utf-8") as file:
        file.write("🛒 **Lista de Compras:**\n")
        for ingrediente, (cantidad, unidad) in shopping_list.items():
            line = f"   - {cantidad} {unidad} de {ingrediente}\n"
            print(line.strip())
            file.write(line)
    
    print("\n🛒 **Lista de Compras:**")
    for ingrediente, (cantidad, unidad) in shopping_list.items():
        print(f"   - {cantidad} {unidad} de {ingrediente}")

if __name__ == "__main__":
    ticket_files = ["ticket.txt", "ticket2.txt","ticket3.txt", "ticket4.txt","ticket5.txt", "ticket6.txt", "ticket7.txt"]  # Lista de archivos de tickets
    show_shopping_list(ticket_files)