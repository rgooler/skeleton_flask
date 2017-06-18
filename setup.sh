#!/bin/bash
rm -rf virtualenv
virtualenv virtualenv
virtualenv/bin/pip install -r myapp/requirements.txt
