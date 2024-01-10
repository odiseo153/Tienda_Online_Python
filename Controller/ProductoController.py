from DataBase.Models.modelos import producto



def get_products():
    # Now you can use the 'id' parameter directly in your function
     query = producto.select()
     producto_lista = [ {'id': product.id, 'nombre': product.nombre,'descripcion':product.descripcion} for product in query ]
     
     return {'Productos': producto_lista}


def create_product(product_data):
    # Assuming 'product_data' is a dictionary with all the necessary fields to create a 'producto'
    new_product = producto.create(
        nombre=product_data['nombre'],
        descripcion=product_data['descripcion'],
        precio=product_data['precio'],
        stock=product_data['stock']
    )
    
    # Assuming 'id' is the primary key that gets created automatically
    product_dict = {
        'id': new_product.id,
        'nombre': new_product.nombre,
        'descripcion': new_product.descripcion,
        'precio': new_product.precio,
        'stock': new_product.stock
    }
    
    return {'Producto_Creado': product_dict}
 

def get_product_by_id(id):
    # Now you can use the 'id' parameter directly in your function
    query = producto.select().where(producto.id == id)
    product = query.first()

    if product:
        product_data = {
            'id': product.id,
            'nombre': product.nombre, 
            'descripcion': product.descripcion,
            'precio':product.precio,
            'stock':product.stock
            }
        
        
        return {'success': product_data}
    else:
        return {'error': 'Product not found'}, 404
    
    
def delete_product(id):
    # Use the 'id' parameter directly in your function
    product = producto.get_or_none(producto.id == id)

    if product:
        product.delete_instance()
        return {'success': 'Product deleted successfully'}
    else:
        return {'error': 'Product not found'}, 404
    
    
def update_product(id, product_data):
    # Use the 'id' parameter directly in your function
    product = producto.get_or_none(producto.id == id)

    if product:
        product.nombre = product_data.get('nombre', product.nombre)
        product.descripcion = product_data.get('descripcion', product.descripcion)
        product.precio = product_data.get('precio', product.precio)
        product.stock = product_data.get('stock', product.stock)
        product.save()
        return {'success': 'Product updated successfully'}
    else:
        return {'error': 'Product not found'}, 404