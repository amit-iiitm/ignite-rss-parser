def reverse(inp_str):
	word_list=inp_str.split()
	reversed_string=""
	for word in word_list:
		curr_word=""
		spec_char=0
		for i in range(len(word)):
			if word[i].isalpha() or word[i].isdigit() or word[i]=='-':
				curr_word+=word[i]
			else:
				spec_char=1
				reversed_string+=curr_word[::-1]
				reversed_string+=word[i]
				if i+1>=len(word):
					reversed_string+=' '
				curr_word=""

		if spec_char==0:
			reversed_string+=curr_word[::-1] + ' '
		if curr_word !="" and spec_char==1:
			reversed_string+=curr_word[::-1] + " "
	print reversed_string	

if __name__=="__main__":
	inp_str=raw_input()
	reverse(inp_str)
