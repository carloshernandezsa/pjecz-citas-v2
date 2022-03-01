"""
Comandos Click para instalar con pip install --editable .
"""
from setuptools import setup


setup(
    name="citas_v2",
    version="0.1",
    entry_points="""
        [console_scripts]
        citas_v2=cli.cli:cli
    """,
)
