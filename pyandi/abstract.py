class PyandiSet:
    def where(self, **kwargs):
        wheres = dict(self._wheres, **kwargs)
        return self.__class__(self._basepath, **wheres)

    def __len__(self):
        return len(list(iter(self)))

    def first(self):
        for first in self:
            return first

    def all(self):
        return list(iter(self))

    def find(self, **kwargs):
        return self.where(**kwargs).first()