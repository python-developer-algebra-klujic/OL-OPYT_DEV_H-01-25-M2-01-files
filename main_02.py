

def save_to_file(content: str, file_name: str):
    try:
        with open(file_name, 'a') as file_writer:
            file_writer.write(f'{content}\n')

    except Exception as ex:
        print(f'Dogodila se greska: {ex}.')


def save_to_db(content: str):
    # TODO implement db CRUD (Create, Read, Update, Delete)
    pass


def save_contact(contact: str):
    if app_config['app_config_save'] == 'file':
        save_to_file(content=contact, file_name=app_config['app_config_file_name'])

    elif app_config['app_config_save'] == 'db':
        save_to_db(contact)


def main(app_config):
    while True:
        first_name = input('Upisite ime kontakta: ')
        last_name = input('Upisite prezime kontakta: ')

        save_contact(f'{first_name} {last_name}')

        print()
        next_name = input('Zelite li dodati novi kontakt u adresar? (da/ne): ')
        if next_name.lower() != 'da':
            break



















# Lokacija kamo mozemo pohraniti podatke:
# - file = u address_book.txt datoteku
# - db = u address_book.db bazu
# - https = na server POST https://api/address_book
try:
    with open('app_config.txt', 'r') as file_reader:
        file_content = file_reader.readlines()

        app_config = {}

        app_config['app_config_save'] = file_content[0]
        app_config['app_config_file_name'] = file_content[1]

        main(app_config)

except Exception as ex:
    print(f'NIJE MOGUCE POKRENUTI APLIKACIJU')
    print(f'Dogodila se greska {ex}.')