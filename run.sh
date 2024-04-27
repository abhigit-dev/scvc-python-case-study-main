#!/bin/bash

# Check if the virtual environment is activated, if not, attempt to activate it
# if [[ "$VIRTUAL_ENV" == "" ]]
# then
#     echo "Activating virtual environment..."
#     source venv/bin/activate
# fi

# trap 'exit 0' SIGTERM
# alembic upgrade heads

# Start Uvicorn with live reload enabled for development
echo "Starting FastAPI server with Uvicorn..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload