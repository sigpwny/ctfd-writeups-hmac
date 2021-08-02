from os import environ

def config(app):
    '''
    Writeups form as a format string with a parameter for the hmac
    '''
    app.config['WRITEUPS_FORM'] = environ.get('WRITEUPS_FORM')

    '''
    Writeups form hmac secret
    '''
    app.config['WRITEUPS_SECRET'] = environ.get('WRITEUPS_SECRET')
