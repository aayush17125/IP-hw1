#Aayush Gupta
#2017125
import urllib.request
import datetime
def weather_response(location, API_key):
	data = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+API_key)
	data = data.read()
	data= data.decode("utf-8")
	return data

def has_error(location,json):
	json=json.lower()
	location=location.lower()
	location=location.replace(" ","")
	json=json.replace(" ","")
	if json.find(location) == -1:
		return True
	else:
		return False

def get_temperature (json, n, t):
	if 0<= n <= 4:
		today = datetime.date.today()
		required_date = today+datetime.timedelta(n)
		index_find = str(required_date)+" "+str(t)
		data_of_required_date= json.find(index_find)
		tp = json.find("temp",data_of_required_date-350)
		tp_a = json.find(",",tp)
		tp_b = json[tp+6 : tp_a]
		return float(tp_b)
	else:
		return 0

def get_humidity(json, n, t):
	if 0<= n <= 4:
		today = datetime.date.today()
		required_date = today+datetime.timedelta(n)
		index_find = str(required_date)+" "+str(t)
		data_of_required_date= json.find(index_find)
		hd = json.find("humidity",data_of_required_date-350)
		hd_a = json.find(",",hd)
		hd_b = json[hd+10 : hd_a]
		return float(hd_b)
	else:
		return 0

def get_pressure(json, n, t):
	if 0<= n <= 4:
		today = datetime.date.today()
		required_date = today+datetime.timedelta(n)
		index_find = str(required_date)+" "+str(t)
		data_of_required_date= json.find(index_find)
		ps = json.find("pressure",data_of_required_date-350)
		ps_a = json.find(",",ps)
		ps_b = json[ps+10 : ps_a]
		return float(ps_b)
	else:
		return 0

def get_wind(json, n, t):
	if 0<= n <= 4:
		today = datetime.date.today()
		required_date = today+datetime.timedelta(n)
		index_find = str(required_date)+" "+str(t)
		data_of_required_date= json.find(index_find)
		wd = json.find("wind",data_of_required_date-350)
		wd_a = json.find(",",wd)
		wd_b = json[wd+15 : wd_a]
		return float(wd_b)
	else:
		return 0

def get_sealevel(json, n, t):
	if 0<= n <= 4:
		today = datetime.date.today()
		required_date = today+datetime.timedelta(n)
		index_find = str(required_date)+" "+str(t)
		data_of_required_date= json.find(index_find)
		sl = json.find("sea_level",data_of_required_date-350)
		sl_a = json.find(",",sl)
		sl_b = json[sl+11 : sl_a]
		return float(sl_b)
	else:
		return 0
if __name__=="__main__":
	k = input()
	a = weather_response(k,"2ab136be1543b5789451a5994364c0d3")
	print("Temp of "+str(k)+"="+str(get_temperature(a,0,"15:00:00"))+" K")
	print("humidity of "+str(k)+"="+str(get_humidity(a,0,"15:00:00")))
	print("pressure of "+str(k)+"="+str(get_pressure(a,0,"15:00:00"))+" mm of Hg")
	print("Wind speed of "+str(k)+"="+str(get_wind(a,0,"15:00:00"))+" kmph")
	print("Sea level of "+str(k)+"="+str(get_sealevel(a,0,"15:00:00"))+" feet")
#Aayush Gupta
#2017125