from database import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, name,descripcion,price,stock):
        self.name = name 
        self.descripcion = descripcion
        self.price = float(price)
        self.stock = int(stock)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Product.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)
    
    def update(self, name, descripcion, price, stock):
        if name is not None:
            self.name = name
        if descripcion is not None:
            self.descripcion = descripcion
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()