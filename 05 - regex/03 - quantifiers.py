###
# 03 - Quantifiers
# Los cuantificadores son caracteres especiales que permiten especificar la cantidad de veces 
# que un patrón debe aparecer en una cadena.
###

import re

# *: Puede aparecer 0 o más veces
pattern = r"ab*"
string = "a, ab, abb, abbb, abbbb"
matches = re.findall(pattern, string)
print(f"Matches for '{pattern}' in '{string}': {matches}")

# +: Puede aparecer 1 o más veces
pattern = r"a+"
string = "a, ab, abb, aaabb, abbabb" 
matches = re.findall(pattern, string)
print(matches)

# ?: Puede aparecer 0 o 1 vez
pattern = r"a?b"
string = "aababbabbb abbbb"
matches = re.findall(pattern, string)
print(matches)

# {n}: Debe aparecer exactamente n veces
pattern = r"a{2}"
string = "a, aa, aaa, aa, aaaa aa, aaaa "
matches = re.findall(pattern, string)
print(matches)

# {n, m}: Debe aparecer entre n y m veces
pattern = r"a{2,3}"
string = "a, aa, aaa, aaaa, aaaaa, aaaaaa"
matches = re.findall(pattern, string)
print(matches)

#ejercicio:
#encuentra todas las palabras que contengan entre 2 y 4 letras
words= "la casa de la playa es muy bonita"
patter=r"\b\w{2,4}\b"
matches = re.findall(patter, words)
print(matches)

#ejercicio:
#encuentras las palabras de mas de 5 letras
words= "la casa de la playa es muy bonita"
patter=r"\b\w{5,}\b"
matches = re.findall(patter, words)
print(matches)