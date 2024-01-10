from DataBase.Models.modelos import pedido as Pedido,producto as Producto,usuario,historialcambio,detallespedido



from flask import jsonify

def get_pedidos():
     return {'Pedidos': [ {'id': pedido.id, 'estado': pedido.estado,'fechapedido':pedido.fechapedido} for pedido in Pedido.select()  ]}


def create_pedido(pedido_data):
    
    required_fields = ['usuarioid', 'productoid', 'estado', 'fechapedido']
    for field in required_fields:
        if field not in pedido_data or not pedido_data[field]:
            return (400, f'Campo obligatorio faltante o vacío: {field}')


    # Verificar si el usuario existe
    usuario_id = pedido_data['usuarioid']
    usuario_existente = usuario.get_or_none(usuario.id == usuario_id)

    if not usuario_existente:
        return (404, "No se encontró al usuario con ese ID")

    # Verificar si el producto existe
    producto_id = pedido_data['productoid']
    producto_existente = Producto.get_or_none(Producto.id == producto_id)

    if not producto_existente:
        return (404, "No se encontró el producto con ese ID")

    # Crear el pedido si tanto el usuario como el producto existen
    nuevo_pedido = Pedido.create(
        estado=pedido_data['estado'],
        fechapedido=pedido_data['fechapedido'],
        productoid=pedido_data['productoid'],
        usuarioid=pedido_data['usuarioid']
    )

    # Crear un diccionario con la información del nuevo pedido
    pedido_dict = {
        'id': nuevo_pedido.id,
        'estado': nuevo_pedido.estado,
        'fechapedido': nuevo_pedido.fechapedido,
        'producto':{'id':producto_existente.id,'nombre':producto_existente.nombre,
                        'precio':producto_existente.precio,
                        'descripcion':producto_existente.descripcion,
                        'stock':producto_existente.stock},
        'usuario':{'id':usuario_existente.id,'nombre':usuario_existente.nombre,
                       'correoElectronico':usuario_existente.correoElectronico,
                       'rol':usuario_existente.rol},
    }

    return {'Pedido_Creado': pedido_dict}


def get_pedido_by_id(id):
    # Now you can use the 'id' parameter directly in your function
    pedido = Pedido.get_or_none(Pedido.id == id)

    if pedido:
        
        usuario_existente = usuario.get_or_none(usuario.id == pedido.usuarioid)
        producto_existente = Producto.get_or_none(Producto.id == pedido.productoid)
        

        pedido_data = {
            'id': pedido.id,
            'estado': pedido.estado, 
            'fechapedido': pedido.fechapedido,
            'producto':{'id':producto_existente.id,'nombre':producto_existente.nombre,
                        'precio':producto_existente.precio,
                        'descripcion':producto_existente.descripcion,
                        'stock':producto_existente.stock},
            'usuario':{'id':usuario_existente.id,'nombre':usuario_existente.nombre,
                       'correoElectronico':usuario_existente.correoElectronico,
                       'rol':usuario_existente.rol},
            }
        
        
        return {'success': pedido_data}
    else:
        return {'error': 'Pedido not found'}, 404
    
    
def delete_pedido(id):
    # Use the 'id' parameter directly in your function
    pedido = Pedido.get_or_none(Pedido.id == id)
    

    if pedido:
        detalle = detallespedido.get_or_none(detallespedido.id == id);
        
        if detalle:
            detalle.delete_instance()

        pedido.delete_instance()
        return {'success': 'pedido borrado correctamente'}
    else:
        return {'error': 'pedido no encontrado'}, 404
    
    
def update_pedido(id, pedido_data):
    # Use the 'id' parameter directly in your function
    pedido = Pedido.get_or_none(Pedido.id == id)

    if pedido:
        pedido.estado = pedido_data.get('estado', pedido.estado)

        #usuario_existente = usuario.get_or_none(usuario.id == pedido_data['usuarioid'])


        pedido.save()
        return {'success': 'Pedido actualizado correctamente','PedidoActualizado':{'id':pedido.id,'estado':pedido.estado}}
    else:
        return {'error': 'Pedido no encontrado'}, 404

