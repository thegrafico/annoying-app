import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-thegrafico", # Replace with your own username
    version="0.0.1",
    author="Raul Pichardo Avalo",
    author_email="raul022107@gmail.com",
    description="SCRUM Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thegrafico/annoying-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)