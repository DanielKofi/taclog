import os
import time
import requests
import json
import re
#grab device# cisco-[^\s]+)(\s.)((cc|zz|rm)\w{5})
#grab command#cmd=((?:\S|\s(?!\s))*)
#grab username#(cc|zz|rm)\w....


pattern = re.compile('(\w{1,3}\s+\d{1,2}\s\d{1,2}:\d{1,2})(:\d{1,2}\s+)(cisco-[^\s]+)(\s+)((cc|zz|rm)\w{5})([^cmd]).*cmd=((?:\S|\s(?!\s))*)')

#pattern = re.compile('(\w{1,3}\s\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\s+)(cisco-[^\s]+)(\s+)((cc|zz|rm)\w{5})([^cmd]).*cmd=((?:\S|\s(?!\s))*)')

my_dict = {
'cceadan':'Daniel Ansong',
'zzaardb' : 'Ross Bates',
'rmhzhoc' : 'Henry Chimah',
'ccaampa' : 'Paul Ayling',
'ccaareb' : 'Roy Banks',
'cceaook' : 'Ovie Okoro',
'ccaatmh' : 'Tarig Hanid',
'ccaacrh' : 'Craig hurley',
'ccaacrb' : 'Colin Byelong',
'ccaasol' : 'Smith Oliveria'}

a = ['cceadan','zzaardb','rmhzhoc','ccaampa','ccaareb','cceaook','ccaatmh','ccaacrh','ccaampa','cceasfo','ccaacrb','ccaasol']
Rpattern = r"cisco-[^\s]+"
Spattern = r"\bstart\b"
Dpattern = r"disc"
pats = [r"cisco-[^\s]+"]
def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)



    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

for line in follow('/var/log/tacacs/tacplus.acc'):
    #if re.search(Rpattern, line) and any(x in line for x in a):
    if re.match('(\w{1,3}\s+\d{1,2}\s\d{1,2}:\d{1,2})(:\d{1,2}\s+)(cisco-[^\s]+)(\s+)((cc|zz|rm)\w{5})([^cmd]).*cmd=((?:\S|\s(?!\s))*)',line):
        print(line)
        match = pattern.match(line)
        newline = (match.group(1) + '  ' + (my_dict['{0}'.format(match.group(5))]) +' ' + match.group(3) + ' ' +  '' + '>>>>' + ' '  + match.group(8))
        print     (match.group(1) + '  ' + (my_dict['{0}'.format(match.group(5))]) +' ' + match.group(3) + ' ' +  '' + '>>>>' + ' '  + match.group(8))


        url = 'https://outlook.office.com/webhook/259922d6-28bb-4426-ac14-a44f8da775b9@1faf88fe-a998-4c5b-93c9-210a11d9a5c2/IncomingWebhook/59011a10e8f545f08f369f25967bd404/43bfe760-7689-4d0b-96fd-46b265519580'
        message = {
            'text': newline
        }
        response_body = requests.post(url=url,data=json.dumps(message))
        #print(line)


