# Author: Zheng Hao Tan
# Email: tanzhao@umich.edu

import sys
import sms

if len(sys.argv) != 6:
  sys.exit('Invalid arguments. Please rerun the script')

accountSID = sys.argv[1]
authToken = sys.argv[2]
from_ = sys.argv[3]
to = sys.argv[4]
smsBody = sys.argv[5]

print('Setting up phone numbers and logging in...')
sms = sms.SMS(accountSID, authToken)

print('Sending SMS...')

sms.send(from_, to, smsBody)

print('SMS sent!')

