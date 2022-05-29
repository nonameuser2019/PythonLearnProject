class AttrDisplay:

    def gather_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.gather_attrs()}'


