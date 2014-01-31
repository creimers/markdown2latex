from setuptools import setup

setup(
    name = 'markdown2latex',
    version = "2.1",
    py_modules=['mdx_latex'],
    entry_points='''
    [console_scripts]
    markdown2latex.py=mdx_latex:main
    ''',
    install_requires=[
        'Markdown>=1.5',
        ],

    # metadata for upload to PyPI
    author = 'Rufus Pollock (Open Knowledge Foundation)',
    url = 'http://www.okfn.org/okftext/',
    author_email = 'rufus [at] rufuspollock [dot] org',
    description = "Extension to python-markdown to support LaTeX (rather "
		  "than html) output.",
    long_description = "Extension to python-markdown to support LaTeX "
		       "(rather than html) output.",
    license = 'MIT',
    keywords = 'latex markdown python',
    download_url = 'http://pypi.python.org/pypi/markdown2latex/',
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
