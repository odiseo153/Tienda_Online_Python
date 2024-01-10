from ..connection import BaseModel
from peewee import *

class usuario(BaseModel):
       # Define your fields here
    nombre = CharField()
    id = IdentityField();
    correoElectronico = CharField()
    clave = CharField()
    rol = CharField()

class producto(BaseModel):
       # Define your fields here
    nombre = CharField()
    id = IdentityField();
    descripcion = CharField()
    precio = DoubleField()
    stock = IntegerField()


class pedido(BaseModel):
    id = IdentityField()
    estado = CharField()
    fechapedido = DateField()
    productoid = IntegerField()
    usuarioid = IntegerField()



class historialcambio(BaseModel):
    id = IdentityField();
    pedidoid = IntegerField()
    FechaCambio = DateField()
    usuarioid = IntegerField()


class detallespedido(BaseModel):
    id = IdentityField();
    cantidad = IntegerField()
    precioUnitario = IntegerField()
    pedidoid = IntegerField()

class carritocompra(BaseModel):
    id = IdentityField();
    cantidad = IntegerField()
    productoid = IntegerField()
    usuarioid = IntegerField()


