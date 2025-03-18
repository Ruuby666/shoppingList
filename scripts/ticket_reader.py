import json
import re
import os
import sys
from collections import defaultdict

# Cargar la base de datos de productos
def load_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Error: El archivo 'products.json' no fue encontrado.")
        return {}

# Leer uno o varios tickets
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
                        product = match.group(2).strip()
                        if product in products_db:
                            products_find[product] += cantidad
        except FileNotFoundError:
            print(f"⚠️ Advertencia: No se encontró el archivo {ticket_file}")

    return products_find

# Generar la lista de compras
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

    return shopping_list

# Mostrar y guardar la lista de compras
def show_shopping_list(ticket_files):
    shopping_list = generate_shopping_list(ticket_files)

    if not shopping_list:
        print("🛒 No hay productos en la lista de compras.")
        return

    with open("lista_compras.txt", "w", encoding="utf-8") as file:
        file.write("🛒 **Lista de la Compra:**\n")
        for ingrediente, (cantidad, unidad) in shopping_list.items():
            line = f"   - {cantidad} {unidad} de {ingrediente}\n"
            print(line.strip())
            file.write(line)

    print("\n✅ Lista de compras guardada en 'lista_compras.txt'.")

if __name__ == "__main__":
    ticket_files = sys.argv[1:]
    if ticket_files:
        show_shopping_list(ticket_files)
    else:
        print("❌ No se proporcionaron archivos de tickets.")
