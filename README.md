# Holberton AirBnB clone project #

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

### Available commands: ###

| command  | Explanation |
-- | --
| all |	Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel |
| create | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel |
| show | Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234 |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" |

### Alternative command input ###
| Alternative command | Example |
-- | --
| CLASS_NAME.all() | City.all() |
| CLASS_NAME.count() | User.count() |
| CLASS_NAME.destroy(ID) | Place.destroy(1234-1234-1234-1234) |
| CLASS_NAME.show(ID) | Amenity.show(1234-1234-1234-1234) |


### AUTHORS: ###
