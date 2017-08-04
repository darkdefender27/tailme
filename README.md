tailme
======

Follow the below steps to run the application.


### Clone

- Make sure your Internet is working. :)
- Clone this repo by typing ::

```sh
$ git clone https://github.com/darkdefender27/tailme.git tailme
$ cd tailme/
```

### Installation

- Install Virtual Environment using the following command ::

```sh
$ brew install python-virtualenv
```

- Create a Virtual Environment ::

```sh
$ virtualenv /path/to/virtualenv
```

- Activate the virtualenv using the command ::

```sh
$ source /path/to/virtualenv-name/bin/activate
```

- Change the directory to the `tailme/` project using the command ::

```sh
$ cd /path/to/tailme
```
- Install pre-requisites using the command ::

```sh
$ pip install -r Requirements.txt
```
  or you can also type ::

```sh
$ easy_install `cat requirement.txt`
```

### Execution

```sh
$ python manage.py runserver
```



### License

GNU GPL Version 3, 29 June 2007.

Please refer this `link <http://www.gnu.org/licenses/gpl-3.0.txt>`_
for detailed description.
