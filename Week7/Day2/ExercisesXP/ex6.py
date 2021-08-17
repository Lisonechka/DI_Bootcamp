# Exercise 6 : Magicians …
magicians_names = ['John', 'Albert', 'Frederick', 'Paolo', 'Ludwig']
def show_magicians():
    for mag in magicians_names:
        print([mag])

def make_great():
    for key, value in enumerate(magicians_names):
        magicians_names[key] = 'the Great ' + value

make_great()
print([magicians_names])
show_magicians()
