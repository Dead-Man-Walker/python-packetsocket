from setuptools import setup, find_packages
import os


def getREADME(return_on_failure=""):
	_dir = os.path.abspath(os.path.dirname(__file__))
	readmes = [x for x in os.listdir(_dir) 
		if x.split(".")[0].lower() == "readme"]	
	try:
		readme = readmes[0]
	except IndexError:
		return return_on_failure
	with open(os.path.join(_dir, readme)) as f:
		return f.read()


setup(name='packetsocket',
      version='1.0.0',
      description='High-level socket interface for non-blocking packet communication',
      long_description=getREADME(),
      long_description_content_type='text/markdown',
      url='https://github.com/Dead-Man-Walker/python-packetsocket',
      author='Kevin Hambrecht',
      author_email='kev.hambrecht@gmail.com',
      license='Nope',
      packages=find_packages(),
      zip_safe=False)
