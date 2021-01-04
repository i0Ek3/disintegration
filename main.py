"""
I'm freshbird for Python.
"""

y = 'Yes'
n = 'No'

def isNewer(yes, ret=True):
    if ret == True and yes == 'Yes':
        print('Hello, freshbird!')
    elif ret == True and yes == 'No':
        print('Here we go, driver!')
    else:
        print('Your request was dined!')

yes = input('Are you newer for Python? [Yes or No]: ')

isNewer(yes)
