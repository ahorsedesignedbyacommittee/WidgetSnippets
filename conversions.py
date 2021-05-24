------------------------------------------------------------------------------------------------------------
def currency (source_currency, target_currency, amount):
	
	"""Converts between 33 different currencies, based on exchange rates parsed from an ECB-run website.
	
	Syntax: conversions.currency(source_currency, target_currency, amount; e.g.: conversions.currency("USD", "HKD", 500)
	Output: Float number corresponding to the amount converted into the target currency """
	
	def findcurrencyrate(x):
		
		# This function will retrieve the exchange rate of a desired currency
		# against the euro from the ECB website
		
		#Obtains the source code from the ECB website that has currency exchange rates in it
		import urllib.request
		import re
		source = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
		fh = urllib.request.urlopen(source)
		pagecode = fh.read()
		pagecode = str(pagecode.decode())
		fh.close()
		
		
		# Sets the exchange rate to 1 if the currency in question is the 
		# EUR (because all rates on the page are against the euro)
		# In case of other currencies, the function proceeds to parse
		# the source code of the ECB website for the corresponding
		# exchange rate (see below)
		if x == "EUR":
			rate = 1
		else:
			# Finds, inside the source code of the ECB website, the
			# HTML tag <td id="XXX" class="currency">
			# (where XXX is the currency code of the desired currency)
			
			currency_instance = '<td id="'+x+'" class="currency">'
			hit1 = pagecode.find(currency_instance)
			
			# Finds the first occurrence of the HTML tag
			# <span class="rate">
			# After the tag of the desired currency
			hit2 = pagecode.find('<span class="rate">', hit1)
			
			# Takes the first 30 pages after the HTML tag <span class="rate">
			# and uses regular expressions to find a floating point number,
			# which will be the rate for this currency
			hit3 = hit2 + 30
			stringtoparse = pagecode[hit2:hit3]
			match = re.search("[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)", stringtoparse)
			rate = match.group(0)
		return rate
		

	source_currency = source_currency.upper()
	target_currency = target_currency.upper()
	amount = float(amount)

	# Checks if the source and target currencies are among the supported
	# currencies
		
	list_of_currencies = ("USD", "JPY", "BGN", "CZK", "DKK", "EUR", "GBP", 
	"HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", 
	"AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", 
	"MYR", "NZD", "PHP", "SGD", "THB", "ZAR")

	if source_currency not in list_of_currencies:
		return ("Source currency not supported")
	if target_currency not in list_of_currencies:
		return ("Target currency not supported")
	else:
		# Obtains the exchange rates of the source currency and the target 
		# currency by calling the findcurrencyrate() function
		source_currency_rate = float(findcurrencyrate(source_currency))
		target_currency_rate = float(findcurrencyrate(target_currency))

		# Calculates the amount in the target currency on the basis of the 
		# exchange rates previously obtained
		new_amount = (amount / source_currency_rate) * target_currency_rate
		return (new_amount)

------------------------------------------------------------------------------------------------------------
	
