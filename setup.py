from setuptools import setup
def readme():
    with open('README.md') as file:
        README = file.read()
    return README
setup(
  name = 'Topsis_Aparna_102103414',         # How you named your package folder (MyLib)
  packages = ['Topsis_Aparna_102103414'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python package for Multiple Criteria Decision Making (MCDM) using Topsis',   # Give a short description about your library
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'Aparna Singh',                   # Type in your name
  author_email = 'aparnasinghmalout@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/AparnaSingh123/Topsis_Aparna_102103414',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AparnaSingh123/Topsis_Aparna_102103414/archive/v1.0..0tar.gz',    # I explain this later on
  keywords = ['TOPSIS', '102103414', 'Aparna Singh'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
