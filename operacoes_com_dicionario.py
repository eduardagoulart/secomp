CODIGOS_DISCAGEM = [
    (86, 'China'),
    (5, 'Brasil'),
    (1, "Estados Unidos"),
    (62, 'Indonesia'),
    (7, 'Russia'),
]

codigo_do_pais = {pais: codigo for codigo, pais in CODIGOS_DISCAGEM}
print(codigo_do_pais)

print(f'keys(): {codigo_do_pais.keys()}')
print(f'values(): {codigo_do_pais.values()}')
print(f'pop(): {codigo_do_pais.pop("Russia")}')
codigo_do_pais.__delitem__("Indonesia")
print(f'__delitem__: {codigo_do_pais}')