"""
function with local and global params

"""

x = 5  # global param

# function declaration
def add():
    global x
    x = 3  # local param
    x = x + 5
    print(x)

add()
print(x)
