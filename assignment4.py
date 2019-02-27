
def padhexa(s): 
    return '0x' + s[2:].zfill(16)

def padbin(s):
	return '0b'+s[2:].zfill(64)

def padbin32(s):
	return '0b'+s[2:].zfill(32)

def hex2str(str):
	padhexa(str)
	lst=[]
	for i in range(2,18,2):
		x=chr(int(str[i:i+2],16))
		lst.append(x)
	lst=''.join(lst);
	return lst

def output(outp): #reducing the output to usable form
	lst=['0x']
	for i in range(len(outp)):
		lst.append(hex(ord(outp[i])-ord('f'))[2])
	return ''.join(lst)

def swap(str): #swapping the halfs of the output of the last round
	str=padbin(str)
	str=str[2:]
	str_l=str[0:32]
	str_r=str[32:]
	return '0b'+str_r+str_l


def inv_ip(s): #computing the inverse of initial permutation of a string
	s=padbin(s)
	s=s[2:]
	lst=[]
	perm=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
	for i in range(1,65):
		ind=perm.index(i)
		lst.append(s[ind])
	s='0b'+''.join(lst)
	return int(s,0)

def ip(s): #computing the initial permutation of a string
	s=padbin(s)
	s=s[2:]
	lst=[]
	perm=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
	for i in range(1,65):
		ind=perm.index(i)
		lst.append(s[ind])
	s='0b'+''.join(lst)
	return int(s,0)

def inv_s_permut(s): # computing inverse of s-boxes permutation
	s=padbin32(s)
	s=s[2:]
	lst=[]
	perm =[16, 7, 20, 21, 29, 12, 28, 17,1, 15, 23, 26, 5, 18, 31, 10,2, 8, 24, 14, 32, 27, 3, 9,19, 13, 30, 6, 22, 11, 4, 25]
	for i in range(1,33):
		ind=perm.index(i)
		lst.append(s[ind])
	s='0b'+''.join(lst)
	return int(s,0)

def expand(block): # expansion box
	block=block[2:]
	table=[32, 1, 2, 3, 4, 5,4, 5, 6, 7, 8, 9,8, 9, 10, 11, 12, 13,12, 13, 14, 15, 16, 17,16, 17, 18, 19, 20, 21,20, 21, 22, 23, 24, 25,24, 25, 26, 27, 28, 29,28, 29, 30, 31, 32, 1]
	lst=[block[x-1] for x in table]
	return '0b'+''.join(lst)



import random, subprocess, string
inlst1=[]
inlst2=[]
outlst1=[]
outlst2=[]

char_xor= int('0x4008000004000000',0) #input XOR for S boxes after initial permutation
in_xor=inv_ip(bin(char_xor)) #XOR corresponding before initial permutation 


for i in range(1):
	in1=''.join(random.choice(string.ascii_lowercase) for i in range(8))
	print(in1)
	if in1 not in inlst1:
		inlst1.append(in1)
		in2=int(in1.encode('utf-8').hex(),16)^in_xor
		in2=hex2str(hex(in2))
		print(in2)
		inlst2.append(in2)
	

	args1="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in1+"\"}\' -k https://172.27.26.163:9000/des"
	args2="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in2+"\"}\' -k https://172.27.26.163:9000/des"
	out1=subprocess.check_output(args1,shell=True)
	out1=out1.decode('utf-8').split('"')[3]
	print(out1)
	out1=swap(bin(ip(bin(int(output(out1),0))))) #output of the final round before initial permutation and swapping

	out2=subprocess.check_output(args2,shell=True)
	out2=out2.decode('utf-8').split('"')[3]
	print(out2)
	out2=swap(bin(ip(bin(int(output(out2),0))))) #output of the final round before initial permutation and swapping

	out_xor=padbin(bin(int(out1,0)^int(out2,0))) #output XOR 
	print(out_xor)
	last_in_xor='0b'+out_xor[2:34]
	last_in_1='0b'+out1[2:34] #input for final round
	last_in_2='0b'+out2[2:34]
	
	last_out_xor='0b'+out_xor[34:]
	
	ex_in_xor=expand(last_in_xor) 
	ex_in_1=expand(last_in_1) #input for S box
	ex_in_2=expand(last_in_2)#input for S box

	print(last_out_xor)
	s_out_xor=inv_s_permut(bin(int('0x04000000',0)^int('10000100110000011001001101000110',2)^int(last_out_xor,0))) #computing output XOR for S boxes
	print((ex_in_1))
	print((ex_in_2))
	print((ex_in_xor))
	print(padbin32(bin(s_out_xor)))





	
