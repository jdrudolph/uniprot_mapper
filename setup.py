from distutils.core import setup
setup(name='Uniprot mapper',
		version='0.1',
		packages=['uni_mapper'],

		requires=['urllib','urllib2','argparse'],

		author='Jan Rudolph',
		license='MIT license',
		author_email='jan.daniel.rudolph@gmail.com',
		description='Simple interface for uniprot.org/mapping',
		url='https://github.com/jdrudolph/uniprot_mapper',
		)
