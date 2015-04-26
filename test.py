import hpd

def test_say_hi():
  assert hpd.say_hi() == 'hello ziggy'

def test_parse_contact():
  assert hpd.parse_contact('data/RegistrationContact20150331.txt')[2]['RegistrationContactID'] == '11388605'
  assert hpd.parse_contact('data/RegistrationContact20150331.txt')[8]['FirstName'] == 'NEIL'

