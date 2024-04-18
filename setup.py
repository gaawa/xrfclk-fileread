from setuptools import setup


with open("README.md", encoding='utf-8') as fh:
    readme_lines = fh.readlines()[:]
long_description = (''.join(readme_lines))


setup(
    name="xrfclk-fileread",
    version='1.0',
    description="Extension for xrfclk driver to allow passing local register files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    license='BSD 3-Clause',
    author="Gaawa",
    author_email="",
    packages=['xrfclk_fileread'],
    package_data={
        '': ['*.py'],
    }
)

