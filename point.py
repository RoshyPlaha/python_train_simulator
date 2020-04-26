class point(object):

    paths = []

    def __init__(self):
        self.position = 0
        self.paths = []

    def add_paths(self, p):
        if len(self.paths) <= 3: # max paths for a point
            self.paths.append(p)

    def switch_path(self):
        self.position +=1

        print('current position is: ', self.position, ' and there is a size of array ', len(self.paths)-1)
        if self.position > len(self.paths)-1:
            print ('reset when position ', self.position, ' became greater than', len(self.paths)-1)
            self.position = 0
        for i, p in enumerate(self.paths):
            if i == self.position:
                print ('returning position ', i)
                return p
            else:
                print('not found brudda: ', i)

