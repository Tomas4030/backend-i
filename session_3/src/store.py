class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} costs ${self.price:.2f}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"

class Store:
  def __init__(self):
      self.stock = []
      self.users = []

  def Add_Products(self, product):
      self.stock.append(product)
      print("Produto adicionado:")

  def Add_Users(self, user):
    self.users.append(user)
    print("Users adicionado")
  
  def Mostar_Products(self):
    if self.stock == None:
      print("Não temos produtos")
    for stock in self.stock:
      print(stock)

  def Mostar_Users(self):
    if self.users == None:
      print("Não temos users no sistema")
    for user in self.users:
      print(user)

store = Store()

produto1 = ("Pao", 2)
produto2 = ("Agua", 3)
user1 = ("tomas", "Tomas@teste.com")
user2 = ("Tiago", "Tiago@teste.com")

store.Add_Products(produto1)
store.Add_Products(produto2)
store.Add_Users(user1)
store.Add_Users(user2)

store.Mostar_Products()
store.Mostar_Users()