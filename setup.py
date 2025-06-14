from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="dcckit",
    version="0.0.2",
    description="Description",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="dcckit",
    url="https://github.com/Bailey3D/dcc-kit",
    author="Bailey3D",
    author_email="bailey@bailey3d.com",
    license="MIT",
    packages=["dcckit"],
    package_dir={"dcckit": "dcckit"},
    install_requires=[
        "numpy",
        "pythonnet",
        "qtpy",
        "scipy",
    ],
    include_package_data=True,
    zip_safe=False
)