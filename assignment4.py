
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

def padbin6(s):
	return s[2:].zfill(6)


def creare_xor_table(n):
	matrix=[]
	for i in range(64):
		row=[]
		for j in range(16):
			lst=[]
			row.append(lst)
		matrix.append(row)


	s = [
	         
	[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
	 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
	 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
	 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
	],

	[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
	 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
	 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
	 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
	],

	[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
	 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
	 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
	 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
	],

	[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
	 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
	 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
	 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
	],  

	[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
	 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
	 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
	 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
	], 

	[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
	 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
	 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
	 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
	], 

	[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
	 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
	 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
	 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
	],
	   
	[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
	 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
	 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
	 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
	]
	]	
	for in_xor in range(64):
		for j in range(64):
			k=j^in_xor
			k=padbin6(bin(k))
			j=padbin6(bin(j))
			k_r= int(str(k[0])+str(k[5]),2)
			k_c=int(k[1:5],2)
			j_r= int(str(j[0])+str(j[5]),2)
			j_c=int(j[1:5],2)
			out_xor=s[n][j_r][j_c]^s[n][k_r][k_c]

			if j not in matrix[in_xor][out_xor]:
				matrix[in_xor][out_xor].append(int(j,2))
			if k not in matrix[in_xor][out_xor]:	
				matrix[in_xor][out_xor].append(int(k,2))
	return matrix



import random, subprocess, string
inlst1=[]
inlst2=[]
outlst1=[]
outlst2=[]

char_xor= int('0x4008000004000000',0) #input XOR for S boxes after initial permutation
in_xor=inv_ip(bin(char_xor)) #XOR corresponding to characterstic XOR before initial permutation 


xor_table=[] #a 4D matrix where firsr coordinate is corr S-BOX 2 nd coordinate is input XOR, 3rd coordinate is output XOR and resulting is a list of possible input
for i in range(8):
	xor_table.append(creare_xor_table(i))

key_set=[]
Final=[]
for i in range(5):
	key_set.append({})

count=0

for i in range(1600): #trying for 1600 inputs
	in1=''.join(random.choice(string.ascii_lowercase) for i in range(8))
	#print(in1)
	if in1 not in inlst1:
		inlst1.append(in1)
		in2=int(in1.encode('utf-8').hex(),16)^in_xor
		in2=hex2str(hex(in2))
		#print(in2)
		inlst2.append(in2)
	
	try:
		args1="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in1+"\"}\' -k https://172.27.26.163:9000/des"
		args2="curl -H \"Content-Type: application/json\" --request POST --data \'{\"teamname\":\"team5\",\"password\":\"ayz11ospfc\", \"plaintext\":\""+in2+"\"}\' -k https://172.27.26.163:9000/des"
		out1=subprocess.check_output(args1,shell=True)
		out1=out1.decode('utf-8').split('"')[3]
		#print(out1)
		
		out2=subprocess.check_output(args2,shell=True)
		out2=out2.decode('utf-8').split('"')[3]
		#print(out2)
		if(len(out2)<20):
			out2=swap(bin(ip(bin(int(output(out2),0))))) #output of the final round before initial permutation and swapping
			out1=swap(bin(ip(bin(int(output(out1),0))))) #output of the final round before initial permutation and swapping

			out_xor=padbin(bin(int(out1,0)^int(out2,0))) #output XOR 
			#print(out_xor)
			last_in_xor='0b'+out_xor[2:34]
			last_in_1='0b'+out1[2:34] #input for final round
			last_in_2='0b'+out2[2:34]
			
			last_out_xor='0b'+out_xor[34:]
			
			ex_in_xor=expand(last_in_xor) 
			ex_in_1=expand(last_in_1) #input for S box
			ex_in_2=expand(last_in_2)#input for S box

			#print(last_out_xor)
			s_out_xor=inv_s_permut(bin(int('0x04000000',0)^int('10000100110000011001001101000110',2)^int(last_out_xor,0))) #computing output XOR for S boxes
			#print((ex_in_1))
			#print((ex_in_2))
			#print((ex_in_xor))
			#print(padbin32(bin(s_out_xor)))
			s_out_xor=padbin32(bin(s_out_xor))

			ex_in=[]  #input to S2, S5,S6,S7,S8 boxes
			EX_IN=[]                                                          #a whole input block
			ex_in.append('0b'+ex_in_1[8:14])
			EX_IN.append('0b'+ex_in_1[8:14])
			ex_in.append('0b'+ex_in_1[26:32])
			EX_IN.append(ex_in_1[26:32])
			ex_in.append('0b'+ex_in_1[32:38])
			EX_IN.append(ex_in_1[32:38])
			ex_in.append('0b'+ex_in_1[38:44])
			EX_IN.append(ex_in_1[38:44])
			ex_in.append('0b'+ex_in_1[44:50])
			EX_IN.append(ex_in_1[44:50])
			EX_IN=''.join(EX_IN)

			ex_in_x=[] #input XOR to S2, S5,S6,S7,S8 boxes
			ex_in_x.append('0b'+ex_in_xor[8:14])
			ex_in_x.append('0b'+ex_in_xor[26:32])
			ex_in_x.append('0b'+ex_in_xor[32:38])
			ex_in_x.append('0b'+ex_in_xor[38:44])
			ex_in_x.append('0b'+ex_in_xor[44:50])

			s_out=[] #output XOR to S2, S5,S6,S7,S8 boxes
			s_out.append('0b'+s_out_xor[6:10])
			s_out.append('0b'+s_out_xor[18:22])
			s_out.append('0b'+s_out_xor[22:26])
			s_out.append('0b'+s_out_xor[26:30])
			s_out.append('0b'+s_out_xor[30:34])

			


			#print(s_out)
			#print(ex_in_x)
			#print(ex_in)

