class FixedSizedArray:
    def __init__(self, size, default_value=0):
        self.size = size
        self.array = [default_value] * size
    
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")
    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")
    def __repr__(self):
        return repr(self.array)

fixed_array = FixedSizedArray(5)
print(fixed_array)
fixed_array[2] = 10
print(fixed_array)

try:
    fixed_array[5] = 20
except Exception as e:
    print(e)