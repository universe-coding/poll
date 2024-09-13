
def titleBar(title, symbol='/\\', noofdecorators=10):
    """Print a title bar."""
    onesidedecor = round(noofdecorators / 2)
    try:
        decor = symbol * onesidedecor
    except TypeError:
        print('The value entered for "No. of decorators" was not the supposed type.')
        print('It was either a string or a float.')
        decor = ''
    print(decor + title + decor)