

# name = 'Ana Anic'
name = input('Upisite ime: ')

# try:
#     # 1. korak otvaranje datoteke
#     file_writer = open('files/names.txt', 'a', encoding='UTF-8')

#     # 2. korak pisanje u datoteku
#     file_writer.write(f'{name}\n')

# except Exception as ex:
#     print(f'Dogodila se greska: {ex}')

# finally:
#     # 3. korak zatvaranje pristupa datoteci
#     if file_writer != None:
#         file_writer.close()


# Snippet - kako raditi s tekstualnim datotekama
try:
    with open('files/names.txt', 'a', encoding='UTF-8') as file_writer:
        file_writer.write(f'{name}\n')

except Exception as ex:
    print(f'Dogodila se greska: {ex}')
