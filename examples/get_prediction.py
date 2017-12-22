from tensorci import TensorCI


if __name__ == '__main__':
  client = TensorCI()

  unseen_features = {
    'key1': 'val1',
    'key2': 'val2'
  }

  resp = client.predict(features=unseen_features)

  data = resp.json()

  if data.get('ok'):
    print('Got Prediction: ', data.get('prediction'))
  else:
    print('Prediction responded with error: ', data.get('error'))