# SCVS Python Case Study

## Overview
This case study involves creating a RESTful API using FastAPI to manage customer profiles, focusing on basic CRUD operations and integrating a SQLite database.

## Project Setup

### Initial Setup
1. **Extract the provided ZIP file and navigate to the project directory**:
   ```bash
   $ unzip scvs-python-case-study.zip -d scvs-python-case-study
   $ cd scvs-python-case-study
   ```

2. Git Usage
    ```bash
    $ git init
    $ git add .
    $ git commit -m "Initial project setup"
    ```

3. Pip Install minimum requirements
    ```bash
    $ pip install -r requirements.txt
    ```


## Task Description

Below is the basic outline of the required construction that is required.The API will provide functionality to create, retrieve, update, and delete customer data stored in a SQLite database.

## Requirements
    - FastAPI: Use FastAPI as the web framework.
    - SQLite: Use SQLite for the database to store customer profiles.
    - Pydantic: Utilize Pydantic for data validation.
    - Alembic: (Optional) Use Alembic for database migrations if the candidate wishes to demonstrate additional skills.

### API Endpoints
1. Create Customer Profile
    - Method: POST
    - Endpoint: /customers/
    - Payload: {"name": "string", "email": "string", "age": int, "signup_date": "date"}
    - Functionality: Adds a new customer. Validates that signup_date is either today's date or earlier, which is not directly supported by standard Pydantic validators.

2. Retrieve Customer Profile
    - Method: GET
    - Endpoint: /customers/{customer_id}
    - Functionality: Retrieves a customer profile by ID, implementing a custom filter that checks if the customer’s signup anniversary is today.

3. Update Customer Profile
    - Method: PUT
    - Endpoint: /customers/{customer_id}
    - Payload: {"name": "string", "email": "string", "age": int}
    - Functionality: Updates an existing customer's profile with a check to ensure email format is compliant with newly introduced company-specific standards (e.g., must contain a specific domain).

4. Delete Customer Profile
    - Method: DELETE
    - Endpoint: /customers/{customer_id}
    - Functionality: Deletes a customer's profile but requires a verification step that the user making the request has admin privileges (this involves checking an API key against a list of keys stored in the database).


### Database Schema
1. Table: customers
    - Columns:
        id (INTEGER, primary key, autoincrement)
        name (TEXT)
        email (TEXT, unique)
        age (INTEGER)
        signup_date (DATE)

## Developer Tasks
1. Setup Project and Environment:
    - Initialize a new FastAPI project with essential configurations and dependencies.

2. Database Setup and Custom Functions:
    - Implement the database with SQLite and include necessary constraints.
    - Develop custom functions for unique validations and checks as required by the endpoints.

3. Develop and Test API Endpoints:
    - Code each endpoint with the custom requirements specified.
    - Write tests to validate the logic of custom implementations.

4. Documentation:
    - Produce comprehensive API documentation highlighting custom features and usage instructions.
