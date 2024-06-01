# Chat Server Administration API with Front-End Integration

This project focuses on building a comprehensive chat server administration API using Django and Django REST Framework (DRF), and integrating it with a front-end built with React and Material-UI. Key features include chat services using Django Channels, token-based authentication, and a robust front-end interface.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Backend Setup](#backend-setup)
6. [Frontend Setup](#frontend-setup)
7. [API Documentation](#api-documentation)
8. [Running the Project](#running-the-project)
9. [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)

## Project Overview

This project aims to build a chat server administration API and integrate it with a front-end templating framework. It includes:
- Building a chat server administration API.
- Designing chat servers, models, and database tables.
- Creating API endpoints and documentation.
- Integrating with React and Material-UI.
- Implementing chat services with Django Channels.
- Authentication using djangorestframework-simplejwt.

## Features

- **Chat Server Administration API**: Create, update, delete, and manage chat servers.
- **API Documentation**: Filter and retrieve server-related data through well-documented API endpoints.
- **Frontend Integration**: React project setup with routing and Material-UI components.
- **API Integration**: Using Axios for API requests and configuring CORS.
- **Chat Services**: Real-time chat using Django Channels and WebSockets.
- **Authentication**: Secure login and registration using JWT.

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn
- Django 3.2+
- Django REST Framework
- Django Channels
- React 17+
- Material-UI

## Installation

### Backend Setup

1. Clone the repository:

```bash
   git clone https://github.com/yourusername/chat-server-admin.git
   cd chat-server-admin/backend
```

2. Create and activate a virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:
```bash
    pip install -r requirements.txt
```

4. Apply migrations and create a superuser:
```bash
    python manage.py migrate
    python manage.py createsuperuser
```

## API Documentation

API documentation is available at `/api/docs/` once the Django server is running. It provides detailed information on available endpoints, parameters, and responses.

## Running the Project

### Start the Backend Server

```bash
    cd backend
    python manage.py runserver
```

### Start the Frontend Server
In a new terminal, run:

```bash
    cd frontend
    npm start
    # or
    yarn start
```
The application should now be running on http://localhost:3000 for the frontend and http://localhost:8000 for the backend.

### Project Structure

chat-server-admin/
├── backend/
│   ├── chat/
│   ├── chat_admin/
│   ├── config/
│   └── ...
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   └── ...
└── README.md


### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

### License

This project is licensed under the MIT License. See the LICENSE file for details.