=====
geodb
=====

Process base mapping data used by other modules.
Mandatory Module for ASDC

Quick start
-----------

1. Add "geodb" to your ISDC_BASE_APPS setting like this::

   ISDC_BASE_APPS = [
       ...
       'geodb',
   ]

   If necessary add "geodb" in (check comment for description): 
       QUICKOVERVIEW_MODULES, 
       MAP_APPS_TO_DB_CUSTOM

   For development in virtualenv add GEODB_PROJECT_DIR path to VENV_NAME/bin/activate:
       export PYTHONPATH=${PYTHONPATH}:\
       ${HOME}/GEODB_PROJECT_DIR

2. To create the geodb tables:

   python manage.py makemigrations
   python manage.py migrate dashboard --database geodb
