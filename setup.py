"""sample_size python package configuration."""

from setuptools import setup

setup(
    name='sample_size',
    version='0.1.0',
    author='Baker Moran',
    author_email='bamoran99@gmail.com',
    license='MIT',
    description='A website for Bayesian AB Test sample size estimation.',
    packages=['sample_size'],
    keywords=['AB Test', 'Bayes', 'Bayesian Statistics', 'Sample Size'],
    url='https://github.com/bakermoran/AB-Test-Sample-Size',
    include_package_data=True,
    install_requires=[
        'flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'nodeenv',
        'sh',
        'Flask-Testing',
        'selenium',
        'requests',
        'arrow',
        'scipy'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
)
