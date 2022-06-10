from sqlalchemy import Boolean, Column, Integer, String

from db import Model


class Films(Model):
    """
    Класс, который описывает таблицу в базе данных, наследуемся от класса Model.

    The class that describes our table in database.
    """

    """
    __tablename__
    Обязательное к заполнению поле. Значение должно точно соответствовать 
    названию таблички в базе данных, чтобы sqlalchemy понимала, с какой именно
    табличкой она должна взаимодействовать.
        
    __tablename__
    Required parameter that should be filled. The value should be equal to 
    table name in database. It needs for sqlalchemy, because sqlalchemy doesn't
    have any another ways to detect and match needed table.
    """
    __tablename__ = 'films'

    """
    Описание полей в табличке. Вам не обязательно указывать все поля которые 
    там присутствуют, достаточно только тех, которые вы планируете использовать.
    
    !!! Все поля нужно указать только в том случае, если вы планируете создавать
    новые записи в базе данных, тогда нужно указать либо все, либо только
    обязательные к заполнению.
    
    ::primary_key -> Хотя бы одно поле в табличке которую вы описали,
                     обязательно должно иметь такой параметр.
    ::index -> Не обязательное к заполнению значение, но ходят слухи,
               что ОРМ использует этот параметр в моменте построения запроса,
               если это действительно так, то вы можете ускорить свои тесты.
               
    Field describe. You don't have to describe all existed fields here that 
    presented in database, just paste only needed for tests.
    
    !!! You have to describe all required field in case when u going to add 
    some data into database.
    
    ::primary_key -> One field should be with true flag.
    ::index -> It isn't required field, but information from some sources says,
        that sqlalchemy pick fields with this parameter firstly during query
        building for better optimization.
    """
    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    is_premiere = Column(Boolean)


class ItemType(Model):

    __tablename__ = 'item_type'

    item_id = Column(Integer, primary_key=True)
    item_type = Column(String)
