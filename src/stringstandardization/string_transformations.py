import unidecode

def remove_special_characters(text):
    return unidecode.unidecode(text)


name = 'Ramon Durães'
standardized_name = remove_special_characters(name)
print(f"Seu nome padronizado é {standardized_name}")
