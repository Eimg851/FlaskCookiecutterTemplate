==============
flask_platform
==============


.. image:: https://img.shields.io/pypi/v/dummyapp.svg
        :target: https://pypi.python.org/pypi/dummyapp

.. image:: https://img.shields.io/travis/Eimg851/dummyapp.svg
        :target: https://travis-ci.org/Eimg851/dummyapp

.. image:: https://readthedocs.org/projects/dummyapp/badge/?version=latest
        :target: https://dummyapp.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Flask application to show basic system information


* Free software: GNU General Public License v3
* Documentation: https://dummyapp.readthedocs.io.


## Running the Flask

It is assumed that the user has the latest version of Anaconda installed on their machine.

1. Create a virtual environment on the command line using the following command:
```
conda create -n <place your env name here> python
```
  
  

2. Activate the virtual environment:
    - For Mac users:         ```source activate <place your env name here>```
    - For Windows users:       ```activate <place your env name here>```
   
   
   
3. Install flask on the virtual environment:
``` 
pip install flask
```
    
    
    
4. Install the systeminfo file from the [systeminfo GitHub repository](https://github.com/Eimg851/systeminfo.git)
    - or use the following command:
```
pip install git+https://github.com/Eimg851/SysteminfoCookiecutterTemplate.git
```
 
 
 
5. Git clone the flask application to you machine:
```
git clone https://github.com/Eimg851/FlaskCookiecutterTemplate.git
```
  
  
  
6. Run the flask application:
``` 
python dummyapp/run.py
```
  
  
  
7. Open a web browser and navigate to localhost:5000 to view the flask application running on a webserver. You should see the platform on which the flask application is running along with total, used and free storage. 


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
