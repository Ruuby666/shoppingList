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