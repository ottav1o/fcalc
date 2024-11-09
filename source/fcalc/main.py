import sys
import tkinter.messagebox
from .. import commons

import gi
gi.require_version('Gtk', '4.0')

from gi.repository import Gtk as gtk

import logging
import json
import pathlib
import tkinter

from source.fcalc import windows

def load_language(language: str):
    if not pathlib.Path(f'./source/languages/{language}.json').is_file():
        commons.logger.critical('Cannot load language "{}": "./source/languages/{}.json" No such file.'.format(language, language))
        tkinter.messagebox.showerror('ERROR', 'Invalid language')
        exit(1)

    with open(f'./source/languages/{language}.json', 'r') as lfile:
        commons.lang = json.load(fp=lfile)
        commons.logger.info('Loaded language: "{}".'.format(commons.lang['Language']))

def main() -> None:
    logging.basicConfig(format='[%(levelname)s] [ - %(name)s - ] (%(asctime)s): " %(message)s "', level=logging.DEBUG if commons.is_verbose else logging.INFO)

    logging.info('Running fcalc!')
    commons.logger = logging.getLogger(commons.APP_NAME + ' | ' + commons.APP_ID)
    commons.logger.debug('Running on verbose mode.')

    commons.logger.info('Loading default language: "{}".'.format(commons.app_language))
    load_language(commons.app_language)

    app = windows.Application()
    exit_status = app.run()
    commons.logger.debug('Process exited with "{}" as return value.'.format(f'{exit_status} OK' if exit_status == 0 else exit_status))
    sys.exit(exit_status)
