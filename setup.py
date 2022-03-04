"""
Comandos Click para instalar con pip install --editable .
"""
from setuptools import setup


setup(
    name="citas",
    version="0.1",
    entry_points="""
        [console_scripts]
        citas=cli.cli:cli
    """,
)
