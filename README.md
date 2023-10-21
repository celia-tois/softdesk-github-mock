# Softesk - API
***
The Softdesk API allow the user to create projects, add contributors to specific projects, create issues related to the project and add comment to the issues.
## How to install the project
1. Open the Terminal
2. Clone the repository:
```
$ git clone https://github.com/celia-tois/softdesk-github-mock.git
```
3. Go to the project folder:
```
$ cd ../path/to/the/file
```
4. Create the **virtual environment**:
```
python3 -m venv env
```
5. Activate the **virtual environment**:
   - on macOS and Linux:
     ```
     source env/bin/activate
     ```
   - on windows:
     ```
     env/Scripts/activate
     ```
6. Install the packages:
```
$ pip install -r requirements.txt
```
7. Go the app folder:
```
$ cd softdesk
```
8. Create the database:
```
$ python manage.py migrate
```


## How to run the app
1. Open the Terminal
2. Go to the project folder:
```
$ cd ../path/to/the/file
```
3. Activate the virtual environment
4. Run the command:
```
$ python manage.py runserver
```
5. Open the link written in your terminal or copy/paste it in your browser or in POSTMAN: http://127.0.0.1:8000/


## How to use the API
See the POSTMAN documentation: https://documenter.getpostman.com/view/23860920/2s8479yG4m
