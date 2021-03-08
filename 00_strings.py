name = 'FABIOLA'
surname = ' rasgado '

full_name = name + surname
print(full_name)
print(full_name.lower())

'''
full_name = full_name.lower()
full_name = full_name.strip()  
#// funcion que se encarga limpieza de espacios

print(len(full_name))
full_name = full_name.replace(' ', '_')
'''

full_name = full_name.lower().strip().replace(' ', '_')
print(full_name)
