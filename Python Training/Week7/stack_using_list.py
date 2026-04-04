class stack:
 # Method for pushing data into stack
    def push(self, st, data):
         st.append(data)
 # Method for pop
    def pop(self, st):
        if len(st) > 0:
            ans = st.pop()
            print("Removed element from the st:", ans)
        else:
            print("The stack is Empty")
 # Method to get top of stack
    def top(self, st):
        if len(st) > 0:
            return st[len(st) - 1]
 # Method to check stack is empty or not
    def isEmpty(self, st):
        if len(st) == 0:
            return 1
        else:
            return 0
 # Method to get size of stack
    def size(self, st):
        return len(st)
# Creating object of stack class
st = stack()
s = ["Lokesh", "Diwakar", "Ankit", "Ritik"]
print(s)
print(st.size(s))
st.pop(s)
print("Top element in the stack:", st.top(s))
print(st.isEmpty(s))
st.push(s, "Vimal")
print(s)