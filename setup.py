from setuptools import setup

setup(
    #Author info and package location
    name ='hughes',
	url = 'https://github.com/Huggies23/hughes-random',
	author = 'David Hughes',
	author_email = 'david.james.hughes13@gmail.com',
	#packaging and installation parameters
	packages = ['hughes'],
	install_requires=['numpy', 'matplotlib'],
	version = '0.1',
	licence = 'N/A',
	description = 'Produce objects containing random numbers generated from a given statistical distribution'
	#long_desription = open('README.txt').read()
)
