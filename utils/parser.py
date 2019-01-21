import re
import time
from tinydb import TinyDB, Query


class LogParser(object):
    def parser(self, log_line):
        cur_epoch = int(time.time())
        db = TinyDB("data/sendparser.{}.db".format(cur_epoch))

        DATE_RE = r"(\w{3}\s+\d+\s\d+:\d+:\d+)"
        SERVER_NAME_RE = r"(\sdid\d+)"
        INBOUND_WORKER_RE = r"(inbound\[\d+\])"
        EMAIL_RE = r"(?<=email=)(.*)(?=, msgid)"
        DID_RE = r"(?<=did=)(.*)(?=, email)"
        STAT_RE = r"(stat=\w+)"
        MSG_ID_RE = r"(?<=msgid=<)(.*)(?=>)"

        if "Clearing Cache Memory" in log_line:
            pass
        else:
            d_match = re.findall(DATE_RE, log_line)
            s_match = re.findall(SERVER_NAME_RE, log_line)
            in_match = re.findall(INBOUND_WORKER_RE, log_line)
            em_match = re.findall(EMAIL_RE, log_line)
            did_match = re.findall(DID_RE, log_line)
            stat_match = re.findall(STAT_RE, log_line)
            msgid_match = re.findall(MSG_ID_RE, log_line)

            log_transform = {
                "date": d_match[0],
                "server": s_match[0].replace(" ", ""),
                "inbound_worker": in_match[0].replace("inbound[", "").replace("]", ""),
                "email": em_match[0].replace("|2", ""),
                "did": did_match[0],
                "state": stat_match[0].replace("stat=", ""),
                "message_id": "".join(msgid_match),
            }

            print(log_transform)
            db.insert(log_transform)
