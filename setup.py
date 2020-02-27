import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    "pyyaml==5.3",
    "flake8==3.7.9",
    "imgcompare==2.0.1",
    "diffimg==0.2.3"
]

setuptools.setup(
    name="snapyrest",
    version="0.1.0",
    author="Naresh Sekar",
    author_email="nareshnavinash@gmail.com",
    description="Package to test Rest API endpoints along with snap mode and image comparison functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nareshnavinash/pyrest",
    packages=setuptools.find_packages(),
    keywords = ['REST', 'API', 'API-Automation', 'Image comparison through response from REST API'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)
