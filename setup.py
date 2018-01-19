from setuptools import setup

setup(name='russtress',
      version='0.1',
      description='Package that helps you to put lexical stress in russian text',
      long_description='The tool based on LSTM predicts stress position in each word in russian text depending on the word context',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Education'
      ],
      keywords=' nlp russian stress linguistic',
      author_email='ponomarevamawa@gmail.com',
      packages=['russtress'],
      install_requires=[
          'Keras==2.0.4',
		  'numpy==1.13.3',
		  'scipy==0.19.0',
		  'tensorflow==1.1.0'
      ],
      include_package_data=True,
      zip_safe=False)
