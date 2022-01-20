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
)