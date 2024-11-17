from setuptools import setup, find_packages

setup(
    name="account_type_predictor",
    version="1.0.0",
    description="Prédicteur de types de comptes basé sur un modèle ML.",
    author="Abdallah Nassur",
    author_email="nassur1607@gmail.com",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "joblib",
        "pandas",
    ],
    include_package_data=True,
    package_data={"account_type_predictor": ["model.pkl"]},
)
