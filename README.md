# a2o_technical_test
# Description
This repository is a technical trial for a2o dev.
# Tech Stack and Packages Installed
Django: This is the backbone of the backend api, and has the following packages installed:

Django Rest Framework (For the Rest API)
Django-Cors-Headers (For the CORS config to allow React js to make calls)

Note: All this packages are specified in the requirements.txt file inside the django_backend folder. Links to their official documentation can be found at the Useful Links section.

React: The frontend library in use. This was created via npx create-react-app. The only extra packages that were installed (ignoring the ones that are automatically pre-installed) are:

MUI  (For styling)
Axios (To make calls to the Django Backend)
React-Router-Dom and Router-Dom (For managing routing)

# Install (Run) with Docker
bBfore install make sure you have installed docker compose in your enviroment
Clone the repo:

git clone https://github.com/jdavisd/a2o_technical_test.git
Copy a default setup of the environment variables for the project:


Run Docker-Compose:

docker-compose up -d --build
Congratulations !!! The app should be up and running. To access the React frontend go to localhost:3000, and to access the Django backend go to localhost:8000/api. F


