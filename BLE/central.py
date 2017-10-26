from gattlib import GATTRequester, GATTResponse

address = "B8:27:EB:AC:B8:68"
request = GATTRequester(address)

data = request.read_by_handle(0x000c)

d =  data[0].encode('hex')
temp, humid = map(lambda x: int(x, 16), (d[0:2], d[2:]))
print 'Temperature is %d °C, Humidity is %d \%' % (temp, humid)

