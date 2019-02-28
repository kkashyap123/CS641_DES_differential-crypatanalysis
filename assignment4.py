
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

def creare_xor_table(n):
	matrix=[]
	for i in range(64):
		row=[]
		for j in range(64):
			lst=[]
			row.append(lst)
		matrix.append(row)

	s = [         
	[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
 	0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
 	4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
 	15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,
	],

	[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
 	3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
 	0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
 	13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9,
	],

	[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
 	13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
 	13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
 	1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,
	],

	[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
 	13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
 	10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
 	3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,
	],  

	[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
	 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
	 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
	 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,
	], 

	[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
	 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
	 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
	 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,
	], 

	[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
	 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
	 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
	 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
	],
	   
	[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
	 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
	 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
	 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11,
	]
	]	
	for i in range(64):
		in_xor=i
		for j in range(64):
			k=j^i
			out_xor=s[n][j]^s[n][k]
			if j not in matrix[in_xor][out_xor]:
				matrix[in_xor][out_xor].append(j)
				matrix[in_xor][out_xor].append(k)
	return matrix


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

	xor_table=[]
	for i in range(8):
		xor_table.append(creare_xor_table(i))




	
