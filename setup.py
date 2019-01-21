from setuptools import setup, find_packages

setup(
        name='qemu2drvcov',
        version='0.0.1',
        description='convert qemu traces to drcov format',
        author='JeffJerseyCow',
        author_email='jeffjerseycow@gmail.com',
        url='https://github.com/JeffJerseyCow/jeff',
        packages=find_packages(),
        entry_points={'console_scripts':['qemu2drcov=qemu2drcov.__main__:main']},
)
