from notificationOptions import *
from vlrInfo import *

#importVLRJSON()
# Create Email
msg = constructMessage()

# Send email
sendEmailSMTP(msg)