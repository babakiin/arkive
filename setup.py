from setuptools import setup

setup(
    name = "arkive",
    description = "Archive your files in a secure way.",
    url = "https://github.com/babakiin/arkive",
    author = "babakiin",
    author_email = "curious.seal@yahoo.com",
    license = "MIT",
    packages = ["arkive"],
    install_requires = [
        "flask",
    ],
    entry_points = {
        "console_scripts": [
            "arkive=arkive.flask_app:main",
        ],
    },
    zip_safe = False
)
