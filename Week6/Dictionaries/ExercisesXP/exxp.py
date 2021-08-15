# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key, value in family.items():
    if value < 3:
        print(f'For {family[key]} the ticket is free.')
    if value >= 3 and value < 12 :
        print(f'For {family[key]} the ticket is $10.')
    if value >= 12:
        print(f'For {family[key]} the ticket is $15.')

