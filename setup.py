from setuptools import setup, find_packages

setup(name='telegbot',
      version='0.1',
      description='Python API to manage Telegram bot',
      keywords='',
      url='',
      author='Aleksey Preyzner',
      author_email='alexey.preyzner@gmail.com',
      license='GPL v3.0',
      packages=find_packages(),
      install_requires=[
          'requests==2.31.0',
      ],
)
