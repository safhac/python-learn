class MyList:

    def __init__(self):
        self.items = {}

    def get(self, key):
        keys = list(self.items.keys())
        if 'all' in keys:
            if keys.index(key) < keys.index('all'):
                return self.items.get(key)
            else:
                return self.items.get('all')
        else:
            return self.items.get(key, None)

    def set(self, val):
        l_index = len(self.items)
        self.items.update({l_index: val})

    def set_all(self, val):
        self.items.update({'all': val})

    def unset_all(self):
        self.items.pop('all')



mylist = MyList()
mylist.set('a')
mylist.set('b')
print(mylist.get(1))

mylist.set_all('z')
print(mylist.get(1))
