import json
import re
from collections import defaultdict


# Function to read products from the products.json file
def load_products():
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
# Read the ticket in ASCII format from ticket.txt
def read_ticket():
    productos_db = load_products()
    productos_encontrados = defaultdict(int)

    with open("ticket.txt", "r", encoding="ascii") as file:
        for linea in file:
            linea = linea.strip()
            match = re.match(r"(\d+)x\s+(.*)", linea)  # Busca líneas con "2x Producto"
            if match:
                cantidad = int(match.group(1))
                producto = match.group(2)
                if producto in productos_db:
                    productos_encontrados[producto] += cantidad

    return productos_encontrados

# Generate the shopping list
def generate_shopping_list():
    productos = read_ticket()
    productos_db = load_products()
    lista_compras = defaultdict(lambda: [0, ""])  # {Ingrediente: [Cantidad, Unidad]}

    for producto, cantidad_pedida in productos.items():
        if "ingredientes" in productos_db[producto]:  
            for i, ingrediente in enumerate(productos_db[producto]["ingredientes"]):
                cantidad_original = productos_db[producto]["cantidad"][i]
                match = re.match(r"([\d.]+)\s*(\w+)", cantidad_original)  # Extraer número y unidad
                
                if match:
                    valor = float(match.group(1)) * cantidad_pedida
                    unidad = match.group(2)
                    lista_compras[ingrediente][0] += valor  # Sumar cantidad
                    lista_compras[ingrediente][1] = unidad  

    return lista_compras

def show_shopping_list():
    lista_compras = generate_shopping_list()
    
    print("\n🛒 **Lista de Compras:**")
    for ingrediente, (cantidad, unidad) in lista_compras.items():
        print(f"   - {cantidad} {unidad} de {ingrediente}")