from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

# The text of the README file

README = (HERE / "README.md").read_text()

VERSION = '0.1.5'
DESCRIPTION = 'e-nowshop-payment'
LONG_DESCRIPTION = 'Manager payment'
#
# Setting up
setup( 
    name="enowshop-payment",
    version=VERSION,
    author="GustavoSwDaniel",
    author_email="<gustavodanieldetoledo@gmail.com.com>",
    description=DESCRIPTION,
    long_description=README,
    license="MIT",
    url='https://github.com/GustavoSwDaniel/e-nowshop-payment',
    install_requires=['requests'],
    keywords=['python'],
    packages=['enowshop_payment', 'enowshop_payment.orders.', 'enowshop_payment.providers', 'enowshop_payment.schema'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
