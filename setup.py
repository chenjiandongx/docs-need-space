from setuptools import setup

setup(
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    name="dnspace",
    version="0.1.0",
    license="MIT",
    url="https://github.com/chenjiandongx/docs-need-space",
    py_modules=["dnspace"],
    description="docs need space",
    entry_points={"console_scripts": ["space=dnspace:command_line_runner"]},
)
