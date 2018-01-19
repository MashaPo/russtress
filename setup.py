from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='russtress',
      version='0.1.1',
      description='Package that helps you to put lexical stress in russian text',
      long_description=readme(),
      url='https://github.com/MashaPo/russtress',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Education'
      ],
      author='Maria Ponomareva, Kirill Milintsevich',
      keywords='nlp russian stress linguistic',
      author_email='ponomarevamawa@gmail.com',
      packages=['russtress'],
      install_requires=[
          'Keras',
		  'numpy',
		  'scipy',
		  'tensorflow'
      ],
      include_package_data=True,
      zip_safe=False)
