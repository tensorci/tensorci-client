from tensorci import TensorCI


if __name__ == '__main__':
  client = TensorCI()

  new_entries = [
    {
      'key1': 'some-val',
      'key2': 'some-other-val'
    },
    {
      'key1': 'some-other-val',
      'key2': 'some-other-val'
    }
  ]

  resp = client.update_dataset(records=new_entries)

  data = resp.json()

  if data.get('ok'):
    print('Dataset successfully updated.')
  else:
    print('Dataset update failed with error: ', data.get('error'))