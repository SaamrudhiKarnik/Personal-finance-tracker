from setuptools import setup, find_packages

setup(
    name="personal-finance-tracker",
    version="1.0.0",
    description="A comprehensive Python application for managing personal finances",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.5.0",
        "pandas>=1.3.0", 
        "seaborn>=0.11.0",
        "numpy>=1.21.0",
        "Pillow>=8.0.0",
        "fpdf>=1.7.0",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'finance-tracker=run:main',
        ],
    },
)