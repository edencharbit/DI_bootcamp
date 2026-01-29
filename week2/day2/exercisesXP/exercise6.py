# Exercise 6: Magicians…

"""Goal: Modify a list of magician names and display them in different ways."""

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)


def make_great(magician_names):
    magician_great = []
    for magician in magician_names:
        magician_new = "the Great " + magician
        magician_great.append(magician_new)
    return magician_great


great_magician = make_great(magician_names)
show_magicians(great_magician)
