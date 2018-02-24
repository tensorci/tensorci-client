import os
from restful_redis.client import RestfulRedisClient


class TensorCISocket(object):

  def __init__(self):
    redis_url = os.environ.get('REDIS_URL')
    self.client = RestfulRedisClient(url=redis_url)

  def predict(self, data):
    # TODO: add error handling
    return self.client.request(data)