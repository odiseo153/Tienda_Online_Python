from DataBase.Models.modelos import carritocompra
from DataBase.Models.modelos import producto as Producto
from DataBase.Models.modelos import usuario



def get_carritos():
     return {'Carritos': [ {'id': carrito.id, 'cantidad': carrito.cantidad,'usuarioid':carrito.usuarioid,'productoid':carrito.productoid} for carrito in carritocompra.select() ] }
 

def create_carrito(carrito_data):
    # Assuming 'product_data' is a dictionary with all the necessary fields to create a 'producto'
    required_fields = ['usuarioid', 'productoid', 'cantidad']
    for field in required_fields:
        if field not in carrito_data or not carrito_data[field]:
            return (400, f'Campo obligatorio faltante o vacío: {field}')


    # Verificar si el usuario existe
    usuario_id = carrito_data['usuarioid']
    usuario_existente = usuario.get_or_none(usuario.id == usuario_id)

    if not usuario_existente:
        return (404, "No se encontró al usuario con ese ID")

    # Verificar si el producto existe
    producto_id = carrito_data['productoid']
    producto_existente = Producto.get_or_none(Producto.id == producto_id)

    if not producto_existente:
        return (404, "No se encontró el producto con ese ID")


    new_carrito = carritocompra.create(
        cantidad=carrito_data['cantidad'],
        usuarioid=usuario_id,
        productoid=producto_id
    )
    
    # Assuming 'id' is the primary key that gets created automatically
    carrito_dict = {
        'id': new_carrito.id,
        'cantidad': new_carrito.cantidad,
        'producto':{'id':producto_existente.id,'nombre':producto_existente.nombre,
                        'precio':producto_existente.precio,
                        'descripcion':producto_existente.descripcion,
                        'stock':producto_existente.stock},
        'usuario':{'id':usuario_existente.id,'nombre':usuario_existente.nombre,
                       'correoElectronico':usuario_existente.correoElectronico,
                       'rol':usuario_existente.rol},
    }
    
    return {'Producto_Creado': carrito_dict}


def get_carrito_by_id(id):
    # Now you can use the 'id' parameter directly in your function
    carrito = carritocompra.get_or_none(carritocompra.id == id)

    usuario_existente = usuario.get_or_none(usuario.id == carrito.usuarioid)

    if not usuario_existente:
        return (404, "No se encontró al usuario con ese ID")

    # Verificar si el producto existe
    producto_existente = Producto.get_or_none(Producto.id == carrito.productoid)
    
    if carrito:
        product_data = {
            'id': carrito.id,
            'cantidad': carrito.cantidad, 
  'producto':{'id':producto_existente.id,'nombre':producto_existente.nombre,
                        'precio':producto_existente.precio,
                        'descripcion':producto_existente.descripcion,
                        'stock':producto_existente.stock},
            'usuario':{'id':usuario_existente.id,'nombre':usuario_existente.nombre,
                       'correoElectronico':usuario_existente.correoElectronico,
                       'rol':usuario_existente.rol},
            }
        
        
        return {'success': product_data}
    else:
        return {'error': 'Product not found'}, 404
    
    
def delete_Carrito(id):
    # Use the 'id' parameter directly in your function
    carrito = carritocompra.get_or_none(carritocompra.id == id)

    if carrito:
        carrito.delete_instance()
        return {'success': 'Product deleted successfully'}
    else:
        return {'error': 'Product not found'}, 404
    
    
def update_Carrito(id, carrito_data):
    # Use the 'id' parameter directly in your function
    carrito = carritocompra.get_or_none(carritocompra.id == id)

    if carrito:
        carrito.cantidad = carrito_data.get('cantidad', carrito.cantidad)

        carrito.save()
        return {'success': 'Carrito Actualizado correctamente'}
    else:
        return {'error': 'no se encontro carrito con ese id '}, 404