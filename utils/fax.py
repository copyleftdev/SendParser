class FaxUtils(object):
    def get_send_abbreviation(self):
        """Returns a list of Fax T.30 Abbreviations"""
        abbrev = {
            "CFR": "Confirmation To Receive",
            "CIG": "Calling Subscriber Identification",
            "CRP": "Command Repeat",
            "CSA": "Called Subscriber Internet Address",
            "CSI": "Called Subscriber Identification",
            "CTR": "Response for Continue to Correct",
            "DCN": "Disconnect",
            "DCS": "Digital Command Signal",
            "DIS": "Digital Identification Signal",
            "DTC": "Digital Transmit Command",
            "EOM": "End Of Message",
            "EOP": "End of Procedure",
            "EOR": "End of Retransmission",
            "EOS": "End Of Selection",
            "FCD": "Facsimile Coded Data",
            "FCF": "Facsimile Control Field",
            "FIF": "Facsimile Information Field",
            "FDM": "File Diagnostics Message",
            "FTT": "Failure To Train",
            "HDLC": "High-level Data Link Control",
            "JM": "Joint Menu See ITU-T Rec. V.8. F.5",
            "MCF": "Message Confirmation",
            "MPh": "Half Duplex Modulation Parameter See ITU-T Rec. V.34. F.3.1.4",
            "MPS": "Multipage Signal",
            "NSC": "Non-standard facilities Command",
            "NSF": "Non-standard Facilities",
            "NSS": "Non-standard Set-up",
            "PID": "Procedure Interrupt Disconnect",
            "PIN": "Procedure Interrupt Negative",
            "PIP": "Procedure Interrupt Positive",
            "PPR": "Partial Page Request",
            "PPS": "Partial Page Signal",
            "PRI-EOM": "Procedure Interrupt-EOM",
            "PRI-EOP": "Procedure Interrupt-EOP",
            "PRI-MPS": "Procedure Interrupt-MPS",
            "PPS-NULL": "Partial Page Signal-Null",
            "PWD": "Password(for polling)",
            "RCP": "Return to Control for Partial page",
            "RNR": "Receive Not Ready",
            "RR": "Recieve Ready",
            "RTN": "Retrain Negative",
            "RTP": "Retrain Positive",
            "SEP": "Selective Polling",
            "SID": "Sender Identification",
            "SUB": "Subaddress",
            "TCF": "Training Check Zeros",
            "TSI": "Transmitting Subscriber Identification",
            "XID": "EXchange IDentification procedure",
        }
        return abbrev

    def get_inbound_codes():

        error_codes = {
            "errors": [
                {
                    "329": "Special Info. Tone: invalid #",
                    "331": "Special Info. Tone: no circuit",
                    "327": "Invalid Number or No service",
                    "303": "Fast busy (trunk lines busy)",
                    "301": "Normal Busy",
                    "318": "Dialtone remains after dial sequence",
                    "325": "Ringing timed out (no answer)",
                    "328": "Possible dead line after dial",
                    "316": "Answer detected, probable human",
                    "4104": "Tx Error",
                    "328215": "T30 Protocol error",
                }
            ],
            "CALLCONNECTED": [{"0": "CallerID"}],
            "CALLOVER": [
                {
                    "0=NMSINFO": "Call over duration -> ## secs.",
                    "0=BTINFO": "Call over duration -> XX secs.",
                }
            ],
            "CALL_DISCONNECTED": [
                {"-2=BTINFO": "CNG tone detected for voice only user!"}
            ],
        }
