class ApiException(BaseException):

  def __init__(self, status=None, code=None, error=None):
    self.status = status
    self.code = code
    self.error = error
    self.message = 'Request returned error: {}'.format(self.error)


class RequestError(BaseException):

  def __init__(self, message=None):
    self.message = message