# Products App

This is a Products app that consists of two microservices, one built with Django and the other with FastAPI. The microservices communicate with each other using RabbitMQ as the message broker. The app uses MySQL as the database and is containerized with Docker.

## Features

- Django microservice acts as the admin interface, allowing administrators to manage products.
- FastAPI microservice provides the main interface for users to interact with products. Users can like products, and these changes will be reflected in the admin interface.

## Prerequisites

Before running the app, make sure you have the following installed:

- Docker
- RabbitMQ
- MySQL

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Change into the project directory: `cd <project_directory>`
