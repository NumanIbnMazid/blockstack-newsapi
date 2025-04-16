#!/bin/bash

# Exit on error
set -e

# Build and run the container
docker compose build --progress=plain
docker compose up -d

# Run Flake8 for PEP-8 compliance inside the container
echo "Running Flake8 for PEP-8 compliance..."
docker compose exec app flake8 .

# Run tests with pytest to ensure proper test coverage inside the container
echo "Running tests with pytest..."
docker compose exec app coverage run -m pytest --maxfail=1 --disable-warnings -q
docker compose exec app coverage report -m

echo "Code quality checks and tests completed successfully!"
