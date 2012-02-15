try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='simpleversions',
    version='0.1.2',
    py_modules=['simpleversions'],
    zip_safe=False,
)
