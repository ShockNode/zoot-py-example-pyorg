import setuptools

setuptools.setup(
  name = 'definitions',
  packages=setuptools.find_packages(),
  version = '0.0.1',
  install_requires = ['zoot'],
  description = 'sample automation suite',
  author = 'Brent Ray',
  author_email = 'brentlamarrayjr@gmail.com',
  url = 'https://github.com/brentlamarrayjr/zoot-py-example-pyorg',
  keywords = ['testing', 'api', 'json', 'validation','automation','framework'],
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)