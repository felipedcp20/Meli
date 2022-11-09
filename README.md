 ### Steps To run in Local:
for run the app need create a file .env with the next items:

```
db_mongo_url = mongodb+srv://<user>:<password>@cluster0.37dqxrv.mongodb.net/?retryWrites=true&w=majority
dm_mongo_username = meli
db_mongo_password =  Ek4wyzghzmYkmbgo
key_encriptor = JJfmeevTgp5haMjiN0fd8gMWCoMg0ObMGuDYQ_B1LgE=
```

1. create a virtual env:
```
python3.10 -m venv venv
```

2. Activate the virtual env:
```
source venv/bin/activate
```

3. Run requirements:
```
pip install -r requirements.txt
```

4. for run the app use the next command after install requeriments:

```
uvicorn main:app --reload
```

 ### Instructions to create Mysql Database for use the app:

 1. create a database Mysql (local or in something host) with user and passwotd
 2. login in the mysql database:
    ```mysql -u root -p```
 3. create the datatabase for the example:
    ```CRREATE DATABASE meli```
 4. after to create de databe you need create a table:
    ```
    CREATE TABLE users (
        id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(20) UNIQUE,
        usermail VARCHAR(30) UNIQUE,
        credit_card_number VARCHAR(150),
        created_at TIMESTAMP ,
    )
    ```
5. the API only use the name of the columns for create a clasification **so we will not insert records into the tables.**
6. the creation of the table that stores the results of the classifications is created in **MongoDb** directly from the code and credentials are also attached to access the closter via the web:
     ```
     Mail :  gatab99977@hempyl.com
     Pass: Meli2022*
    ```
    ![](https://i.ibb.co/6mLmS4M/mongodb.png)

### Documentation For USE API:
this **Api** uses 5 endpoints for the whole database classification process, it was developed with **FastApi** we can use its automatic documentation (**openapi**) to test the endpoints described below:

**to use the automatic documentation we place a /docs at the end of the api url and we will visualize the Endpoints  Example**:
     ```
    http://127.0.0.1:8000/docs
    ```
    ![](https://i.ibb.co/pXBTvqP/openapi.png)

### endpoint Root:
```
http://127.0.0.1:8000/
```
This endpoint return the version name of the service and the version:
```
{
  "service": "Meli",
  "version": "1.0"
}
```
![](https://media1.tenor.com/images/b543c7dd3e11e34da7908fed37df32ae/tenor.gif?itemid=27066230)
