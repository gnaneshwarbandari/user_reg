import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Clear all migration folders and delete the SQLite database'

    def handle(self, *args, **kwargs):
        # 1. Delete SQLite database file (if using SQLite)
        db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        if os.path.exists(db_path):
            self.stdout.write(f"Deleting database file: {db_path}")
            os.remove(db_path)
        else:
            self.stdout.write(f"Database file not found: {db_path}. If using MySQL/PostgreSQL, delete the database manually.")

        # 2. Loop through all apps and delete migration folders
        for root, dirs, files in os.walk(settings.BASE_DIR):
            if 'migrations' in dirs:
                migration_dir = os.path.join(root, 'migrations')
                self.stdout.write(f"Found migrations directory: {migration_dir}")

                # Delete the entire migrations folder
                shutil.rmtree(migration_dir)
                self.stdout.write(f"Deleted migrations directory: {migration_dir}")

        self.stdout.write(self.style.SUCCESS("Migrations folders and database have been cleared."))
