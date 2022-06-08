# This program demonstrates various set operations

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

print('Students on the baseball team:')
for name in baseball:
    print(name)

print()
print('Students on the basketball team:')
for name in basketball:
    print(name)

# Intersection
print()
print('Students who play baseball and basketball:')
for name in baseball & basketball: # set1.intersection(set2)
    print(name)

# Union
print()
print('Students who play either baseball or basketball:')
for name in baseball | basketball: # set1.union(set2)
    print(name)

# Difference
print()
print('Students who play baseball, but not basketball:')
for name in baseball - basketball: # set1.difference(set2)
    print(name)

print()
print('Students who play basketball, but not baseball:')
for name in basketball - baseball: # set2.difference(set1)
    print(name)

# Symmetric difference
print()
print('Students who play one sport, but not both:')
for name in baseball ^ basketball: # set1.symmetric_difference(set2)
    print(name)
