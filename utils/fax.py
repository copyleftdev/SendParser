

class FaxUtils(object):


    def get_send_abbreviation(self):
         abbrev = {
             "CFR": "Confirmation To Recieve",
             "CIG": "Calling Subscriber Identification",
             "CRP": "Command Repeat",
             "CSA": "Called Subscriber Internet Address"
         }
         return abbrev