
import sys

sys.path.append(".")
sys.path.append("..")

import SMS

accountSID = 'bla1'
authToken = 'bla2'

class TestSMS(object):

  def test_create(self):
    sms = SMS.SMS(accountSID, authToken)
