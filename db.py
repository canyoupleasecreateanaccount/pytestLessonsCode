from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from configuration import CONNECTION_ROW

"""
Создаём модель для того, чтобы потом использовать её для описания наших таблиц.

Here we creates model. It needs for future using and table describing.
"""
Model = declarative_base(name='Model')


"""
Создаём коннекшен к нашей базе данных, передавая ему креденшеналы и другую 
информацию для этого. Пример коннекшен строки вы можете найти в файле 
configuration.py.

In next row we creates connection to our database. It receives credential and 
another info about connection. More info and full connection sting example 
you can find in configuration.py.
"""
engine = create_engine(
    CONNECTION_ROW
)

"""
Создаём экземпляр сессии, которая даст нам возможность каждый раз генерировать
новую сессию.

We create instanse of session maker, that gives possibility to create fresh 
database session.
"""
Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

