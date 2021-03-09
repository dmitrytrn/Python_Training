person = {'name': 'Polina', 'lastname': 'ppp'}
print('My name is {} {} '.format(*person.values()))
print(f'My name is {person.get("name")} {person.get("lastname")}')
print('My name is ' + ' '.join(str(data) for data in person.values()))
