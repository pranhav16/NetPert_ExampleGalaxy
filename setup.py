from setuptools import setup, find_packages, Command
from setuptools.command.install import install
import subprocess
import os

class CustomInstallCommand(install):
    def run(self):
        # Get the directory where setup.py is located
        base_dir = os.path.abspath(os.path.dirname(__file__))
        # Path to build.sh relative to setup.py
        build_script = os.path.join(base_dir, 'netpert_examplegalaxy', 'build.sh')
        # Execute build.sh
        subprocess.call(['bash', build_script])
        install.run(self)
setup(
    name="netpert_examplegalaxy",
    author="Pranhav Sundararajan",
    author_email="pranhav16@gmail.com",
    description="Tool to identify if a gene is a mouse or human gene",
    url="https://github.com/pranhav16/NetPert_ExampleGalaxy",
    cmdclass={
        'install': CustomInstallCommand,
    },
    packages=find_packages(),
    package_data={
        '': ['databases/MRK_List2.rpt'], '': ['databases/trrust_rawdata.human.tsv'],  # Include all .txt files in the 'data' directory
    },
    entry_points={
        'console_scripts': [
            'netpert_examplegalaxy = netpert_examplegalaxy:__init__',
        ],
    },
    install_requires=['pandas'],
    
)
