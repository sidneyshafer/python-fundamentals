
dict1 = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
dict2 = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
dict3 = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}

key = input('Enter a course number: ')

room_number = dict1.get(key, 'The course number is not found')
intstructor = dict2.get(key, 'The course number is not found')
time = dict3.get(key, 'The course number is not found')

print('Room Number:', room_number)
print('Instructor:', intstructor)
print('Meeting Time:', time)
