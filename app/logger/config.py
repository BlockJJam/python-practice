import logging

Logger = logging.getLogger()
Logger.setLevel(logging.INFO)
formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')
streamingHandler = logging.StreamHandler()
streamingHandler.setFormatter(formatter)
Logger.addHandler(streamingHandler)