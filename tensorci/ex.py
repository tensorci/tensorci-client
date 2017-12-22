class ApiException(BaseException):

  def __init__(self, status=None, code=None, error=None):
    self.status = status
    self.code = code
    self.error = error
    self.message = 'Request returned error: {}'.format(self.error)


class RequestException(BaseException):

  def __init__(self, message=None):
    self.message = message


class MissingCredentialsException(BaseException):

  def __init__(self, missing_creds=None):
    self.missing_creds = missing_creds or []
    self.message = None

    if self.missing_creds:
      self.message = 'Missing TensorCI credentials:\n'
      missing_cred_temp = '{} -- either set {} during instantiation of TensorCI or set the {} environment variable.\n'

      for c in self.missing_creds:
        attr, backup = c
        self.message += missing_cred_temp.format(attr, attr, backup)