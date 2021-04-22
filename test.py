from piplapis.data import Person, Name, Address, Job, DOB, DateRange
from piplapis.search import SearchAPIRequest
from piplapis.search import SearchAPIError
import json
import datetime

# Test for DOB parsing. The DOB provided below does not appear in the "parsed data" in the pipl API console query view
# I believe therefore it is not being included in the filtering logic, and there are too many returned responses

# Please change the name and DOB range below to something useful for your tests. 

fields = [Name(first=u'Clark',  last=u'Kent'),
          DOB(date_range=DateRange(datetime.date(1970,1,1),datetime.date(1980,1,1)))]
request = SearchAPIRequest(person=Person(fields=fields), api_key='YOURS_HERE')

try:
    response = request.send()
except SearchAPIError as e:
    print(e.http_status_code, e)
    exit(1)

exit(0)
