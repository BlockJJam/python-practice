import logging
logger = logging.getLogger()


def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell
        
def search_nested(array, desired_value):
    try:
        coord = next(
            coord for(coord, cell) in _iterate_array2d(array) if cell == desired_value
        )
    except StopIteration:
        raise ValueError(f'{desired_value} not found')

    print('[%i, %i]에서 값 %r 찾음' %( *coord, desired_value))
    return coord

arr = [[1,2,3],[4,5,6],[7,8,9]]
desired = 3

print(search_nested(arr, desired))

class MappedRange:
    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)
        print("index %d: %s" %(index, result))
        return result
    
    def __len__(self):
        return len(self._wrapped)

mr = MappedRange(abs, -10, 5)
print(mr[0])
print(list(mr))
