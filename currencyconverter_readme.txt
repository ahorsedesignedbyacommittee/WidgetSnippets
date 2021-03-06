currencyconverter is a simple currency conversion module. It includes one function, convert().

The syntax of this function is:

currencyconverter.convert(source_currency, target_currency, amount)

Where source_currency is the ISO 4217 code of the original currency in which the amount you want to convert is denominated;
target_currency is the ISO 4217 code of the currency to which you want to convert;
and amount is the amount in the source_currency you want to convert.

source_currency and target_currency are strings (not case-sensitive), amount can be a float or string.
The source and target currencies must be from the list of supported currencies (see below), otherwise the function will return an error message.

(For information on ISO currency codes, see https://en.wikipedia.org/wiki/ISO_4217)

For example: If you wish to convert an amount of US$1,000 into Japanese yen, the syntax would be:

currencyconverter.convert("USD", "JPY", 1000)

The function will return a float corresponding to the converted amount in the target currency. This float is unrounded, to leave users 
flexibility in determining the desired number of decimal places.

The exchange rates are automatically pulled and parsed from a website of the ECB which is available at
https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
This website gives exchange rates of a range of currencies against the euro. However, these rates can be used to calculate cross rates,
i.e. exchange rates of two non-euro currencies against each other. The ECB obtains the data which underlies this website on the basis of 
a data collection procedure conducted by central banks across Europe once per workiung day.

The following currencies are supported:

Currency		ISO 4217 code
-------------------------------
U.S. dollar		USD
Japanese yen		JPY
Bulgarian lev		BGN
Czech koruna		CZK
Danish krone		DKK
Pound Sterling		GBP
Hungarian forint	HUF
Polish zloty		PLN
Romanian leu		RON
Swedish krona		SEK
Swiss franc		CHF
Icelandic krona		ISK
Norwegian krone		NOK
Croatian kuna		HRK
Russian rouble		RUB
Turkish lira		TRY
Australian dollar	AUD
Brazilian real		BRL
Canadian dollar		CAD
Chinese renminbi yuan	CNY
Hong Kong dollar	HKD
Indonesian rupiah	IDR
Israeli shekel		ILS
Indian rupee		INR
South Korean won	KRW
Mexican peso		MXN
Malaysian ringgit	MYR
New Zealand dollar	NZD
Philippine peso		PHP
Singapore dollar	SGD
Thai baht		THB
South African rand	ZAR

Version 1.0, March 2021
