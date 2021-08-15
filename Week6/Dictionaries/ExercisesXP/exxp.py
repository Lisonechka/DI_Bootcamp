# # Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result = dict(zip(keys, values))
# print(result)

# Exercise 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# tickets_coasts = ['free', 10, 15]
# coast_total = []
# for key, value in family.items():
#     if value < 3:
#         print(f'For {key} the ticket is {tickets_coasts[0]}.')
#     if value >= 3 and value < 12 :
#         print(f'For {key} the ticket is {tickets_coasts[1]}$.')
#     if value >= 12:
#         print(f'For {key} the ticket is {tickets_coasts[2]}$.')

# Exercise 3
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {'France': 'blue','Spain': 'red', 'US': ['pink', 'green']}}

brand['number_stores'] = 2
print('Zara creats goodies for ' + str(brand['type_of_clothes'][0] + ',' + brand['type_of_clothes'][1]+ ',' + brand['type_of_clothes'][2]))
brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(list(brand.keys()))

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)
print(brand['number_stores'])






