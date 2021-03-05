def convert (source_currency, target_currency, amount):
	
	# This is the main function, which will continue in line 52.
	# It calls the sub-function findcurrencyrate() to retrieve 
	# the exchange rates for the source and target currencies online
		
	def findcurrencyrate(x):
		
		# This function will retrieve the exchnage rate of a desired currency
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
