# Ticket Manager & Shopping List 🛒

This project processes shopping tickets from a single file or a folder containing multiple ticket files and generates a shopping list based on the detected products. A graphical user interface (GUI) allows users to easily select files or folders.

## 🚀 Installation & Usage

### 1️⃣ Requirements

Ensure **Python 3.x** is installed on your system.

### 2️⃣ Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Ruuby666/compras.git
cd compras
```

### 3️⃣ Run the GUI

```bash
python ./scripts/ui.py
```

Options:

- **📄 A file**: Process a single ticket.
- **📂 A folder**: Process multiple tickets.

### 4️⃣ Run Manually

If you prefer running the script manually:

```bash
python ticket_reader.py ticket1.txt ticket2.txt
```

To process all tickets in a folder:

```bash
python ticket_reader.py tickets/*.txt
```

## 📜 `products.json` Format

```json
{
    "Pizza": {
        "ingredients": ["Flour", "Tomato", "Cheese"],
        "quantity": ["200g", "100ml", "150g"]
    },
    "Bread": {
        "ingredients": ["Flour", "Yeast"],
        "quantity": ["500g", "10g"]
    }
}
```

## 📝 Output: `shopping_list.txt`

The generated shopping list:

```
🛒 **Shopping List:**
   - 400g Flour
   - 1.0ud Tomato
   - 300g Cheese
   - 10g Yeast
```

## 📌 Notes

- If `products.json` is missing, the program will show an error.
- If a ticket contains products not in `products.json`, they will be ignored.

## 🤖 Author

Developed by **Rubén Sepúlveda Real** ✨

---

## 📖 Leer en Español

Este proyecto permite procesar tickets de compra desde un archivo o una carpeta con varios tickets y generar una lista de compras. Tiene una interfaz gráfica para seleccionar archivos.

### 🚀 Uso

1️⃣ Clona el repositorio:

```bash
git clone https://github.com/Ruuby666/compras.git
cd compras
```

2️⃣ Ejecuta la interfaz gráfica:

```bash
python ui.py
```

3️⃣ O ejecuta manualmente:

```bash
python ticket_reader.py ticket1.txt ticket2.txt
```

## 📜 `products.json` Formato

```json
{
    "Pizza": {
        "ingredients": ["Flour", "Tomato", "Cheese"],
        "quantity": ["200g", "100ml", "150g"]
    },
    "Bread": {
        "ingredients": ["Flour", "Yeast"],
        "quantity": ["500g", "10g"]
    }
}
```

- **Salida:** genera la lista de compras (`shopping_list.txt`):

```
🛒 Lista de Compras:
   - 400g Harina
   - 100ml Tomate
   - 300g Queso
   - 10g Levadura
```

### 📌 Notas

- Si `products.json` no existe, el programa mostrará un error.
- Los productos desconocidos serán ignorados.

Desarrollado por **Rubén** ✨

