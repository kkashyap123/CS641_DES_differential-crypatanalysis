
def padhexa(s):
    return '0x' + s[2:].zfill(16)

def padbin(s):
	return '0b'+s[2:].zfill(64)

def hex2str(str):
	padhexa(str)
	lst=[]
	for i in range(2,18,2):
		x=chr(int(str[i:i+2],16))
		lst.append(x)
	lst=''.join(lst);
	return lst

def output(outp):
	lst=['0x']
	for i in range(len(outp)):
		lst.append(hex(ord(outp[i])-ord('f'))[2])
	return ''.join(lst)

def inv_ip(s):
	s=padbin(s)
	print(s)
	s=s[2:]

	lst=[]
	perm=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
	for i in range(1,65):
		ind=perm.index(i)
		lst.append(s[ind])
	s='0b'+''.join(lst)
	return int(s,0)

import random, subprocess, string
inlst1=[]
inlst2=[]
outlst1=[]
outlst2=[]

init_xor= int('0x0080820060000000',0)
char_xor=inv_ip(bin(init_xor))

for i in range(1):
	in1=''.join(random.choice(string.ascii_lowercase) for i in range(8))
	print(in1)
	if in1 not in inlst1:
		inlst1.append(in1)
		in2=int(in1.encode('utf-8').hex(),16)^char_xor
		in2=hex2str(hex(in2))
		print(in2)
		inlst2.append(in2)
	

	args1="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in1+"\"}\' -k https://172.27.26.163:9000/des"
	args2="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in2+"\"}\' -k https://172.27.26.163:9000/des"
	out1=subprocess.check_output(args1,shell=True)
	out1=out1.decode('utf-8').split('"')[3]
	print(out1)
	outlst1.append(int(output(out1),0))

	out2=subprocess.check_output(args2,shell=True)
	out2=out2.decode('utf-8').split('"')[3]
	print(out2)
	outlst2.append(int(output(out2),0))


