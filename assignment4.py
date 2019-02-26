
def padhexa(s):
    return '0x' + s[2:].zfill(16)

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

	
import random, subprocess, string
inlst1=[]
inlst2=[]
outlst1=[]
outlst2=[]
char_xor= int('0x0080820060000000',0)
for i in range(1):
	in1=''.join(random.choice(string.ascii_lowercase) for i in range(8))
	print(in1)
	if in1 not in inlst1:
		inlst1.append(in1)
		print(in1.encode('utf-8').hex())
		in2=int(in1.encode('utf-8').hex(),16)^char_xor
		print(hex(in2))
		in2=hex2str(hex(in2))
		
		inlst2.append(in2)
	

	args1="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in1+"\"}\' -k https://172.27.26.163:9000/des"
	args2="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+"password"+"\"}\' -k https://172.27.26.163:9000/des"
	out1=subprocess.check_output(args1,shell=True)
	out1=out1.decode('utf-8').split('"')[3]
	print(out1)
	outlst1.append(int(output(out1),0))

	out2=subprocess.check_output(args2,shell=True)
	out2=out2.decode('utf-8').split('"')[3]
	print(out2)
	outlst2.append(int(output(out2),0))




