from glob import glob
from os.path import basename, join

from .models import Publisher


class PublisherSet:
    def __init__(self, basepath, **kwargs):
        self._basepath = basepath
        self._wheres = kwargs

    def where(self, **kwargs):
        wheres = dict(self._wheres, **kwargs)
        return PublisherSet(self._basepath, **wheres)

    def __len__(self):
        return len(list(iter(self)))

    def __iter__(self):
        paths = glob(join(self._basepath, '*'))

        where_path = self._wheres.get('path')
        if where_path:
            paths = filter(lambda x: x == where_path, paths)
        where_name = self._wheres.get('name')
        if where_name:
            paths = filter(lambda x: basename(x) == where_name, paths)

        for path in paths:
            name = basename(path)
            yield Publisher(path, name)

    def first(self):
        for first in self:
            return first

    def all(self):
        return list(iter(self))

    def find(self, **kwargs):
        return self.where(**kwargs).first()


class Registry:
    def __init__(self, path=None):
        if not path:
            path = join('__pyandicache__', 'data')
        self.path = path

    @property
    def publishers(self):
        return PublisherSet(self.path)


def publishers():
    return Registry().publishers