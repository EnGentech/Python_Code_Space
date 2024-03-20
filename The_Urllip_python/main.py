import fabric

connect = fabric.Connection(host='ubuntu@engentech.tech')

def process_list(c):
    return c.run('ps aux')

print(process_list(connect))