import os
from api import AbstractApi
from definitions import auth_header_name


class TensorCI:

  def __init__(self, client_id=None, client_secret=None):
    self.client_id = client_id or os.environ.get('TENSORCI_CLIENT_ID')
    self.client_secret = client_secret or os.environ.get('TENSORCI_CLIENT_SECRET')

    self.api = AbstractApi(
      base_url=os.environ.get('TENSORCI_API_URL') or 'https://app.tensorci.com/api',
      auth_header_name=auth_header_name,
      auth_header_value=self.client_secret
    )

  def predict(self, features={}):
    payload = self.build_payload(features=features)
    return self.api.post('/predict', payload=payload)

  def update_dataset(self, records=[]):
    payload = self.build_payload(records=records)
    return self.api.put('/dataset', payload=payload)

  def build_payload(self, **kwargs):
    payload = kwargs
    payload['client_id'] = self.client_id
    return payload