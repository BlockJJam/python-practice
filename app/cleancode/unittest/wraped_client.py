from asyncio.log import logger
from logger import Logger


class MetricsClient:
    def send(self, metric_name, metric_value):
        if not isinstance(metric_name, str):
            raise TypeError('metric_name으로 문자열 타입을 사용해야 한다')

        if not isinstance(metric_value, str):
            raise TypeError('metric_value로 문자열 타입을 사용해야 함')
        Logger.info('%s 전송 값 = %s ', metric_name, metric_value)

class WrappedClient:
    def __init__(self):
        self.client = MetricsClient()

    def send(self, metric_name, metric_value):
        return self.client.send(str(metric_name), str(metric_value))

class Process:
    def __init__(self) -> None:
        self.client = WrappedClient()

    def process_iterations(self, n_iterations):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send('iteration.'.format(i), result)
            
    