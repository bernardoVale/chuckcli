from setuptools import setup

setup(
        name='chucknorris-cli',
        version='0.1',
        author='Bernardo Vale',
        author_email='bvale@avenuecode.com',
        packages=['chucknorris'],
        scripts=['bin/chuck'],
        install_requires=[
            'requests==2.18.1'
        ],
)
