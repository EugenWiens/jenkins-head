import setuptools

with open("package-description.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="jenkins-head-controller",
    version="0.0.0.dev2",
    author="Hermann Leinweber",
    author_email="hermann.leinweber@leinies.de",
    description="Deamon to visualize the state of jenkins jobs with a 'jenkins head' (BLE controlled lights)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EugenWiens/jenkins-head",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'jenkins-head-controller=jenkins_head_controller:main'
        ]
    },
    install_requires=[
        'pyyaml',
        'python-jenkins'
    ],
)
