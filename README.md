# Zameen Assessment


## Description

This is the solution of GitHub Gist API project. I have attempted this project using Python's Flask Web framework. Additionally, I have used Bootstrap for a little polished look of the web page.


## Technologies

* Python Programming Language
* Flask Web Framework
* HTML
* CSS
* Bootstrap


## Files

**Description of the project files:**

* `run.py`: Entry point of the application. Contains the endpoints of the Flask server.
* `helpers.py`: Contains implementation of helper methods.
* `index.html`: Front-end of this application.


## RUN the project

**Installation via `requirements.txt`:**

```shell
$ cd <path/to/project/>
$ sudo apt install python3-venv
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 run.py
```
Open the following link to open the web page
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)




## Optimizations/Suggestions

**Front-End**

* Use gist names in the gists list instead of gist ids
* Dropdown/Collapse can be used for Files/Forks list
* Use modal to display the contents of the file
* Use pagination for a better user experience

**Back-End** 

* Handle results per page in the (Gists/Forks)API response.






