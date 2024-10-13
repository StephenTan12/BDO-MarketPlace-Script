# BDO MarketPlace Script

## Description

This is a python script that fetches market place data from Black Desert Online using the [BDO Market Arsha API](https://github.com/guy0090/api.arsha.io?tab=readme-ov-file). The data will then be stored on a cloud sql database for future uses.

## Usage

### Installation
1) Create virtual env
```
python -m venv .venv
```
2) Create .env file
3) Activate virtual env
```
source .venv/bin/activate
```
4) Install dependencies
```
pip install -r "requirements.txt"
```
5) Run script!
```
python main.py
```
