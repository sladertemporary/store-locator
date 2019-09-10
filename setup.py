from setuptools import setup

setup(
    name='tails-test',
    version='1.0',
    packages=['app', 'app.StoreLocator', 'app.StoreLocator.static'],
    url='',
    license='GNU',
    author='Sam Lader',
    author_email='me@samlader.com',
    description='Test assignment for Tails interview',
    install_requires = [
                       'flask',
                        'requests',
                        'click',
                        'Werkzeug'
                   ],
)
