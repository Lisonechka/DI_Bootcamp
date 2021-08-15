# # Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result = dict(zip(keys, values))
# print(result)

# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
tickets_coasts = ['free', 10, 15]
coast_total = []
for key, value in family.items():
    if value < 3:
        print(f'For {key} the ticket is {tickets_coasts[0]}.')
    if value >= 3 and value < 12 :
        print(f'For {key} the ticket is {tickets_coasts[1]}$.')
    if value >= 12:
        print(f'For {key} the ticket is {tickets_coasts[2]}$.')



