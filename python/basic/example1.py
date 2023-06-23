# Data of fakeusers

fakeusers = [
	{"name":"John Westin", "id": "user1"},
	{"name":"Sally Smith", "id": "user2"},
    {"name":"Jane Doe", "id": "user3"},
    {"name":"Bob Smith", "id": "user4"},
	{"name":"Sue Jones", "id": "user5"},
    {"name":"Sally Smith", "id": "user6"},	
    {"name":"Jane Doe", "id": "user7"},
    {"name":"Bob Smith", "id": "user8"},
    {"name":"Sue Jones", "id": "user9"},
    {"name":"Sally Smith", "id": "user10"},
]

# print(fakeusers)

#print fakesuers 10 element
# print(fakeusers[8]['name'])
# print(fakeusers[8]['id'])

#write code to travese fakesuers
for user in fakeusers:
    if user['name'] == 'Sally Smith':
        print(user['id'])
