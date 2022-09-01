import os
import shutil


class Blob(object):
    def __init__(self, hash_, path):
        self.hash_ = hash_
        self.path = path

    def restore(self):
        try:
            os.makedirs(os.path.dirname(self.path))
        except FileExistsError:
            pass

        shutil.copy(os.path.join('./.shit/objects/', self.hash_, os.path.basename(self.path)), self.path)
    