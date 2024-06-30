# Lunch Voting System

This is a Django REST Framework project that implements a lunch voting system.

## Features

- User authentication
- CRUD operations for Restaurants and Menus
- Daily menu viewing
- Voting system


## Running the Server

To start the development server, run:

```
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

## API Endpoints

- `/users/` - User management
- `/restaurants/` - Restaurant management
- `/menus/` - Menu management
  - `/menus/current-day/` - Get menus for the current day
- `/votes/` - Vote management
  - `/votes/results/` - Get voting results for the current day

## Usage

1. Log in using your superuser credentials or create a new user.
2. Use the `/restaurants/` endpoint to add restaurants.
3. Use the `/menus/` endpoint to add menus for restaurants.
4. Users can view the current day's menus using the `/menus/current-day/` endpoint.
5. Users can vote for their preferred menu using the `/votes/` endpoint.
6. View the voting results for the current day using the `/votes/results/` endpoint.