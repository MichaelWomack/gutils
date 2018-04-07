from setuptools import setup

setup(
		name='gutils',
		version='0.4.0',
		packages=['gutils'], # commented out gutils.gcp
		url='',
		license='',
		author='michaelwomack',
		author_email='',
		description='Utilities for google apis',
		install_requires = [
			'google-cloud-storage==1.7.0'
		]
)
