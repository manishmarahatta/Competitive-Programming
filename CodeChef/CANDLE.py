T = int (raw_input ())

for i in range (T) :
	min_candles ,min_candle_digit = 9, 0
	candles = map (int, raw_input ().split ())	
	zero_candles = candles[0]	
	for j in range (1, len (candles)) :
		if min_candles > candles[j] :
			min_candles = candles[j]
			min_candle_digit = j

	output = ""

	if zero_candles < min_candles :
		output += str (1)
		for j in range (zero_candles + 1) :
			output += str (0)
		print output
	else :
		for j in range (min_candles + 1) :
			output += str (min_candle_digit)
		print output
