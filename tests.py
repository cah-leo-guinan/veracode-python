if __name__ == '__main__':
    import doctest
    from veracode import application
    from veracode.exceptions import *

    doctest.testmod(application)

# pycco veracode/*.py veracode/SDK veracode/API -ips