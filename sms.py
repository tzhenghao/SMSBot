# Author: Zheng Hao Tan
# Email: tanzhao@umich.edu

from twilio.rest import TwilioRestClient

class SMS(object):

  def __init__(self, accountSID, authToken):
    self.accountSID = accountSID
    self.authToken = authToken
    self.twilioCli = TwilioRestClient(accountSID, authToken)

  # EFFECTS: Sends the given SMS body from the given sender to the intended receiver.
  def send(self, from_, to, smsBody):
    message = twilioCli.messages.create(body = smsBody, from_ = from_, to = to)

