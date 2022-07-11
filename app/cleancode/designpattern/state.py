import abc
from logger import Logger

class InvalidTransitionError(Exception):
    pass

class MergeRequestState(abc.ABC):
    def __init__(self, merge_request):
        self._merge_request = merge_request
    
    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def merge(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Open(MergeRequestState):
    def open(self):
        self._merge_request.approvals = 0
    
    def close(self):
        self._merge_request.approvals = 0
        self._merge_request.state = Close

    def merge(self):
        Logger.info('%s 머지', self._merge_request)
        Logger.info('%s 브랜치 삭제', self._merge_request.source_branch)
        self._merge_request.state = Merge

class Close(MergeRequestState):
    def open(self):
        Logger.info('종료된 머지 리퀘스트 %s 재오픈', self._merge_request)
        self._merge_request.state = Open
    
    def close(self):
        pass

    def merge(self):
        raise InvalidTransitionError('종료된 요청을 머지할 순 없음')

class Merge(MergeRequestState):
    def open(self):
        raise InvalidTransitionError('이미 머지 완료됨')
    
    def close(self):
        raise InvalidTransitionError('이미 머지 완료됨')

    def merge(self):
        pass


class MergeRequest:
    def __init__(self, source_branch:str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state = None
        self.approvals = 0
        self.state = Open

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state_cls):
        self._state = new_state_cls(self)

    # def open(self):
    #     return self.state.open()

    # def close(self):
    #     return self.state.close()

    # def merge(self):
    #     return self.state.merge()
    # 위에 중복된 로직들이 state에 위임됐기 때문에 발생, 어떻게 하면 반복코드를 없앨 수 있나
    def __getattr__(self, method):
        return getattr(self.state, method)
        
    def __str__(self):
        return f'{self.target_branch} : {self.source_branch}'
    
mr = MergeRequest('dev','main')

mr.open()
print(mr.approvals)

mr.approvals = 3
print(mr.approvals)

mr.close()
print(mr.approvals)

mr.open()
mr.merge()
mr.close()