def numbersystems (source_system, target_system, number):
	"""Converts numbers between different number systems (from binary, i.e. base-2, up to base-36)
	Syntax: conversions.numbersystems(source_system, target_system, number; e.g.: conversions.numbersystems(8, 16, "54.23")
	Output: String corresponding to the number converted into the target system. The string will contain a floating point if the converted number did """
    
    base_in = int(source_system)
    base_out = int(target_system)
    
    #Creates two dictionaries (one in each direction) for the characters that can
    #be used and their associated numerical values
    
    from string import ascii_uppercase, ascii_lowercase
    alphabet = ascii_uppercase
    digit_list = "0123456789"
    alphabet_and_digits = digit_list + alphabet
    char_value = {char:alphabet_and_digits.index(char) for char in alphabet_and_digits}
    inverted_dic = {char_value[item]:item for item in char_value}
    
    #Converts lower case letters (if any) in the input into upper case)
    
    number_adj = ""
    for x in number:
        if x in ascii_lowercase:
            number_adj += x.upper()
        else:
            number_adj += x
    number = number_adj

    def sum_calculator(s, p, i, step_p, step_i, b):
        """Handles the calculation of the inserted string into a mathematical sum"""
        sum = 0
        while True:
            if i < -len(s) and step_i == -1:
                break
            elif i + 1 > len(s) and step_i == 1:
                break
            else:
                sum += char_value[str(s[i])] * (b ** p)
                i += step_i
                p += step_p
        return sum
        #sum is now the numerical value of the inserted number (before the point)
        
    def from_sum_to_target_system (s, b):
        """Handles the conversion of the mathematical sum into the representation in the target system"""
        result_str = ""
        #Determines the maximum power that the calculation has to start with
        max_p = 0
        while True:
            if b ** max_p <= s:
                max_p += 1
            else:
                break
        max_p -= 1
        #Divides the sum progressively by the various powers of the base
        while True:
            new_digit = s // (b ** max_p)
            s -= (b ** max_p) * new_digit
            result_str += inverted_dic[new_digit]
            max_p -= 1
            if max_p == -1: result_str += "."
            if max_p < -6:
                break
        if result_str.split(".")[1] == "000000": return result_str.split(".")[0]
        else: return result_str
         

#Splits the inserted string, if there is a point, into the parts before and after that point, and
#calls the sum_calculator function to obtain the numercial sum
    if "." in number:
        number_split = number.split(".")
        sum_bp = sum_calculator(s=number_split[0], p=0, i=-1, step_p=1, step_i=-1, b = base_in)
        sum_ap = sum_calculator(s = number_split[1], p=-1, i=0, step_p=-1, step_i=1, b = base_in)
        sum = sum_bp + sum_ap
    else:
        sum = sum_calculator(s=number, p=0, i=-1, step_p=1, step_i=-1, b = base_in)
        
    return from_sum_to_target_system(s=sum, b=base_out)
	
------------------------------------------------------------------------------------------------------------
	
def shoesize(source_system, target_system, size):
	
    """Converts between shoe size measurement systems: UK (adults or children), US customary (male adults, female adults, children), EU, Mondpoint (length only)
	
    Syntax: conversions.shoesize(source_system, target_system, size; e.g.: conversions.shoesize("UKa", "USm", 10.5)
    Output: Number corresponding to the shoe size in the target system"""
    

    #Provides a dictionary of formulas to convert the size 
    #from the various source systems into the length 
    #of the last made to use it
    
    lastlengthformula = {
        "uka": "25.4*(size + 25)/3",
        "ukc": "25.4*(size + 12)/3",
        "usm": "25.4*(size + 24)/3",
        "usf": "25.4*(size + 23)/3", 
        "usc": "25.4*(size + 11.667)/3",
        "eu": "size*10*0.667",
        "md": "size + 15"}
        
    #Picks the applicable formula from the lastlengthformula dictionary  
    #and uses it to calculate the lastlength (in millimetres)
    	
    size = float(size) #For security reasons, as this will feed into eval()
    lastlength_mm = eval(lastlengthformula[source_system.lower()])
    
    #Provides a dictionary of formulas to convert the last length 
    #into the shoe size for the various systems
    
    sizeformula = {
        "uka": "(lastlength_mm/25.4)*3 - 25",
        "ukc": "(lastlength_mm/25.4)*3 - 12",
        "usm": "(lastlength_mm/25.4)*3 - 24",
        "usf": "(lastlength_mm/25.4)*3 - 23", 
        "usc": "(lastlength_mm/25.4)*3 - 11.667",
        "eu": "lastlength_mm*0.15",
        "md": "lastlength_mm - 15"
        }
    
    #Picks the applicable formula from the sizeformula dictionary 
    #and uses it to calculate the shoe size in the target system
    
    shoesize = eval(sizeformula[target_system.lower()])
    
    #Rounds to the precision typically used in the target system and
    #returns the result
    
    if target_system.lower() in ["eu", "md"]:
        return round(shoesize)
    if target_system.lower() in ["uka", "ukc", "usm", "usf", "usc"]:
        return round(shoesize * 2.0) / 2.0
