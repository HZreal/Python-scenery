import shutil

a = 1

assert a == 1, 'assert successfully, here will not be output'
assert a == 2, 'assert error, here will be output'



assert shutil.which('python') is None, 'error in assert'

