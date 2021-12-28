import setuptools


setuptools.setup(
    name='mkdocs-monorepo-wildcard-plugin',
    version='0.1.0',
    description='Plugin for adding monorepository support with additional support for wildcard includes in Mkdocs.',
    long_description="""
        This introduces support for the !include syntax in mkdocs.yml, allowing you to import additional Mkdocs navigation.
        It enables large or complex repositories to have their own sets of docs/ folders, whilst generating only a single Mkdocs site.
        This is a fork adding support for wildcard includes.
    """,  # noqa: E501
    keywords='mkdocs monorepo wildcard',
    url='https://github.com/TeamTeaTime/mkdocs-monorepo-plugin',
    author='Thomas Jung',
    author_email='thomas@jung.town',
    license='Apache-2.0',
    python_requires='>=3',
    install_requires=[
        'mkdocs>=1.0.4',
        'python-slugify>=4.0.1'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'mkdocs.plugins': [
            "monorepo-wildcard = mkdocs_monorepo_wildcard_plugin.plugin:MonorepoWildcardPlugin"
        ]
    }
)
