from setuptools import setup

setup(name='remarkable_addons',
      version='0.1.0',
      install_requires=[
        'cssselect2==0.2.2',
        'img2pdf==0.3.3',
        'lxml==4.4.2',
        'Pillow==9.3.0',
        'PyPDF2==1.26.0',
        'reportlab==3.5.32',
        'svglib==0.9.3',
        'tinycss2==1.0.2',
        'webencodings==0.5.1',
      ],
      packages=['src', 'src.classes'],
      entry_points={
          'console_scripts': [
              'remarkable_addons = src.__main__:main'
          ]
      },
      )