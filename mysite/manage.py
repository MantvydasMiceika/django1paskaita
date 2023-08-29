#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



# https://codeacademylt.sharepoint.com/sites/PythonPTU15studijos/_layouts/15/stream.aspx?id=%2Fsites%2FPythonPTU15studijos%2FShared%20Documents%2FGeneral%2FRecordings%2F2023%2D08%2D28%20%2D%20Django%20%2D%20I%2C%20II%20dalis%2D20230828%5F082913%2DMeeting%20Recording%2Emp4&referrer=Teams%2ETEAMS%2DELECTRON&referrerScenario=teamsSdk%2DopenFilePreview