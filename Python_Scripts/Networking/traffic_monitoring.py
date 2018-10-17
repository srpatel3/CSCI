import subprocess as sub
import re
p = sub.Popen(('sudo', 'tcpdump','host dirt06.cs.olemiss.edu','-v', '-l'), stdout=sub.PIPE)
count = 0
# line = " dirt06.cs.olemiss.edu.4001 > s-bot.cs.olemiss.edu.4001: Flags [P.], cksum 0xc8fa (correct), seq 4931:4979, ack 4835, win 272, options [nop,nop,TS val 1974197339 ecr 2306126535], length 48"
# line1 = "12:39:45.168769 IP (tos 0x0, ttl 64, id 44345, offset 0, flags [DF], proto TCP (6), length 52)"
re1 = ".* length (.*)"
re2 = ".* length (.*)\\)"
# matches = re.match(re1,line)
# matches1 = re.match(re2,line)
MB = 0
GB = 0
try:
	while True:
		row = p.stdout.readline().strip()
		if not row:
			break
		# print row.rstrip()
		matches = re.match(re2,row)
		matches1 = re.match(re1,row)
		if matches:
			count += int(matches.group(1))
			if count > 1024*1024:
				count = 0
				MB+=1
				if MB > 2014:
					MB = 0
					GB += 1
		elif matches1:
			# print row
			# print matches1.group(1)
			# print matches1.group(0)
			count += int(matches1.group(1))
			if count > 1024*1024:
				count = 0
				MB+=1
				if MB > 2014:
					MB = 0
					GB += 1
		print "Total Data Transferred : GB : " + str(GB) + " MB : "+str(MB) + " KB "+str(count/1024) 

except Exception as e:
	print e
	print "Total Data Transferred : GB : " + str(GB) + " MB : "+str(MB) + " KB "+str(count/1024) 
