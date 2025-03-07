import pandas as pd

# Crear datos ficticios y guardarlos en un archivo CSV
data = {
    'Producto': ['Laptop', 'Tablet', 'Smartphone', 'Teclado', 'Mouse'],
    'Cantidad': [15, 20, 50, 100, 150],
    'Precio_unitario': [1000, 500, 300, 50, 25],
    'Fecha': ['2025-03-01', '2025-03-01', '2025-03-02', '2025-03-03', '2025-03-03']
}
df = pd.DataFrame(data)
df.to_csv('ventas.csv', index=False)

# Leer el archivo CSV
df = pd.read_csv('ventas.csv')

# Calcular el ingreso total
df['Ingreso_total'] = df['Cantidad'] * df['Precio_unitario']

# Filtrar productos con ingreso mayor a 1000
productos_filtrados = df[df['Ingreso_total'] > 1000]

# Resumen de ventas por producto
resumen = df.groupby('Producto')['Ingreso_total'].sum().reset_index()

# Guardar los resultados en un nuevo archivo CSV
productos_filtrados.to_csv('productos_filtrados.csv', index=False)
