# setup.py

from setuptools import setup, find_packages

setup(
    name='titas_lib',
    version='0.1.0',
    author='Geanderson Lemonte e Luiz Fernando',
    author_email='geandersonlemonte.gl@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pybricks',  # Adicione dependências necessárias aqui
    ],
    description='Uma biblioteca Python para controle de robótica LEGO cara EV3 e SPIKE',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)