class SharedAllMixin:
    def __init__(self, *args, **kwargs):
        try:
            self.__class__._attributes
        except:
            self.__class__._attributes = {}

        self.__dict__ = self.__class__._attributes
        super().__init__(*args, **kwargs)


class BaseFetcher:
    def __init__(self, source):
        self.source = source

class TagFetcher(SharedAllMixin, BaseFetcher):
    def pull(self):
        return f'Tag= {self.source}'

class BranchFetcher(SharedAllMixin, BaseFetcher):
    def pull(self):
        return f'Branch = {self.source}'


    
