<!-- TOC -->
  * [Instructions](#instructions)
  * [Setting up the sqlite](#setting-up-the-sqlite)
  * [Run sqlite](#run-sqlite)
  * [Create DB in sqlite and Table](#create-db-in-sqlite-and-table)
  * [Populate data into table](#populate-data-into-table)
  * [Setting up mysql](#setting-up-mysql)
<!-- TOC -->

## Instructions
* Reference was taken from here: https://youtu.be/3vfum74ggHE?t=308
* install the prerequisites in the `Pipfile`

## Setting up the sqlite

* First install sqlite:

```linux
sudo apt install sqlite3
```

## Run sqlite
* run the command:

```linux
sqlite3
```

## Create DB in sqlite and Table
* Create a database using `my_db.sqlite` and create table `todos`.

```bash
.open my_db.sqlite

CREATE TABLE todos(                                                                                    
        id INTEGER INDEX PRIMARY KEY,                                                                           
        title STRING,                                                                                           
        complete Boolean        
);
```

## Populate data into table
```bash
INSERT INTO todos (id,title ,complete)
VALUES(45454, 'Title example number 1' ,true),(4644, 'Title example number 2' ,true),(9871, 'Title example number 3' ,false);
```

Exit by the command: `.exit` 

* copy the file: `my_db.sqlite` to the code directory.
* Run the app
* The routes is written in the app.py

<p align="center"> <!-- style="width:400px;" -->
  <img src="images/screenshot.png" title="tool tip here">
</p>

## Setting up mysql

https://blog.balasundar.com/building-a-crud-app-with-fastapi-and-mysql