from DataBase.Models.modelos import detallespedido, usuario,pedido
from flask import jsonify

def get_Detalles():
     return {'Pedidos': [ {'id': pedido.id, 'cantidad': pedido.cantidad,'precioUnitario':pedido.precioUnitario,'pedidoid':pedido.pedidoid} for pedido in detallespedido.select() ]}


def create_detallepedido(detallepedido_data):
    
    required_fields = ['cantidad', 'precioUnitario', 'pedidoid']
    for field in required_fields:
        if field not in detallepedido_data or not detallepedido_data[field]:
            return (400, f'Campo obligatorio faltante o vacío: {field}')

    # Verificar si el producto existe
    pedido_id = detallepedido_data['pedidoid']
    producto_existente = pedido.get_or_none(pedido.productoid == pedido_id)

    if not producto_existente:
        return (404, "No se encontró el producto con ese ID")

    # Crear el pedido si tanto el usuario como el producto existen
    nuevo_detalle = detallespedido.create(
        cantidad=detallepedido_data['cantidad'],
        precioUnitario=detallepedido_data['precioUnitario'],
        pedidoid=detallepedido_data['pedidoid']
    )

    # Crear un diccionario con la información del nuevo pedido
    pedido_dict = {
        'id': nuevo_detalle.id,
        'cantidad': nuevo_detalle.cantidad,
        'precioUnitario': nuevo_detalle.precioUnitario,
        'producto':{'id':producto_existente.id,'nombre':producto_existente.nombre,
                        'precio':producto_existente.precio,
                        'descripcion':producto_existente.descripcion,
                        'stock':producto_existente.stock},
    }

    return {'Detalle_Pedido_Creado': pedido_dict}


def get_detallepedido_by_id(id):
    
    if not id:
        return {'error':"El campo Id no puede estar vacio"}
    
    # Now you can use the 'id' parameter directly in your function
    detallepedido = detallespedido.get_or_none(detallespedido.id == id)

    if detallepedido:
        pedido_existente = pedido.get_or_none(pedido.id == detallepedido.pedidoid)

        if not pedido_existente:
            return {'message':"al parecer el pedido fue eliminado"}

        pedido_data = {
            'id': detallepedido.id,
            'cantidad': detallepedido.cantidad, 
            'precioUnitario': detallepedido.precioUnitario,
            'pedido':{
                      'id':pedido_existente.id,
                      'estado':pedido_existente.estado,
                      'fechapedido':pedido_existente.fechapedido
                      }
            }
        
        
        return {'success': pedido_data}
    else:
        return {'error': 'Pedido not found'}, 404
    
    
def delete_detallespedido(id):
    # Use the 'id' parameter directly in your function
    detallepedido = detallespedido.get_or_none(detallespedido.id == id)

    if detallepedido:
        detallepedido.delete_instance()
        return {'success': 'detalle pedido borrado correctamente'}
    else:
        return {'error': 'detalle del pedido no encontrado'}, 404
    
    
def update_detallepedido(id, pedido_data):
    # Use the 'id' parameter directly in your function
    detallepedido = detallespedido.get_or_none(detallespedido.id == id)

    if detallepedido:
        detallepedido.cantidad = pedido_data.get('cantidad', detallepedido.cantidad)
        detallepedido.precioUnitario = pedido_data.get('precioUnitario', detallepedido.precioUnitario)

        detallepedido.save()
        return {'success': 'Detalle del Pedido actualizado correctamente','Detelle_Actualizado':{'cantidad':detallepedido.cantidad,
          'precioUnitario':detallepedido.precioUnitario}}
    else:
        return {'error': 'Pedido no encontrado'}, 404

