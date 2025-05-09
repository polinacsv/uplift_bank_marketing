from setuptools import setup, find_packages

setup(
    name="uplift_bank_marketing",
    version="0.1.0",
    description="A Data Science Project for Uplift Modeling on Bank Marketing Data",
    author="Polina Polskaia",
    author_email="polskaia@bu.edu",
    url="https://github.com/polinacsv/uplift-bank-marketing",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy>=1.24,<1.25",
        "pandas>=2.0,<2.1",
        "scikit-learn>=1.1,<1.2",
        "matplotlib>=3.6,<3.7",
        "seaborn>=0.12,<0.13",
        "scipy>=1.9,<1.10"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    options={
        "build": {
            "build_base": "build"  # Ensure build/ directory is specified
        },
        "egg_info": {
            "egg_base": "build/egg-info"
        }
    },
)