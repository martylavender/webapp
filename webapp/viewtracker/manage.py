#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "viewtracker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Added this to see if importing really is caused by Django / masking other exceptions with Python 2
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django."
            )
        raise
    execute_from_command_line(sys.argv)
