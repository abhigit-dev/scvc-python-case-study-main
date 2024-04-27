import time
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .main import app, database

# Create a test client
client = TestClient(app)

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db function to return a test database session
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

# Create a fixture for database transactions
@pytest.fixture
def db_transaction():
    session = TestingSessionLocal()
    session.begin_nested()
    yield session
    session.rollback()

@pytest.fixture
def created_customer(db_transaction):
    unique_email = f"Pieter.Suger{time.time()}@gmail.com"
    response = client.post(
        "/customers/",
        json={"name": "Pieter Suger", "email": unique_email, "age": 30, "signup_date": "2024-04-27"},
    )
    data = response.json()
    return data

# Test creating a customer
def test_create_customer(created_customer):
    unique_email = f"John.Paul+{time.time()}@gmail.com"
    response = client.post(
        "/customers/",
        json={"name":"John Paul", "email": unique_email, "age": created_customer['age'], "signup_date": created_customer['signup_date']},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Paul"
    assert data["email"] == unique_email
    assert data["age"] == created_customer['age']
    assert "id" in data

# Test reading all customers
def test_read_all_customers():
    response = client.get("/customers")
    assert response.status_code == 200

# Test reading a customer
def test_read_customer(created_customer):
    response = client.get(f"/customers/{created_customer['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == created_customer['name']
    assert data["email"] == created_customer['email']
    assert data["age"] == created_customer['age']
    assert data["id"] == created_customer['id']

# Test updating a customer
def test_update_customer(created_customer):
    response = client.put(
        f"/customers/{created_customer['id']}",
        json={"name": created_customer['name'], "email": created_customer['email'], "age": created_customer['age']},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == created_customer['name']
    assert data["email"] == created_customer['email']
    assert data["age"] == created_customer['age']
    assert data["id"] == created_customer['id']

# Test deleting a customer
def test_delete_customer(created_customer):
    response = client.delete(f"/customers/{created_customer['id']}")
    assert response.status_code == 204
    print("CustomerId: {created_customer['id']}")