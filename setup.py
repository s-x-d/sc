from setuptools import setup, find_packages

setup(
    name="aws4",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Django==4.2.7",
        "gunicorn==21.2.0",
        "psycopg2-binary==2.9.9",
        "python-dotenv==1.0.0",
        "pillow==10.1.0",
    ],
)