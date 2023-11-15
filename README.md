# Instructions

* install the prerequisites in the `Pipfile`

## Setting up the sqlite

* First install sqlite:

```linux
sudo apt install sqlite3
```

* run the command:

```linux
sqlite3
```

* Create a database using `my_db.sqlite` and create table `todos`.

```commandline
.open my_db.sqlite

CREATE TABLE todos(                                                                                    
        id INTEGER INDEX PRIMARY KEY,                                                                           
        title STRING,                                                                                           
        complete Boolean        
);
```

* copy the file: `my_db.sqlite` to the code directory.