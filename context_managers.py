# r = open('demo-image.png', 'rb')


# content = r.read()
# print(content)

# s = [1, 2, 3]
# print(s[3])

# r.close()


# with open('demo.txt', 'r') as f:
#     print(f.read())


class open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('Enter into context manager')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        print(type, 'value>>>', value, 'traceback>>>', traceback)
        print('Exit from context manager')
        return True


with open_file('demo.txt', 'w') as f:
    f.write('Akansha is great!!')
    s = [1, 2, 3]
    print(s[3])


