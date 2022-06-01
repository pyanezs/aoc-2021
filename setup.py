import setuptools

setuptools.setup(
    name="aoc2021",
    packages=setuptools.find_packages(exclude=["tests*"]),
    include_package_data=True,
)