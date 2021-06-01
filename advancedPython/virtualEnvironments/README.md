## Creating Virtual Environments

[Document](https://docs.python.org/3/library/venv.html)

#### Step one
`which` will locate a program file in the user's path
You can also check `python2`, `python3`
```commandline
which python
```

To create a virtual environment. First, we'll need to install a dependency for this linux machine:

```commandline
apt-get install python3-venv -y
```

Creation of virtual environments is done by executing the command venv:

```commandline
python3 -m venv /path/to/new/virtual/environment
```

To create the virtual environment running specifically on Python version 3.5. To avoid confusion we can use the -m flag to specify the verison of the Python runtime we'd like to use:
```commandline
python3.5 -m venv venv
```
Running the `ls` command will show a new directory with our virtual environment runtime. Next, we'll learn how we can use this virtual environment.


#### Step two

In a previous step, we created a new virtual environment directory using the `venv` module. We can now use the BASH `source` command to tell the terminal to use the virtual environment runtime. To change your python alias to point to the virtual environment runtime, run:

```commandline
source venv/bin/activate
```
Now if we run the which python command, we can observe that it points to the virtual environment directory! You can now install dependencies using pip as usual, but they will instead be installed to your virtual environment directory:
```commandline
which python

pip install numpy
```
To exit the virtual environment, and instead use your system's default python runtimes, run:
```commandline
deactivate
```
*alias*: a bash concept which links a keyword to a command in the command line.

#### Step three

Let's launch into the virtual environment runtime with:

```commandline
python
```
As we've done before, let's now see where the numpy module is being imported from:
```
import numpy
numpy
exit()
```

We'll observe that this numpy installation is now pointing to our virtual environment's site-packages directory!

###### Managing State

We can easily print all of the installed libraries by running:
```bash
pip freeze
```

It's common practice to save this state to a file called `requirements.txt` using the following bash command:
```bash
pip freeze > requirements.txt
```

The `>` operator will save the command line output to a file, in this case named `requirements.txt`. 

We would then be able to reinstall all of the dependencies locked at a specified version using:

```bash
pip install -r requirements.txt
```

Delete the virtual environment by running: 
```commandline
rm -rf venv(the name)
```
