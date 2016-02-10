try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'SpikeDesktopDjango',
    'description': 'a Spike to see if I can wrap Django into a Windows desktop exe',
    'version': '0.1',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author': 'Lari Kirby',
    'author_email': 'larikirby@fastmail.fm',
    'install_requires': ['nose'],
    'packages': ['SpikeDesktopDjango'],
    'scripts': [],
}

setup(**config)
