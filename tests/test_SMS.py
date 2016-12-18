
import sys

sys.path.append(".")
sys.path.append("..")

import SMS

accountSID = 'AC3ab635e624b006998a8f09ae9b2e4695'
authToken = 'd888435c644791874e677574439357aa'

class TestSMS(object):

  def test_create(self):
    sms = SMS.SMS(accountSID, authToken)
