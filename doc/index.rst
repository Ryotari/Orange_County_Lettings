.. Orange County Lettings documentation master file, created by
	sphinx-quickstart on Tue Sep  5 17:36:09 2023.
	You can adapt this file completely to your liking, but it should at least
	contain the root `toctree` directive.

Welcome to Orange County Lettings's documentation!
==================================================

.. toctree::
	:maxdepth: 2
	:caption: Contents:

===========
The Project
===========
**OpenClassrooms Python Developer Project #13: Scale a Django Application Using Modular Architecture**

This project is a modified version of the `Python OC Lettings FR <https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git>`_.


Improvements brought:

#. Technical debt refactor.
#. Modular architecture refactor.
#. Application and error monitoring via Sentry.
#. CI/CD pipeline using `CircleCI <https://circleci.com/>`_ and deployment to `Heroku <https://www.heroku.com/>`_.


=================
Local development
=================
**Prerequisites**

* GitHub account with read access to this repository
* Git CLI
* SQLite3 CLI
* Python interpreter, version 3.6 or higher

Throughout the local development documentation, it is assumed that the python command in your OS shell runs the above-mentioned Python interpreter (unless a virtual environment is activated).

**Links**

* `Heroku for this project <https://lettings-oc-cpoinhos-4c44e940bafb.herokuapp.com/>`_
* `DockerHub Images <https://hub.docker.com/r/ryotari/oc_13_lettings>`_
* `CircleCI for this project <https://app.circleci.com/pipelines/github/Ryotari/Orange_County_Lettings>`_


**Clone the repository**

.. code-block:: powershell

	$ cd /path/to/put/project/in
	$ git clone https://github.com/Ryotari/Orange_County_Lettings.git


**Create the virtual environment**

.. code-block:: powershell

	$ cd /path/to/Python-OC-Lettings-FR
	$ python -m venv venv

Activate the environment with (Windows):

.. code-block:: powershell

	$ venv\Scripts\activate

Or (MacOS and Linux):

.. code-block:: powershell

	$ source venv/bin/activate

To deactivate the environment:

.. code-block:: powershell

	$ deactivate


**Run the app**

.. code-block:: powershell

	$ cd /path/to/Python-OC-Lettings-FR
	$ venv\Scripts\activate
	$ pip install --requirement requirements.txt
	$ python manage.py runserver

Go to `Localhost <http://localhost:8000>`_

**Linting**

.. code-block:: powershell

	$ flake8

**Tests**

.. code-block:: powershell

	$ pytest


**Docker**

Download and install `Docker <https://docs.docker.com/get-docker/>`_
Go to the project directory and build the image:

.. code-block:: powershell

	$ docker build -t <image-name> .


Run the image:

.. code-block:: powershell

	$ docker run -dp 8000:8000 <image-name>

Click on the affected port on Docker Desktop


**Sentry**

After creating a Sentry account, set up a new Django project. You can find the Sentry_DSN into *Project Settings* > *Client Keys*.
Copy the DSN and replace the DSN in the settings.py file.

==========
Deployment
==========
**Prerequisites**

In order to perform the deployment and continuous integration of the app, you need:
* `CircleCI account <https://circleci.com/>`_
* `GitHub account <https://github.com/>`_
* `Docker account <https://www.docker.com/>`_
* `Heroku account <https://www.heroku.com/>`_
* `Sentry account <https://sentry.io/welcome/>`_

The deployment of the app is automated by the CircleCI pipeline. When updates are pushed to the GitHub repository, the pipeline triggers tests and linting. If updates are made on the master branch, and if the tests and linting pass, it builds a Docker image and pushes it to DockerHub. If the Docker image is pushed, the pipeline then deploys the app on Heroku.


**Configuration**

Set up a new project on CircleCI via "Set Up Project". Select the master branch as a source for the .circleci/config.yml file.

Set up the environment variables (Project Settings > Environment Variables):

* DJANGO_SECRET_KEY : Django secret key. Use:

.. code-block:: powershell

	$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

* DOCKER_LOGIN : Your Docker account username.
* DOCKER_PASSWORD : Your Docker account password.
* DOCKER_REPO : The DockerHub repository name.
* HEROKU_APP_NAME : The Heroku app name that will be deployed. Change it everytime; you will receive an error when running th pipeline if the name is already an existing app.
* HEROKU_TOKEN : The Heroku API Key. You can find it in your Heroku account settings.
