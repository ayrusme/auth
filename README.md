# Project Astrix

This repository contains all the backend files required for Project Astrix

## Installing MySQL
---
TODO 

## Installing Project Astrix
---
This project uses a virtual environment to manage all dependencies. 

### Prerequisites:
* Linux ( Preferably Ubuntu )
* Python 3.6
* pipenv

Python3.6 comes along with Ubuntu versions greater than 17.10, but if you are in a lower version, please use the below command

```shell
sudo apt-get update
sudo apt-get install python3.6
```

To install pipenv, use the command

```shell
pip install --user pipenv
```
If your pip is configured for Python2.7 and you have Python3.6 configured in pip3, use the following command

```shell
pip3 install --user pipenv
```

## Running Project Astrix
---

Run the following command to start the server for Project Astrix

```python
python3 server.py
```