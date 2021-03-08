def clean_names(name):
    return name.lower().strip().replace(' ', '_')

names = [
    'JOSEPH BANKS',
    'PHILIP HAMILTON',
    'ALEXANDER HAMILTON',
    'Fabiola RasgADO',
    'ASDFASD asdfasdf sadf'
]

print(names)

names_clean = list(map(clean_names, names))
print(names_clean)