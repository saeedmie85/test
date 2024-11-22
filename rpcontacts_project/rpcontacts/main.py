# -*- coding: utf-8 -*-
# rpcontacts/main.py

"""This module provides RP Contacts application."""

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window
from .database import createConnection
from PyQt5.QtSql import QSqlQuery


def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)

    if not createConnection("contacts.sqlite"):
        sys.exit(1)

    # insertDataQuery = QSqlQuery()
    # insertDataQuery.prepare(
    #     """
    #     INSERT INTO contacts (
    #         name,
    #         job,
    #         email
    #     )
    #     VALUES (?, ?, ?)
    #     """
    # )
    # data = [
    #     ("Linda", "Technical Lead", "linda@example.com"),
    #     ("Joe", "Senior Web Developer", "joe@example.com"),
    #     ("Lara", "Project Manager", "lara@example.com"),
    #     ("David", "Data Analyst", "david@example.com"),
    #     ("Jane", "Senior Python Developer", "jane@example.com"),
    # ]

    # # Insert sample data
    # for name, job, email in data:
    #     insertDataQuery.addBindValue(name)
    #     insertDataQuery.addBindValue(job)
    #     insertDataQuery.addBindValue(email)
    #     insertDataQuery.exec()

    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
