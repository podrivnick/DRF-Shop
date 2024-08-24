# DRF-Shop

This is a non-commercial project, analogous to a marketplace, featuring:

* **User Registration, Authentication, and Authorization**: Users can register, authenticate, and manage their accounts securely.
* **Product Viewing**: Users can view all products as well as individual products by their identifier.
* **Order Creation System**: A system is implemented for creating orders.
* **Product Filtering**: Products can be filtered based on availability and discounts.


### Installation and Running

These instructions will help you run the project.

## Requirements

Ensure you have the following software installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

___
## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/podrivnick/DRF-Shop.git
   cd DRF-Shop
   ```

2. Install all required packages in `Requirements` section.
3. Set up environment variables:
   - Create a `.env` file and fill it according to `.env.example`.

### Implemented Commands

* `make app` - up application and database/infrastructure, with replication database
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make collectstatic` - collect all static files
* `make migrate` - apply all made migrations
* `make createsuperuser` - run command createsuperuser

### Specific Commands

* `make storages` - up only storages. you should run your application locally for debugging/developing purposes 
* `make storages-logs` - follow the logs in storages containers
* `make storages-down` - down all infrastructure
* `make monitoring` - up APM Elastic application
* `make monitoring-logs` - logs of APM Elastic container
* `make monitoring-down` - down APM Elastic application
* `make appbash` - enter into application container
* `make dbbash` - enter into database container
* `make full_clean` - clean up docker db containers with volume
* `make runtest` - run tests for main application

___
## Structure

```plaintext
DRF-Shop/
├── .pre-commit-config.yaml
├── .flake8
├── .env                         # Environment variables file
├── .gitignore
├── manage.py
├── pytest.ini                   # Initialize the test
├── Dockerfile                   # Dockerfile for creating the application image
├── Makefile                     # Makefile for task automation
├── README.md                    # Project documentation
├── poetry.lock
├── pyproject.toml
├── entrypoint.sh                # Docker container entry point
├── core/                        # Main Django application source code
│   ├── api/                     # All API
│   │   ├── v1/                  # version 1
│   │   │   ├── orders/          # orders app
│   │   │   │   └──handlers.py
│   │   │   ├── products/        # products app
│   │   │   │   └──handlers.py
│   │   │   ├── users/           # users app
│   │   │   │   └── handlers.py
│   │   │   urls.py
│   │   └── base_response.py
│   ├── apps/                    # Django applications (modules)
│   │   ├── common/              # Common app, for base utils and classes
│   │   │   ├── apps.py
│   │   │   ├── models.py        # Time base models
│   │   │   ├── utils/
│   │   │   │   └── repository.py
│   │   │   └──  base_exceptions # Base custom exception class
│   │   ├── products/            # Product app
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models/
│   │   │   │   └── products.py
│   │   │   ├── serializers/
│   │   │   │   └── products.py
│   │   │   ├── exceptions/
│   │   │   ├── services/
│   │   │   └── migrations/
│   │   ├── users/               # User management module
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── exception.py
│   │   │   ├── serializers.py
│   │   │   ├── service.py
│   │   │   ├── dependencies/
│   │   │   └── migrations/
│   │   ├── orders/              # Order management module
│   │   │   ├── config/
│   │   │   ├── exceptions/
│   │   │   │   ├── base_order_exception.py     # BaseExceptionOrder
│   │   │   │   ├── database_orders_exceptions.py     # Orders create exceptions
│   │   │   │   └── validation_orders_exceptions.py.     # Validaton Order
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   ├── schemas/
│   │   │   ├── serializers/
│   │   │   ├── services/
│   │   │   ├── use_cases/
│   │   │   └── utils/           # All Spec's for validation order
│   ├── project/                 # Project configuration for Django
│   │   ├── settings/
│   │   │   ├── local.py         # Local configuration for Django
│   │   │   ├── main.py          # Main Django configuration for Django
│   │   ├── middlewares.py       # Middleware configuration for Elasticsearch
│   │   ├── cantainers.py        # Dependency Injection
│   │   ├── urls.py
│   │   ├── wsgi.py              # WSGI configuration for deployment
│   │   └── asgi.py
├── docker_compose/
│   ├── postgres.yaml            # Docker Compose for PostgreSQL
│   ├── backup.yaml              # Docker Compose for PostgreSQL backup
│   ├── monitoring.yaml              # Docker Compose for ElasticSearch
│   └── app.yaml                 # Docker Compose for app
├── tests/                       # All tests
│   ├── unit/
│   │   ├── services/            # Test services
│   │   │   ├── conftest.py
│   │   │   ├── test_create_orders.py
│   │   │   ├── test_products.py
│   │   │   └── test_validate_data_orders.py
│   │   └── factories/           # Factory model for tests
│   │       └── products.py
```

## Technology
+ **DRF**
+ **Python**
+ **Docker**

___
## Design Patterns
+ **Adapter**
+ **Repository Pattern**
+ **Configuration Management** (dotenv)
+ **Factory Pattern**
+ **Dependency Injection**: (punq)
+ **Specification Pattern**

## Author
Author of the backend: ***Rybakov Artem***  (https://github.com/podrivnick)