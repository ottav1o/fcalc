import logging

is_verbose=False
APP_ID='org.ottav1o.fcalc'
APP_VERSION='0.0.0-DEVEL'
APP_NAME='FCalc'
APP_DESC='School absences calculator (Based on brazillian laws)'
app_language='pt-BR'
logger: logging.Logger = None
lang: dict = None
max_percentage: int = 25