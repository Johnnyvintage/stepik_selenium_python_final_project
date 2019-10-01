# STEPIK HOMEWORK

## Main info

It is the repository with final homework project for **_chapter 4_** from course ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/course/575)

Don't forget to check requirements and activate appropriate environment!


----
Make sure you use _Python 3.7.3_!
----
## Troubleshooting
### How to activate environment and install requirements?

1. Choose any folder
2. Open the command line
3. Create new virtual environment. Execute command:<br />`python3 -m venv env_stepik_final_project`
4. Activate virtual environment: Execute command:<br />`source env_stepik_final_project/bin/activate`
5. You will see the environment name in brackets before folder path in command line:

    > (stepik_final_project) **user@n261:~/environments$** 

6. Unzip project downloaded from GitHub (you may use Explorer)
7. In command line with activated _venv_ follow inside the folder of the project
8. Install required packages. Execute command:<br />`pip install -r requirements.txt`
9. After the end of the process you may start tests with **pytest**

### Experiencing any problems with starting tests in pytest? Try the following:

* It may be problem with `__init__.py`.
Try to change location of this file to `./pages/` directory or store this file simultaneously in **parent** and `./pages/` directory

* It may be problem with `conftest.py`.
Try to change location of the project to completely different folder (e.g. `/Downloads/`). You may use environment of any folder, but don't forget to change directory to directory of the project before start. 
