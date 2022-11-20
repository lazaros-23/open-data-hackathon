import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+30 6955759077',
  'message': 'to kinito sou parakolouthite, pouthena den mporeis na pas xoris na to ksero isisisisisissis',
  'key': 'textbelt',
})
print(resp.json())