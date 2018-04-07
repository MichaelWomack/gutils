#!/usr/bin/env bash

pip install pipenv
pipenv lock --requirements > requirements.txt
pipenv lock --requirements --dev >> requirements.txt
pip install -r requirements.txt