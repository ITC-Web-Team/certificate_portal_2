#!/bin/bash

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.py[cod]" -delete
find . -type f -name "*$py.class" -delete

# Remove migration files (be careful with this in production)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Remove development and log files
find . -type f -name "*.log" -delete
find . -type f -name "*.sqlite3" -delete

# Remove static and media files (if not using persistent storage)
rm -rf staticfiles/
rm -rf media/

# Remove any .DS_Store files on macOS
find . -type f -name ".DS_Store" -delete

# Remove any .env.local or other local environment files
find . -type f -name ".env.local" -delete

echo "Cleanup completed successfully!" 