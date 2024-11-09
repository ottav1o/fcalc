import gi
gi.require_version('Gtk', '4.0')

from gi.repository import Gtk as gtk
from gi.repository import GLib as glib
from gi.repository import Gio as gio

import math

from .. import commons

class MainWindow(gtk.ApplicationWindow):
    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        glib.set_application_name('School Absenses Calculator')

        self.set_resizable(False)

        self.main_box = gtk.Box(orientation=gtk.Orientation.VERTICAL)
        self.main_box.set_spacing(10)
        self.main_box.set_margin_top(10)
        self.main_box.set_margin_bottom(10)
        self.main_box.set_margin_start(10)
        self.main_box.set_margin_end(10)

        self.wdays_lbl = gtk.Label(label=commons.lang['WorkingDaysMsg'])
        self.wdays_entry = gtk.Entry()

        self.lper_day_lbl = gtk.Label(label=commons.lang['LessonsPerDayMsg'])
        self.lperday_entry = gtk.Entry()

        self.calc_btn = gtk.Button(label=commons.lang['CalcButtonMsg'])
        self.advanced_btn = gtk.Button(label=commons.lang['AdvancedMsg'])

        self.main_box.append(self.wdays_lbl)
        self.main_box.append(self.wdays_entry)
        self.main_box.append(self.lper_day_lbl)
        self.main_box.append(self.lperday_entry)
        self.main_box.append(self.calc_btn)
        self.main_box.append(self.advanced_btn)

        self.calc_btn.connect('clicked', self.calculate_max_absences)

        self.set_child(self.main_box)

    def calculate_max_absences(self, button):
        wdays = self.wdays_entry.get_text()
        lperday = self.lperday_entry.get_text()
        if wdays and lperday:
            wdays = int(math.ceil(float(wdays)))
            
            lperday = int(math.ceil(float(lperday)))
            commons.logger.info(f'Working days: {wdays}, Lessons per day: {lperday}')
                
            dialog = gtk.AlertDialog()

            dialog.set_message(commons.lang['OpResultMsg'])
            dialog.set_detail(f'{commons.lang['ResultMsg'][0]} {int(((wdays * lperday) / 100) * 25 / lperday)} {commons.lang['ResultMsg'][1]}')
            dialog.set_modal(True)
            dialog.show()
        
        else:
            dialog = gtk.AlertDialog()

            dialog.set_message(commons.lang['OpResultMsg'])
            dialog.set_detail(commons.lang['ErrNaN'])
            dialog.set_modal(True)
            dialog.show()


class Application(gtk.Application):
    def __init__(self, *args, **kargs) -> None:
        super().__init__(
            *args, 
            application_id=commons.APP_ID,
            **kargs,
        )

        self.window = None
    
    def do_activate(self):
        if not self.window:
            self.window = MainWindow(application=self, title=commons.lang['WinTitle'])

        self.window.present()