from distutils.core import setup


setup(
    name='Django Google Tools',
    version='0.1.3',
    description='A simple Django app for managing Google Analytics and Site Verification codes.',
    author='Orne Brocaar',
    author_email='info@brocaar.com',
    url='http://github.com/LUKKIEN/django-google-tools',
    packages=[
        'googletools',
        'googletools.migrations',
        'googletools.templatetags',
    ]
)
