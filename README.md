### Steps:



1. create a virtual env:

```python3.10 -m venv venv```

2. Activate the virtual env:

```source venv/bin/activate```

3. Run requirements:

```pip install -r requirements.txt```

4. Run the api with :

```uvicorn main:app --reload```

5. Create table user with columns:

    CREATE TABLE users (
        id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(20) UNIQUE,
        usermail VARCHAR(30) UNIQUE,
        credit_card_number VARCHAR(150),
        created_at TIMESTAMP ,
    )

Acces Mongo web:

``` Mail :  gatab99977@hempyl.com ```
``` Pass: Meli2022*```
