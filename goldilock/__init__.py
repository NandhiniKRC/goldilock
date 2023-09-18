"""Top-level package for goldilock."""

__author__ = """Nandhini Ramachandran"""
__email__ = 'nandhini.krc@gmail.com'
__version__ = '0.0.2'

from .goldilock import* 

'''When we say goldilock.function it won't work since the  file opens __init__first.                   
To    avoid goldilock.goldilock.funtion we can import the package directly here so that we can directly access it as goldilock.function rather than the above '''


