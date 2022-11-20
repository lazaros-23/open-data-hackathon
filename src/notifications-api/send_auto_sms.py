import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+30 6955759077',
  'message': 'To αίτημα σου Ικανοποιήθηκε, Βρες την ανάλυση νερού στο παρακάτω pdf',
  'key': 'textbelt',
})
print(resp.json())
