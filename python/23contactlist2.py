# 23contactlist.py
# Version 2:


def load(csv):
    with open(csv) as f:
        lines = f.read().split('\n')
    contact_list = {}
    props = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(props, row))
        contact_list[contact['name']] = contact
    return (contact_list, props)


def create(contact_list, contact):
    if contact_list.get(['name']):
        return f"Error: {contact['name']} already exists."
    contact_list[contact['name']] = contact
    return f"Created contact for {contact['name']}."


def read(contact_list, name):
    return contact_list.get(name, f'Error: {name} does not exist.')


def update(contact_list, name, updated_info):
    if contact_list.get(name):
        contact_list[name].update(updated_info)
        return f'Updated contact for {name}'
    return f'Error: {name} does not exist.'


def delete(contact_list, name):
    if contact_list.get(name):
        del contact_list[name]
        return f'{name} deleted'
    return f'Error: {name} does not exist.'


def print_contact(contact):
    if type(contact) is dict:
        for k, v in contact.items():
            print(f'{k}: {v}')
    else:
        print(contact)


def list_all(contact_list):
    for contact in contact_list:
        print_contact(contact_list[contact])
        print()


def save(csv):
    contacts = []
    for contact in contact_list:
        print(contact)


# ----------------------------------------------------------------


if __name__ == '__main__':
    contacts, props = load('contacts.csv')
    loop = True
    valid_inputs = [
        'c', 'create',
        'r', 'read',
        'u', 'update',
        'd', 'delete',
        'e', 'list', 'ls',
        'x', 'exit', 'quit',
        'h', 'help'
    ]
    commands = """
        Commands:
        (c)reate
        (r)ead
        (u)pdate
        (d)elete
        (e)xpand list
        e(x)it
        (h)elp
    """

    print('Welcome to your contact list')
    print(commands)

    while loop:
        print('-'*60)
        while True:

            cmd = input('> ').strip().lower()
            if cmd in valid_inputs:
                break
                print('Invalid input.')
                print(commands)

                if cmd in ['x', 'exit', 'quit']:
                    # save(contacts, 'contacts_out.csv')
                    loop = False
                    print('Goodbye!')

                elif cmd in ['e', 'list', 'ls']:
                    list_all(contacts)

                elif cmd in ['h', 'help']:
                    print(commands)

                elif cmd.startswith('c'):
                    contact = {}
                    for prop in props:
                        contact[prop] = input(f'{prop}: ')
                    print(create(contacts, contact))

                elif cmd.startswith('r'):
                    name = input('name: ')
                    contact = read(contacts, name)
                    print_contact(contact)

                elif cmd.startswith('u'):
                    name = input('name: ')
                    contact = {}
                    for prop in props:
                        val = input(f'{prop}: ')
                        if val:
                            contact[prop] = val
                    print(update(contacts, name, contact))

                elif cmd.startswith('d'):
                    name = input('name: ')
                    print(delete(contacts, name))

# --------------------------------------------------------
