from distutils.core import setup

setup(
    name='asciiart',
    version='0.0.2',
    author='Shiva Velmurugan',
    author_email='shiv@shiv.me',
    scripts=['scripts/art.py'],
    url='https://github.com/shiva/asciiart',
    license='LICENSE.md',
    description='Generate Ascii Art using pyfiglet.',
    long_description=open('README.md').read(),
    install_requires=['pyfiglet >= 0.6.1'],
    dependency_links = [
        "https://github.com/pwaller/pyfiglet.git"
    ],
)

