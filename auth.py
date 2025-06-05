    
class Authentication:
  def __init__(self):
    self.admin ='admin'
    self.password = 'password'

    
  def check_password(self,admin,password):
    if admin == self.admin and password == self.password:
      return True
    return False
   