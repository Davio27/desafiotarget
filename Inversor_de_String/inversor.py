def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

entrada = input("Digite uma palavra/frase: ")
print(f"String invertida: {inverter_string(entrada)}")
