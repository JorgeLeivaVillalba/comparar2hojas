import pandas as pd

# Ruta del archivo Excel
archivo = 'comparar.xlsx'  # Reemplaza con el nombre real del archivo

# Cargar las dos hojas
df1 = pd.read_excel(archivo, sheet_name='Hoja1')  # Reemplaza con el nombre real de la hoja
df2 = pd.read_excel(archivo, sheet_name='Hoja2')

# Alinear columnas si están en distinto orden pero con mismos nombres
df1 = df1[df2.columns]

# Filas que están en Hoja1 pero no en Hoja2
diff_1 = df1[~df1.apply(tuple, axis=1).isin(df2.apply(tuple, axis=1))]

# Filas que están en Hoja2 pero no en Hoja1
diff_2 = df2[~df2.apply(tuple, axis=1).isin(df1.apply(tuple, axis=1))]

# Marcar origen de las diferencias
diff_1['Origen'] = 'Solo en Hoja1'
diff_2['Origen'] = 'Solo en Hoja2'

# Combinar resultados
diferencias = pd.concat([diff_1, diff_2])

# Guardar a un nuevo archivo
diferencias.to_excel('filas_diferentes.xlsx', index=False)
