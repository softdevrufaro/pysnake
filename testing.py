hello_world = "Hello world"
print(hello_world)
def _change_hello_world():
	global hello_world 
	hello_world = "bup"
_change_hello_world()
print(hello_world)