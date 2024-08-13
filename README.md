# DRF-Shop

This is a non-commercial project, analogous to a marketplace, featuring:

* **User Registration, Authentication, and Authorization**: Users can register, authenticate, and manage their accounts securely.
* **Product Viewing**: Users can view all products as well as individual products by their identifier.
* **Order Creation System**: A system is implemented for creating orders.
* **Product Filtering**: Products can be filtered based on availability and discounts.
* **Product Search**: Users can search for products based on name, description, and tags.



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
   cd shop
   ```

2. Install all required packages in `Requirements` section.
3. Set up environment variables:
   - Create a `.env` file and fill it according to `.env.example`.

### Implemented Commands

* `make app` - up application and database/infrastructure, with replication database
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make migrate` - apply all made migrations
* `make createsuperuser` - run command createsuperuser

### Specific Commands

* `make storages` - up only storages. you should run your application locally for debugging/developing purposes 
* `make storages-logs` - follow the logs in storages containers
* `make storages-down` - down all infrastructure
* `make appbash` - enter into application container
* `make dbbash` - enter into database container
* `make full_clean` - clean up docker db containers with volume

___
## Structure

```plaintext
Shop/
├── .pre-commit-config.yaml
├── .flake8   
├── manage.py                    
├── .env                         # Environment variables file
├── .gitignore
├── Dockerfile                   # Dockerfile for creating the application image
├── Makefile                     # Makefile for task automation
├── README.md                    # Project documentation
├── poetry.lock
├── pyproject.toml
├── entrypoint.sh                # Docker container entry point
├── core/                        # Main Django application source code
│   ├── api/                     # All API
│   │   ├── v1/                  # version 1
│   │   │   ├── urls.py
│   │   │   ├── products/        # products app
│   │   │   │   └──handlers.py
│   │   │   ├── users/           # users app
│   │   │   │   └── handlers.py
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
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   └── migrations/
│   ├── project/                 # Project configuration for Django
│   │   ├── settings/
│   │   │   ├── local.py         # Local configuration for Django
│   │   │   ├── main.py          # Main Django configuration for Django
│   │   ├── urls.py
│   │   ├── wsgi.py              # WSGI configuration for deployment
│   │   └── asgi.py              
├── docker_compose/              
│   ├── postgres.yaml            # Docker Compose for PostgreSQL
│   ├── backup.yaml              # Docker Compose for PostgreSQL backup
│   └── app.yaml                 # Docker Compose for app
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
+ **Dependency Injection**: (Depends)

## Author
Author of the backend: ***Rybakov Artem***  (https://github.com/podrivnick)