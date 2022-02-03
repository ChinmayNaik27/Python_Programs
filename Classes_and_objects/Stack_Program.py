"""Create a stack program using classes and object"""
class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,item):
        if self.top==4:
            print("Stack is Full")
        else:
            self.top+=1
            self.stack.insert(self.top,item)
            print("Pushed Item is :",self.stack[self.top])
    def pop(self):
        if self.top==-1:
            print("Stack is Empty!!")
        else:
            print("Poped item is :",self.stack[self.top])
            self.top-=1
    def peek(self):
        print("The last inserted item is ",self.stack[self.top])
    def isempty(self):
        if self.top==-1:
            return True
        else:
            return False
st=Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)
st.pop()
st.peek()
st.push(90)
st.peek()
if st.isempty==True:
    print("Stack empty")
else:
    print("Stack Has Values!!!")