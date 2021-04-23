class Category:
  def __init__(self, name):
    self.name = name
    self.book = list()

  def withdraw(self, amount, description = ""):
    if self.isSufficient(amount):
      self.book.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def deposit(self, amount, description = ""):
    self.book.append({"amount": amount, "description": description})

  def check_funds(self):
    total = 0
    for item in self.book:
      total += item['amount']
    return total

  def transfer(self, amount, target_category):
    if self.isSufficient(amount):
      self.withdraw(amount, f"Transfer to {target_category.name}")
      target_category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def isSufficient(self, amount):
    if amount <= self.check_funds():
      return True
    else:
      return False
      
  def __str__(self):
    title = f"{self.name:*^34}\n"
    body = ""
    ttotal = 0
    for item in self.book:
      body += item["description"][:23].ljust(23) + str('{:.2f}'.format(item["amount"]))[:7].rjust(10) + '\n'
      ttotal += item["amount"]
    table = title + body + f"Total: {ttotal:.2f}"
    return table
