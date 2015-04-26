import hpd

def test_parse_contact():
  assert hpd.parse_contact('data/RegistrationContact20150331.txt')[2]['RegistrationContactID'] == '11388605'
  assert hpd.parse_contact('data/RegistrationContact20150331.txt')[8]['FirstName'] == 'NEIL'
  # test for length
  assert len(hpd.parse_contact('data/RegistrationContact20150331.txt')) > 550000

def test_parse_registrations():
  assert hpd.parse_registrations('data/Registration20150331.txt')[5]['RegistrationID'] == '103151'
  assert hpd.parse_registrations('data/Registration20150331.txt')[6]['StreetName'] == 'CROSBY STREET'
  assert len(hpd.parse_registrations('data/Registration20150331.txt')) > 150000
