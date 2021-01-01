from setuptools import setup

setup(name='smartbekant',
      version='0.1',
      description='Control your IKEA BEKANT standing desk with a Raspberry Pi.',
      url='https://github.com/theboyknowsclass/SmartBekant',
      author='TheBoyKnowsClass',
      author_email='g@theboyknowsclass.com',
      license='GPLv3+',
      packages=['smartbekant'],
      install_requires=[
          'keybow', 'python3-gpiozero'
      ],
      zip_safe=False)
