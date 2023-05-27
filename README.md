# Traceroute Visualization
Open [https://traceroute-visualization.vercel.app/](https://traceroute-visualization.vercel.app/) to access the deployed application.


This project contains a Django backend and a ReactJS frontend for a Trace Visualization Application.

## Getting Started

These instructions will guide you on how to run the application on your local machine for development and testing purposes.

### Prerequisites

- Python
- Node.js
- Pipenv (for managing Python dependencies)
- npm (comes with Node.js, for managing JavaScript dependencies)

You can check the versions you have installed by running:

`python3 --version`

`node --version`

`npm --version`

`pipenv --version`

### Directory Structure

The repository is divided into two main parts:

1. `trace-viz-backend`: This directory contains the Django backend.
2. `trace-viz-frontend`: This directory contains the ReactJS frontend.

## Setting up the Backend

The following steps will help you setup the Django backend on your local machine:

1. Navigate to the `trace-viz-backend` directory:

    `cd trace-viz-backend`

2. Install the required Python dependencies using Pipenv:

    `pipenv install`

3. Activate the Pipenv shell:

    `pipenv shell`

4. Run the Django migrations to setup your database:

    `python manage.py migrate`

5. Start the Django server:

    `python manage.py runserver`

By default, the server will start on http://127.0.0.1:8000/

**Note:** To fetch locations of ip addresses we are using ipapi.com, which has a limit of 1000 requests in free account. If you see only private addresses on running traceroute that implies 1000 limit is reached. You can create your own account in ipapi.com and just replace key in locations.py file in backend.

## Setting up the Frontend

The following steps will help you setup the ReactJS frontend on your local machine:

1. Navigate to the `trace-viz-frontend` directory:

    `cd ../trace-viz-frontend`

2. Install the required Node.js dependencies:

    `npm install`

3. Start the React development server:

    `npm run dev`

By default, the server will start on http://localhost:5173/

## Running the Application

Open http://localhost:5173 in your web browser to access the frontend of the application. The frontend will communicate with the backend, which is running on http://127.0.0.1:8000/


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
