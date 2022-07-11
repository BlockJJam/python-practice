from typing import Callable, Iterable, Dict


class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query

class QueryEnhancer:
    def __init__(
        self,
        query: DictQuery,
        *decorators: Iterable[Callable[[Dict[str,str]], Dict[str,str]]]
    ) -> None:
        self._decorated = query
        self._decorators = decorators
    
    def render(self):
        current_result = self._decorated.render()
        for deco in self._decorators:
            current_result = deco(current_result)
        return  current_result


def remove_empty(query: dict):
    return {k: v for k, v in query.items() if v}

def case_insensitive(query: dict):
    return {k : v.lower() for k, v in query.items() }

    
query = DictQuery(foo='bar', empty = '', none = None, upper = 'UPPER', title = 'Title')
print(QueryEnhancer(query, remove_empty, case_insensitive).render())
