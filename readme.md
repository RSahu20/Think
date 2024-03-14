
1) Use a representative image of the cell (to be uploaded by the
user)
![Altextt ](https://github.com/RSahu20/Think/blob/master/media/upload.png)    


3) Generated a unique 10-digit Cell_ID and a Bar Code automatically and use
it as a unique identifier for the cell.
![Altextt ](https://github.com/RSahu20/Think/blob/master/media/barcode.png)

5) The page  have option to enter the meta information and electric parameters.
![Altextt ](https://github.com/RSahu20/Think/blob/master/media/Meta%20inforamtion.png)
![Altextt ](https://github.com/RSahu20/Think/blob/master/media/Electric.png) 

7) The webpage have an option to upload the data from a file:
![Altextt ](https://github.com/RSahu20/Think/blob/master/media/cv%20fileupload.png) 

8) After uploading the data, the webpage will transform the data to
produce the results listed below using this python library(impedance)
![Altextt ](https://github.com/RSahu20/Think/blob/master/media/Results.png) 

9)The State-of-the-Health (SoH) of the battery cell
 ![Altextt ](https://github.com/RSahu20/Think/blob/master/media/soh.png) 

## Installation 
 Use git commands to copy repo

#Create a Virtual Environment and install Dependencies.
If you don't have the virtualenv command yet, you can find installation instructions here. Learn more about Virtual Environments.
$ pip install virtualenv

#Create a new Virtual Environment for the project and activate it.

$ virtualenv venv
$ source venv/bin/activate

## Install requirements

```
pip install -r requirements.txt
```
## Database

```
Set the database from settings.py
```

## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```


## Collects all static files in your apps
```
python manage.py collectstatic
```

## Run the server
```
python manage.py runserver
```

# Main directory file

*   `battery_project`
 * `urls.py` - path reference to the app URLs
 * default django project files, such as: `settings.py`, `wsgi.py`, `asgi.py` etc.
		* `battery_app` - app directory
		


  * `static` - directory containing the JavaScript and CSS files inside the app directory within
        
  * `templates` - directory containing the HTML templates inside the app directory within
   
  * `manage.py` - default django file
  * `README.md` - this readme file
