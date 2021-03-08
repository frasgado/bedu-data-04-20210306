lista_nombres = [
    'JOSEPH BANKS',
    'PHILIP HAMILTON',
    'ALEXANDER HAMILTON',
    'Fabiola RasgADO',
    'ASDFASD asdfasdf sadf'
]

lista_nombres_homogeinezados = []
for nombre in lista_nombres:
    nombre_limpio = nombre.lower().strip().replace(' ', '_')
    lista_nombres_homogeinezados.append(nombre_limpio)

print(lista_nombres_homogeinezados)