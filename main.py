from flask import Flask, request, jsonify
from Controller import ProductoController, UsuarioController, PedidoController , CarritoController,HistorialController,DetallesController

app = Flask(__name__)

# Product routes
@app.route("/productos", methods=['GET'])
def get_products():
    return jsonify(ProductoController.get_products())

@app.route("/productos/<int:id>", methods=['GET'])
def get_product_by_id(id):
    return jsonify(ProductoController.get_product_by_id(id))

@app.route("/productos", methods=['POST'])
def create_product():
    product_data = request.get_json()
    return jsonify(ProductoController.create_product(product_data))

@app.route("/productos/<int:id>", methods=['DELETE'])
def delete_product(id):
    return jsonify(ProductoController.delete_product(id))

@app.route("/productos/<int:id>", methods=['PUT'])
def update_product(id):
    product_data = request.get_json()
    return jsonify(ProductoController.update_product(id, product_data))



# User routes
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    return jsonify(UsuarioController.login(data))

@app.route("/usuario/<int:id>", methods=['GET'])
def get_user_by_id(id):
    return jsonify(UsuarioController.get_user_by_id(id))

@app.route("/usuario", methods=['GET'])
def get_users():
    return jsonify(UsuarioController.get_users())

@app.route("/usuario", methods=['POST'])
def create_user():
    user_data = request.get_json()
    return jsonify(UsuarioController.create_user(user_data))

@app.route("/usuario/<int:id>", methods=['DELETE'])
def delete_user(id):
    return jsonify(UsuarioController.delete_user(id))

@app.route("/usuario/<int:id>", methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    return jsonify(UsuarioController.update_user(id, user_data))




#Pedido routes
@app.route("/pedido/<int:id>", methods=['GET'])
def get_pedido_id(id):
    return jsonify(PedidoController.get_pedido_by_id(id))

@app.route("/pedido", methods=['GET'])
def get_the_pedidos():
    return jsonify(PedidoController.get_pedidos())

@app.route("/pedido", methods=['POST'])
def create_pedidos():
    pedido_data = request.get_json()
    return jsonify(PedidoController.create_pedido(pedido_data))

@app.route("/pedido/<int:id>", methods=['DELETE'])
def delete_pedidos(id):
    return jsonify(PedidoController.delete_pedido(id))

@app.route("/pedido/<int:id>", methods=['PUT'])
def update_pedido(id):
    pedido_data = request.get_json()
    return jsonify(PedidoController.update_pedido(id, pedido_data))




#Carrito controller
@app.route("/carrito/<int:id>", methods=['GET'])
def get_carrito_id(id):
    return jsonify(CarritoController.get_carrito_by_id(id))

@app.route("/carrito", methods=['GET'])
def get_the_carritos():
    return jsonify(CarritoController.get_carritos())

@app.route("/carrito", methods=['POST'])
def create_carritos():
    carrito_data = request.get_json()
    return jsonify(CarritoController.create_carrito(carrito_data))

@app.route("/carrito/<int:id>", methods=['DELETE'])
def delete_carrito(id):
    return jsonify(CarritoController.delete_Carrito(id))

@app.route("/carrito/<int:id>", methods=['PUT'])
def update_carrito(id):
    carrito_data = request.get_json()
    return jsonify(CarritoController.update_Carrito(id, carrito_data))



#DetalleCarrito controller
@app.route("/detallecarrito/<int:id>", methods=['GET'])
def get_detalles_By_id(id):
    return jsonify(DetallesController.get_detallepedido_by_id(id))


@app.route("/detallecarrito", methods=['GET'])
def get_the_detalles():
    return jsonify(DetallesController.get_Detalles())


@app.route("/detallecarrito", methods=['POST'])
def create_detallepedidos():
    data = request.get_json()
    return jsonify(DetallesController.create_detallepedido(data))


@app.route("/detallecarrito/<int:id>", methods=['DELETE'])
def delete_detalles(id):
    return jsonify(DetallesController.delete_detallespedido(id))


@app.route("/detallecarrito/<int:id>", methods=['PUT'])
def update_detallescarrito(id):
    data = request.get_json()
    return jsonify(DetallesController.update_detallepedido(id, data))




#Historial controller
@app.route("/historial/<int:id>", methods=['GET'])
def get_historia_By_id(id):
    return jsonify(HistorialController.get_Historial_by_id(id))


@app.route("/historial", methods=['GET'])
def get_Historiales():
    return jsonify(HistorialController.get_Historial())




if __name__ == "__main__":
    app.run(debug=True)
