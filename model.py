from sqlalchemy import Column, Integer, String, Data, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product:
	def __init__(self,)