from emailUpdate import sendEmailSMTP, constructMessage
from vlrInfo import importVLRJSON

#importVLRJSON()
# Create Email
msg = constructMessage()

# Send email
sendEmailSMTP(msg)