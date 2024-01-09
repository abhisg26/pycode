people: dict = {'mario':1,'luigi':2}

print(people.get('mario'))

print(people.get('asd'))
print(people.get('asd',0))
print(people.setdefault('asd',0))
print(people)