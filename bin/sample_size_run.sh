#!/bin/bash

export FLASK_DEBUG=True
export FLASK_APP=sample_size
export SAMPLESIZE_SETTINGS=config.py
flask run --host 0.0.0.0 --port 8000
