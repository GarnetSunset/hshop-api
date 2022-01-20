from distutils.core import setup
setup(
    name = 'hshop-api',
    packages = ['hshop-api'],
    version = '0.1',
    license = 'GPL3',
    description = 'A Python API for interacting with the hShop.',
    author = 'Odyssey346',
    author_email = 'odyssey346@disroot.org',
    url = 'https://github.com/Odyssey346/hshop-api',
    install_requires=[
        'qrcode',
        'requests',
        'tqdm'
    ],
    keywords = ['api', 'nintendo', '3ds', 'downloader'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)