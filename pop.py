import os, sys, string
import poplib
import getpass
host = "pop3.163.com"

username = raw_input('Username:')


pp = poplib.POP3(host)

pp.set_debuglevel(1)

pp.user(username)

pp.pass_(getpass.getpass())

action =""

if len(sys.argv) > 1:
   action = sys.argv[1]

if action == 'stat':
   ret = pp.stat()
   print ret
  # sys.exit()

elif action == 'list':
     ret = pp.list()
     print ret

elif action =='retr':
  down = pp.retr(1)
  print 'lines:', len(down)

  for line in down[1]:
      print line
elif action == 'quit':
  pp.quit()
elif action == 'delete':
   ret = pp.list()
   if ret[0].startswith('+OK'):
     msglist = ret[1]
     for msgspec in msglist :
        msgnum = int(msgspec.split(' ')[0])
        print "Deleting msg "
        pp.dele(msgnum)
else:
 print "I dont know this command"
