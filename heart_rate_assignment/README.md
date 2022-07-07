For this assignment, I used Python Interpreter version 3.10.5 on a Windows machine.
I have also used the module prettytable, version 3.3.0.

Note that all commands are done via the terminal.

1. Open the project in its designated folder.

If you have a different Python Interpreter, delete the venv folder and continue with 
step 2. Otherwise, continue with step 5.

Optional step: In case you do not have virtualenv installed, you can do so via the
command: `pip install --user virtualenv`. Note that this is required for the following
steps to come.

2. Create a virtual environment: `python -m virtualenv venv`. Where venv is the name
of the virtual environment.

3. Activate the virtual environment, via the command: `venv/Scripts/activate`. Note that
if you are using Pycharm the command will work. However, if you are using VSCode, you
need to use: `./venv/Scripts/activate`.

Note: If you get an error saying that the activation script is not digitally signed,
then you can run:`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in the 
terminal to fix this.

4. Now that we are inside the venv, we install the modules from the requirements.txt.
This is done via the command: `pip install -r requirements.txt`

5. Run the program with the command: `python heart_rate.py`. Note that you can also run
with python3 or py, depending on what Python executable you chose for your 
installation.