#8.6
life = {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants': {}, 'other': {}}
print(life)

#8.7
print(life.keys())

#8.8
print(life['animals'].keys())

#8.9
print(life['animals']['cats'])

#8.10
squares ={i : i**2 for i in range(10)}
print(squares)

#8.11
A_set = {num for num in range(10) if num % 2 == 1}
print(A_set)

#8.12
aa = (a for a in range(10))
for a in aa:
    print('Got', a)

#8.13
a = ('optimist', 'pessmist', 'troll')
b = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(a, b)))

#8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
print(dict(zip(titles, plots)))
