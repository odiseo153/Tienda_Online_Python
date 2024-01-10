from DataBase.Models.modelos import pedido 
from DataBase.Models.modelos import historialcambio
from DataBase.Models.modelos import usuario
from flask import jsonify

def get_Historial():
     return {'Pedidos': [ {'id': historial.id, 'FechaCambio': historial.FechaCambio,'usuarioid':historial.usuarioid,'pedidoid':historial.pedidoid} for historial in historialcambio.select()  ]}


def get_Historial_by_id(id):
    # Now you can use the 'id' parameter directly in your function
    Historial = historialcambio.get_or_none(historialcambio.id == id)

    if Historial:
        usuario_existente = usuario.get_or_none(usuario.id == Historial.usuarioid)
        pedido_existente = pedido.get_or_none(pedido.id == Historial.pedidoid)

        Historial = {
            'id': Historial.id,
            'FechaCambio': Historial.FechaCambio, 
            'pedido':{'id':pedido_existente.id,'estado':pedido_existente.estado,
                        'fechapedido':pedido_existente.fechapedido},
            'usuario':{'id':usuario_existente.id,'nombre':usuario_existente.nombre,
                       'correoElectronico':usuario_existente.correoElectronico,
                       'rol':usuario_existente.rol},
            }

        return {'success': Historial}
    else:
        return {'error': 'Pedido not found'}, 404
