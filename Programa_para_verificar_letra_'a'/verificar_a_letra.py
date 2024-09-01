def count_a(string):
    count = string.lower().count('a')
    return count

# Exemplo de uso:
string = input("Digite uma palavra: ")
count = count_a(string)
print(f"A letra 'a' aparece {count} vezes na string.")
