# Holberton AirBnB clone project #

<img  width="521"  alt="image"  src="https://user-images.githubusercontent.com/53787841/86299550-29f40c80-bbc6-11ea-9e54-089ffdc7b4cf.png">


For further information, click on the previous link.

## Airbnb Clone - Structure

![consdole](https://user-images.githubusercontent.com/60367280/86426731-ff7d7e80-bcad-11ea-9ba2-484a6c9a653b.png)

##### In this project, we implement the following: #####

- BaseModel class for instantation of AirBnB clone objects
- User, State, City, Place, Amenity, Review subclasses that inherit from BaseModel
- Serialization/deserialization of instances
- A storage engine for the project: FileStorage
- A console/command interpreter where we can instantiate, store, destroy, and update attributes of objects, as well as print out the string representation of those objects

### The Console ###
The code for the command interpreter is in console.py
To start the console, type ./console.py or python3 console.py in the directory console.py is in. This will make the command prompt (hbnb) appear on your terminal.

`
$ ./console.py
`
`
(hbnb) 
`

Usage
The console accepts the following commands: EOF (CTRL+D), quit, create, show, destroy, all, and update.

Command completion and command history are supported.

Entering <TAB> will autocomplete or show you the options for autocompletion.
`
(hbnb) <TAB>
`
`
EOF      count    destroy  quit     update
all      create   help     show
`

## Environment

Ubuntu 14.04 LTS via Vagrant in VirtualBox and Interpret Python3

## More Info

-   But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Available commands: ###

| command  | Explanation |
-- | --
| all |	Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel |
| create | Creat```
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" |

### Alternative command input ###
| Alternative command | Example |
-- | --
| CLASS_NAME.all() | City.all() |
| CLASS_NAME.count() | User.count() |
| CLASS_NAME.destroy(ID) | Place.destroy(1234-1234-1234-1234) |
| CLASS_NAME.show(ID) | Amenity.show(1234-1234-1234-1234) |


### Example
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

### AUTHORS: ###

-   [GitHub - Santiago Agudelo](https://github.com/RedLyon1200)
-   [GitHub - Deiwin Monsalve](https://github.com/Deiwin-Ignacio-Monsalve-Altamar)
