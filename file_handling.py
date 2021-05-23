# f = open('demo.txt', 'w')

# f.write('Vaishnavi is awesome!!!')

# f.close()

r = open('demo-image.png', 'rb')
w = open('copy.png', 'wb')

content = r.read()
w.write(content)

r.close()
w.close()