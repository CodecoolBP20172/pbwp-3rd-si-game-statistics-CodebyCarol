
# Export functions
#
# file = open('replies_to_Judy.txt', 'w')
# import printing
# with open('printing.py', 'r') as replies:
#     file.write(replies.readlines())
# file.close()
import printing
import reports
from pprint import pprint
text = open ('printing.py', 'rb')

file = open ('replies_to_Judy.txt', 'w')

file.write(' '.format(text))

file.close()
