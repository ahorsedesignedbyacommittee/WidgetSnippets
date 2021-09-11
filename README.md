# WidgetSnippets
Code snippets for little and unspectacular. but potentially useful, widgets that can be incorporated into your programs as functions.




--------------------------------------------------------------------------------------------
## CONVERSIONS (Python)

conversions is a simple module for some minor but handy conversions. It includes three functions:

- conversions.currency()
- conversions.numbersystems()
- conversions.shoesize()



### conversions.currency()


The syntax of this function is:

conversions.currency(source_currency, target_currency, amount)

Where source_currency is the ISO 4217 code of the original currency in which the amount you want to convert is denominated;
target_currency is the ISO 4217 code of the currency to which you want to convert;
and amount is the amount in the source_currency you want to convert.

source_currency and target_currency are strings (not case-sensitive), amount can be a float or integer.
The source and target currencies must be from the list of supported currencies (see below), otherwise the function will return an error message.

(For information on ISO currency codes, see https://en.wikipedia.org/wiki/ISO_4217)

For example: If you wish to convert an amount of US$1,000 into Japanese yen, the syntax would be:

conversions.currency("USD", "JPY", 1000)

The function will return a float corresponding to the converted amount in the target currency. This float is unrounded, to leave users 
flexibility in determining the desired number of decimal places.

The exchange rates are automatically pulled and parsed not from an API but from a website of the ECB which is available at
https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
This website gives exchange rates of a range of currencies against the euro. However, these rates can be used to calculate cross rates,
i.e. exchange rates of two non-euro currencies against each other. The ECB obtains the data which underlies this website on the basis of 
a data collection procedure conducted by central banks across Europe once per workiung day.

The following currencies are supported, together with their ISO 4217 code:

- U.S. dollar		USD
- Japanese yen		JPY
- Bulgarian lev		BGN
- Czech koruna		CZK
- Danish krone		DKK
- Pound Sterling		GBP
- Hungarian forint	HUF
- Polish zloty		PLN
- Romanian leu		RON
- Swedish krona		SEK
- Swiss franc		CHF
- Icelandic krona		ISK
- Norwegian krone		NOK
- Croatian kuna		HRK
- Russian rouble		RUB
- Turkish lira		TRY
- Australian dollar	AUD
- Brazilian real		BRL
- Canadian dollar		CAD
- Chinese renminbi yuan	CNY
- Hong Kong dollar	HKD
- Indonesian rupiah	IDR
- Israeli shekel		ILS
- Indian rupee		INR
- South Korean won	KRW
- Mexican peso		MXN
- Malaysian ringgit	MYR
- New Zealand dollar	NZD
- Philippine peso		PHP
- Singapore dollar	SGD
- Thai baht		THB
- South African rand	ZAR




### conversions.numbersystems()


The syntax of this function is:

conversions.numbersystems(source_system, target_system, number)

Where source_system is an integer representing the base of the system from which you want to convert (e.g. 2 for binary, 10 for decimal, 16 for hexadecimal),
target_system is an integer representing the base of the system you want to convert into,
and number is a string representing the number you want to convert. It is important to keep in mind that it is indeed a string, not an integer or a floating-point number (this is because in systems with base > 10, letters can be part of a number, e.g. hex F5 = decimal 245)

For systems with base > 10, letters will represent the digits from 10 (in decimal) upwards. The function can handle the usual ten digits plus the 26 (in decimal) letters of the alphabet, which means it accepts systems up to base-36 as source ansd target systems.

As an example: AF51 in hexadecimal: The A represents the digit 10 (in decimal), the F represents the digit 15 (in decimal).
AF51 (hex) = 10 * 16^3 + 15 * 16^2 + 5 * 16^1 + 1 * 16^0 = 10 * 4096 + 15 * 256 + 5 * 16 + 1 * 1 = 44881 (in decimal)

The entry of letters is not case sensitive.

The function can also handle floating point numbers, with a point as separator; e.g. 67.9 (decimal) = 124.620462 (base-7). It will omit the floating point and the subsequent digits if all digits after the point are zero; otherwise it will output a floating point and six subsequent digits. As in all programming languages, due to the internal workings of the computer being in binary, there can be minor rounding inaccuracies for the digits after the zero, so the function must be jused with caution as far as values < 1 are concerned.




### conversions.shoesize()


The syntax of this function is:

conversions.shoesize(source_system, target_system, size)

Where source_system is the (code for the) shoe size measurement system you start from, target_system is the system you want to convert to, and size is the shoe size in the source system that you want to convert. Output is a float corresponding to the shoe size in the target system, rounded to the usual precision used in that system (whole sizes for EU and Mondopoint, half sizes for UK and US). source_system and target_system are strings (not case-sensitive), size can be a float (for half sizes: .5) or integer.

Supported source and target systems are: UK adults (code: "UKa"), UK children ("UKc"), US customary male adults ("USm"), US customary female adults ("USf"), US customary children ("USc"), continental EU ("EU"), and Mondopoint ("MD"). For Mondpoint, the conversion takes into account only the foot length component, not the width; the width cannot be converted as the other systems do not include it in their sizes.

For example: If you wish to convert a shoe size of Mondpoint length 260 to a US female adult size, the syntax would be:

conversions.shoesize("MD", "USf", 255)

The output is 9.5; "MD" and "USf" are not case senitive.

The conversions can only be approximate. This is due to rounding, as sizes in one system do not exactly correspond to sizes in another. It is also due to the fact that the production standards of different shoe manufacturers differ. As a consequence, shoe sizes for different manufacturers may be slightly off from the numbers produced by this conversion tool.

For transparency reasons, it has to be pointed out that this tool makes use of the eval() function. The security risk has been mitigated by means of converting user input to a float number before feeding it into the eval() function.



### Version 3.0, May 2021


--------------------------------------------------------------------------------------------
## RELIGIOUSHOLIDAYS (Python)


religiousholidays is a simple module for the calculations of the dates of religious holidays. It includes two functions:

- religiousholidays.easter()
- religiousholidays.passover()

Both take one argument as input, an integer which corresponds to the year in the Gregorian calendar. easter() will return the date of Easter in the Gregorian calendar in this year; passover() will return the date of 15 Nisan, the first day of passover in the Jewish calendar, in that Gregorian year (note that leap months ensure that passover is either in March or April, hence there can be only one passover in each Gregorian calendar year). Note that, as per Jewish custom, the day is considered to start at sunset on the previous day, and ends at sunset on the date indicated.

Both will return their output as a tuple of two integers; the first of these corresponds to the day in March or April of the holiday in question, the second to the month (3 = March, 4 = April). So an output of (16, 4) would correspond to 16 April.

passover() uses the passover algorithm developed by Carl Friedrich Gauss; easter() uses Harold Spencer Jones' algorithm (originally published anonymously in 1876), which is less widely known than Gauss' Easter algorithm but more elegant (since it does not rely on explicitly formulated exceptions). 


### Version 1.0, September 2021

--------------------------------------------------------------------------------------------
## LEN_INDEXING (C)

len_indexing is meant as an implementation in C of some functions which exist off-the-shelf in Python and come in handy many times. 

It contains two functionS:

- len()
- index()

len() is an implementation of the Python function of the same name. It takes an integer as input and returns an integer corresponding to the number of digits in the input integer (its length). If need be, the data type of the input can easily be changed, e.g. to long int.

index() is an implementation of Python's feature to index integers. It takes two integers as inputs, the number you're interested in and the index you want to extract. Negative indexes are counted from the end starting with -1 (last digit has index -1, second-to-last digit -2); non-negative indexes are counted from the beginning, starting with 0 (first digit has index 0, second digit 1 etc). The return value is an integer corresponding to the digit of the nunber indentifieded by the selected index.

### Version 2.0, September 2021
