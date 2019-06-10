import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

install_requires=['beautifulsoup4']

setuptools.setup(
    name='wz_uniform_crawler',
    version='1.0.0',
    author='Issac Lin',
    author_email='issaclin32@gmail.com',
    description='A simple crawler script for Uniform Map / 制服地圖 (http://uniform.wingzero.tw/)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/issaclin32/wz_uniform_crawler',
    packages=['wz_uniform_crawler'],
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=False
)