"""Create classes that capture bank customers and bank accounts. A customer has a first and last name.
An account has a customer and a balance. Make objects for two accounts held by the same customer."""
class customers:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
    def show(self):
        print(self.fn,self.ln)
class account:
    def __init__(self,ob,bal):
        self.customer=ob
        self.balence=bal
    def show1(self):
        self.customer.show()
        print(self.balence)
t1=customers('Anil','Bow')
acc=account(t1,50000)
acc.show1()