##			for k in range(5):
##				if k==0:
##					lst=xor_table[1][int(ex_in_x[k],0)][int(s_out[k],0)]
##					for val in lst:
##						key=val^int(ex_in[k],0) #computing key for each possible input
##						if key not in key_set[k]:
##							key_set[k].update({key:1})
##						else:
##							key_set[k][key]+=1
##				else:
##					lst=xor_table[k+3][int(ex_in_x[k],0)][int(s_out[k],0)]
##					for val in lst:
##						key=val^int(ex_in[k],0)
##						if key not in key_set[k]:
##							key_set[k].update({key:1})
##						else:
##							key_set[k][key]+=1
			for int1 in xor_table[1][int(ex_in_x[0],0)][int(s_out[0],0)]:                         #combine the different s-box inputs
                            for int2 in xor_table[4][int(ex_in_x[1],0)][int(s_out[1],0)]:
                                for int3 in xor_table[5][int(ex_in_x[2],0)][int(s_out[2],0)]:
                                    for int4 in xor_table[6][int(ex_in_x[3],0)][int(s_out[3],0)]:
                                        for int5 in xor_table[7][int(ex_in_x[4],0)][int(s_out[4],0)]:
                                             val=[]
                                             val.append(bin(int1)[2:].zfill(6))
                                             val.append(bin(int2)[2:].zfill(6))
                                             val.append(bin(int3)[2:].zfill(6))
                                             val.append(bin(int4)[2:].zfill(6))
                                             val.append(bin(int5)[2:].zfill(6))
                                             val=''.join(val)
                                             val='0b'+val
                                             val=int(val,0)
                                             Final.append(val^int(EX_IN,0))
##                        for itr in values:
##                                Final=Final.append(itr^int(EX_IN,0)                                                  
			#print(key_set)
			
		else: #if output is not a string
			continue
		
		
	except:
		count+=1
		continue


print(1600-count)

##for dic in key_set:  #maximum occuring key for each of S2, S5,S6,S7,S8
##	print(max(zip(dic.values(), dic.keys())))
from collections import Counter
print(Final[0:20])
most_common,num_most_common = Counter(Final).most_common(1)[0]
print(most_common,num_most_common)
"""
count=0
for dic in key_set:
	print(count)
	for key in dic:
		if dic[key]>100:
			print(dic[key],key)
	count+=1
"""		
