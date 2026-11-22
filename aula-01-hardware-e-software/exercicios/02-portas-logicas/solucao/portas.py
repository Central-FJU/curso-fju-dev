print(True and False)  # False -> luz apagada
print(True or False)   # True  -> luz acesa
print(not True)        # False -> luz apagada

# Desafio: tabela-verdade
print()
print(f"{'A':6}| {'B':6}| {'AND':6}| OR")
for a in (False, True):
    for b in (False, True):
        print(f"{str(a):6}| {str(b):6}| {str(a and b):6}| {a or b}")
