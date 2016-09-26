# Author: Zheng Hao Tan
# Email: tanzhao@umich.edu

import re
from twilio.rest import TwilioRestClient

class SMS(object):

  def __init__(self, accountSID, authToken):
    self.accountSID = accountSID
    self.authToken = authToken
    self.twilioCli = TwilioRestClient(accountSID, authToken)

  # EFFECTS: Sends the given SMS body from the given sender to the intended receiver.
  def send(self, from_, to, smsBody):

    self.enforceValidSMSBody(smsBody)
    self.enforceValidPhoneNumber(from_)
    self.enforceValidPhoneNumber(to)

    message = self.twilioCli.messages.create(body = smsBody, from_ = from_, to = to)

  def enforceValidSMSBody(self, smsBody):
    if len(smsBody) > 160:
      sys.exit('SMS body cannot be more than 160 characters.')

  # TODO:
  def enforceValidPhoneNumber(self, from_):
		# Check length of sms body.
    if len(from_) > 160:
      sys.exit('SMS body cannot be more than 160 characters.')

  # TODO:
  def enforceValidPhoneNumber(self, to):
		# Check length of sms body.
    if len(to) > 160:
      sys.exit('SMS body cannot be more than 160 characters.')
