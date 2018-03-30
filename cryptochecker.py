import requests


#previousAmount = open("previousAmount.txt", "r").read()

Gemini_BTC_Amount = 0.00000000
Gemini_ETH_Amount = 0.00000000

Gdax_BTC_Amount = 0.00000000
Gdax_ETH_Amount = 0.00000000
Gdax_LTC_Amount = 0.00000000

Total_USD_Investment = 00.00
Total_BTC_Investment = 00.00

## URLs ##
##############################################################################
CoinbaseBTC = 'https://api.coinbase.com/v2/prices/spot?currency=USD'

GdaxBTC = 'https://api.gdax.com/products/BTC-USD/ticker'
GdaxETH = 'https://api.gdax.com/products/ETH-USD/ticker'
GdaxLTC = 'https://api.gdax.com/products/LTC-USD/ticker'

GeminiBTC = 'https://api.gemini.com/v1/pubticker/btcusd'
GeminiETH = 'https://api.gemini.com/v1/pubticker/ethusd'



## Get json data from exchanges ##
###############################################################################
get_Coinbase_BTC = requests.get(CoinbaseBTC)
resjson = get_Coinbase_BTC.json()
Coinbase_BTC_Rate = resjson["data"]["amount"]

get_Gdax_BTC = requests.get(GdaxBTC)
resjson = get_Gdax_BTC.json()
Gdax_BTC_Rate = resjson["ask"]

Gdax_LTC_Rate = requests.get(GdaxLTC)
resjson = Gdax_LTC_Rate.json()
Gdax_LTC_Rate = resjson["ask"]

get_Gdax_ETH = requests.get(GdaxETH)
resjson = get_Gdax_ETH.json()
Gdax_ETH_Rate = resjson["ask"]



get_Gemini_BTC = requests.get(GeminiBTC)
resjson = get_Gemini_BTC.json()
Gemini_BTC_Rate = resjson["ask"]

get_Gemini_ETH = requests.get(GeminiETH)
resjson = get_Gemini_ETH.json()
Gemini_ETH_Rate = resjson["ask"]



## We all float down here, strings to floats ##
###############################################################################
dec_Coinbase_BTC_Rate = float(Coinbase_BTC_Rate)

dec_Gdax_BTC_Rate = float(Gdax_BTC_Rate)
dec_Gdax_LTC_Rate = float(Gdax_LTC_Rate)
dec_Gdax_ETH_Rate = float(Gdax_ETH_Rate)

dec_Gemini_BTC_Rate = float(Gemini_BTC_Rate)
dec_Gemini_ETH_Rate = float(Gemini_ETH_Rate)




## Conversions of numbers ##
###############################################################################
converted_Coinbase_BTC = dec_Gemini_BTC_Rate*Gemini_BTC_Amount

converted_Gdax_BTC = dec_Gdax_BTC_Rate*Total_BTC_Investment
converted_Gdax_LTC = dec_Gdax_LTC_Rate*Gdax_LTC_Amount
converted_Gdax_ETH = dec_Gdax_ETH_Rate*Gdax_ETH_Amount

converted_Gemini_BTC = dec_Gemini_BTC_Rate*Total_BTC_Investment
converted_Gemini_ETH = dec_Gemini_ETH_Rate*Gemini_ETH_Amount

average_BTC_Price = ((dec_Gdax_BTC_Rate+dec_Gemini_BTC_Rate)/2)

currentAmount = (average_BTC_Price*Total_BTC_Investment)
currentAmount = round(currentAmount,2)
previousAmount = float(previousAmount)



## Write totalAmount to file on disk ##
###############################################################################
#f = open('previousAmount.txt', 'w')
#f.write(str(currentAmount))
#f.close()



# percentageDif = (((currentAmount-previousAmount)/previousAmount)*100)

# if percentageDif == 0.0:
	# percentageDif = "0.00000"
# elif percentageDif < 0:
	# percentageDif = round(percentageDif, 4)
# elif percentageDif > 0:
	# percentageDif = round(percentageDif, 5)

# percentageStr = str(percentageDif)
		
# numbers = sum(c.isdigit() for c in percentageStr)

# while (numbers < 5) and (percentageDif > 0):
	# percentageStr = percentageStr + "0"
	# numbers = numbers + 1

		
	
	
print ""
print ""
print "+----------------------------------------------------------+"
print "  GDAX    BTC :  ${0:.2f}".format(dec_Gdax_BTC_Rate)," X ",Total_BTC_Investment," BTC = ${0:.2f}".format(converted_Gdax_BTC)
print "  GDAX    ETH :   ${0:.2f}".format(dec_Gdax_ETH_Rate)
print "  GDAX    LTC :   ${0:.2f}".format(dec_Gdax_LTC_Rate)
print "|----------------------------------------------------------|"
print "  Gemini  BTC :  ${0:.2f}".format(dec_Gemini_BTC_Rate)," X ",Total_BTC_Investment," BTC = ${0:.2f}".format(converted_Gemini_BTC)
print "  Gemini  ETH :   ${0:.2f}".format(dec_Gemini_ETH_Rate)
print "|----------------------------------------------------------|"
print ""
print "  Average BTC Price : ${0:.2f}".format(average_BTC_Price)
print ""
print "               Total Investment  : ${0:.2f}".format(Total_USD_Investment)
print "               Current Value     : ${0:.2f}".format(currentAmount)
print "                                  ---------"
print "                         Change  : ${0:.2f}".format(currentAmount - Total_USD_Investment) + "     {0:.2f}".format(((currentAmount - Total_USD_Investment)/Total_USD_Investment)*100), "%"
print ""
print "+----------------------------------------------------------+"
print ""