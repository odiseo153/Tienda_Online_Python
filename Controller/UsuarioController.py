from DataBase.Models.modelos import usuario


def login(user_data):
    # Assuming 'user_data' is a dictionary with 'correoElectronico' and 'clave'
    user = usuario.select().where(usuario.correoElectronico == user_data.get('correoElectronico') and usuario.clave == user_data.get('clave'));
    
    if user:
        return {'success': 'User logged in successfully'}
    else:
        return {'error': 'Invalid email or password'}
    
    

def get_users():
    # Now you can use the 'id' parameter directly in your function
     query = usuario.select()
     usuario_lista = [ {'id': user.id, 'nombre': user.nombre,'correoElectronico':user.correoElectronico,
     'rol':user.rol} for user in query ]
     
     return {'Usuarios': usuario_lista}


def create_user(user_data):
    # Assuming 'user_data' is a dictionary with all the necessary fields to create a 'usuario'
    new_user = usuario.create(
        nombre=user_data['nombre'],
        correoElectronico=user_data['correoElectronico'],
        rol=user_data['rol'],
        clave=user_data['clave']
    )
    
    # Assuming 'id' is the primary key that gets created automatically
    user_dict = {
        'id': new_user.id,
        'nombre': new_user.nombre,
        'correoElectronico': new_user.correoElectronico,
        'clave': new_user.clave,
        'rol': new_user.rol
    }
    
    return {'Usuario_Creado': user_dict}
 

def get_user_by_id(id):
    # Now you can use the 'id' parameter directly in your function
    query = usuario.select().where(usuario.id == id)
    user = query.first()

    if user:
        user_data = {
            'id': user.id,
            'nombre': user.nombre, 
            'clave': user.clave,
            'correoElectronico':user.correoElectronico,
            'rol':user.rol
            }
        
        
        return {'success': user_data}
    else:
        return {'error': 'User not found'}, 404
    
    
def delete_user(id):
    # Use the 'id' parameter directly in your function
    user = usuario.get_or_none(usuario.id == id)

    if user:
        user.delete_instance()
        return {'success': 'User deleted successfully'}
    else:
        return {'error': 'User not found'}, 404
    
    
def update_user(id, user_data):
    # Use the 'id' parameter directly in your function
    user = usuario.get_or_none(usuario.id == id)

    if user:
        user.nombre = user_data.get('nombre', user.nombre)
        user.correoElectronico = user_data.get('correoElectronico', user.correoElectronico)
        user.clave = user_data.get('clave', user.clave)
        user.rol = user_data.get('rol', user.rol)
        user.save()
        return {'success': 'User updated successfully','userUpdated':user}
    else:
        return {'error': 'User not found'}, 404
