Teen Budgeting Tool Setup Guide

1. install python
   go to https://www.python.org/downloads/ and install python 3.x
   during installation, check the box that says "add python to PATH"

2. verify installation
   open command prompt or terminal and type:
   python --version
   you should see something like:
   Python 3.x.x

3. install pip (it usually comes with python)
   check if pip is installed:
   pip --version
   if it’s not found, reinstall python and make sure "add pip" is checked.

4. install visual studio code
   download from https://code.visualstudio.com/
   open the folder where your project will be stored.

5. create a new folder for your project
   example:
   mkdir teen_budget_tool
   cd teen_budget_tool

6. create a virtual environment
   python -m venv venv

7. activate the virtual environment
   windows:
   .\venv\Scripts\Activate
   mac or linux:
   source venv/bin/activate
   once active, you’ll see (venv) at the start of your command line.

8. upgrade pip (optional but good to do)
   python -m pip install --upgrade pip

9. install flask
   pip install flask

10. create a file named app.py in your project folder
    copy and paste your flask code into app.py

11. run the flask app
    python app.py
    you should see something like:
    * Running on http://127.0.0.1:5000/

12. open your browser and go to
    http://127.0.0.1:5000/

13. your teen budgeting tool should now be running.

14. to stop the server
    press ctrl + c in the terminal.

15. to start it again next time
    open the terminal, go to your project folder, activate the venv, and run:
    .\venv\Scripts\Activate
    python app.py

16. optional: create a requirements.txt file
    Flask==3.0.3
    then anyone can install everything using:
    pip install -r requirements.txt
