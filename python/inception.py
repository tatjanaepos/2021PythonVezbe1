"""The very first module in a more structured version of the project.
"""


# Moving code from main.py

# print('Enter year:',end=' ')
# year=input()
# print(year)

def release_year():
    """"A simple function"""
    song='Imagne'
    year=1976
    print(f'The song is {song} and year is {year}')


# Taking care of the module __name__

if __name__ == '__main__':
    release_year()

# Printing with ' ' and printing without '\n'
    print('Enter year:',end=' ')
    year=input()
    print(year)

# Printing with classical formatting (%)

# Keyboard input

# break and continue

# Printing docstrings

# Printing a list using enumerate()

# Importing from Standard Library
    from datetime import date
    d=date(1971,10,11)
    print(d)
    d_format='%b %d %Y'
    print(d.strftime(d_format))

