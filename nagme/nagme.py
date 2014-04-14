#!/usr/bin/env python
# coding: utf-8

import enaml
from enaml.qt.qt_application import QtApplication
from PyQt4.QtCore import QTimer

#from models.model import Person


def f():
    print 'test'

if __name__ == '__main__':
    with enaml.imports():
        from views.view import Main

    #john = Person(first_name='John', last_name='Doe')

    app = QtApplication()

    # Create a QTimer
    timer = QTimer()
    # Connect it to f
    timer.timeout.connect(f)
    # Call f() every 2 seconds
    timer.start(2000)

    #view = PersonView(person=john)
    view = Main()
    view.show()

    view.center_on_screen()

    app.start()

