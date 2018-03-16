"""
Sample script to test ad-hoc scanning by table drive.
This accepts time in 24hour format (xx:xx, x:xx, x.xx, xx.xx) 
"""

def getchar(words,pos):
	""" returns groupChars at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	

	if words[pos] >= '0' and words[pos] <= '1':
		return 'ZERO_ONE'

	elif words[pos] == '2':
		return 'TWO'

	elif words[pos] >= '0' and words[pos] <= '3':
		return 'ZERO_THREE'

	elif words[pos] >= '0' and words[pos] <= '5':
		return 'ZERO_FIVE'

	elif words[pos] >= '0' and words[pos] <= '9':
		return 'ZERO_NINE'

	elif words[pos] == ':' or words[pos] == '.':
		return 'SEPARATOR'

	else:
		return 'OTHER'



	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char

			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary
td = { 
		'q0' : {'ZERO_ONE' : 'q1', 'TWO' : 'q2', 'ZERO_THREE' : 'q3', 'ZERO_FIVE' : 'q3', 'ZERO_NINE' : 'q3'},
		'q1' : {'SEPARATOR' : 'q5','ZERO_ONE': 'q3', 'TWO' : 'q3', 'ZERO_THREE' : 'q3' , 'ZERO_FIVE' : 'q3','ZERO_NINE' : 'q3'},
		'q2' : {'SEPARATOR' : 'q5', 'ZERO_ONE': 'q4', 'TWO' : 'q4', 'ZERO_THREE' : 'q4' },
		'q3' : {'SEPARATOR' : 'q5'},
		'q4' : {'SEPARATOR' : 'q5'},
		'q5' : {'ZERO_ONE': 'q6', 'TWO' : 'q6', 'ZERO_THREE' : 'q6', 'ZERO_FIVE' : 'q6'},
		'q6' : {'ZERO_ONE': 'q7', 'TWO' : 'q7', 'ZERO_THREE' : 'q7', 'ZERO_FIVE' : 'q7', 'ZERO_NINE' : 'q7'}
     } 


# the dictionary of accepting states and their
# corresponding token
ad = {'q7' : 'TIME_TOKEN'}




# get a string from input
text = input('give some input>')



# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position= scan(text,td,ad)
	
	if token == 'ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
text = text[position:]
