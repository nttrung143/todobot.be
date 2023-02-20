#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(
    os.path.dirname(__file__), '.env'), verbose=True)


def main():
    """Run administrative tasks."""
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
    if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

    if sys.argv[1:2] == ['runserver']:
        while True:
            try:
                if os.environ.get('DJANGO_SETTINGS_MODULE') == 'main.settings.docker':
                    connection = psycopg2.connect(
                        dbname='postgres',
                        user='postgres',
                        password='postgres',
                        host='db',
                        port=5432
                    )
                else:
                    connection = psycopg2.connect(
                        dbname=os.environ.get('POSTGRES_DB'),
                        user=os.environ.get('POSTGRES_USER'),
                        password=os.environ.get('POSTGRES_PASSWORD'),
                        host=os.environ.get('POSTGRES_HOST'),
                        port=os.environ.get('POSTGRES_EXPOSE_PORT')
                    )

                if connection.closed == 0:
                    break
                time.sleep(1)
            except psycopg2.OperationalError:
                time.sleep(1)
                print("DB is not yet ready. Retry")
                pass
    main()
