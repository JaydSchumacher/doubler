class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        self = self * self
        return self