import numpy as np
class block(object):
    def __init__(self,type,shape):
        self._shape = shape
        self._type = type

    def rotate(self):
        b = np.zeros((self._shape.shape[1],self._shape.shape[0]))
        for h_dim in range(0,self._shape.shape[1]):
            b[h_dim] = np.flip(self._shape[:,h_dim])
        return block(self._type,b)

    def get_type(self):
        return self._type

    def __str__(self):
        return '{0}'.format(self._shape)
