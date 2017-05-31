# This class was generated on Wed, 31 May 2017 14:25:30 PDT by version 0.01 of Braintree SDK Generator
# event_list.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.list","Description":"Lists webhook event notifications. Use query parameters to filter the response.","Parameters":[{"Type":"string","VariableName":"end_time","Description":"Filters the webhook event notifications in the response to those created on or after the `start_time` and on or before this date and time. Both values are in [RFC 3339 Section 5.6](http://tools.ietf.org/html/rfc3339#section-5.6) format. Example: `end_time=2013-03-06T11:00:00Z`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"event_type","Description":"Filters the response to a single event.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"integer","VariableName":"page_size","Description":"The number of webhook event notifications to return in the response.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"start_time","Description":"Filters the webhook event notifications in the response to those created on or after this date and time and on or before the `end_time` value. Both values are in [RFC 3339 Section 5.6](http://tools.ietf.org/html/rfc3339#section-5.6) format. Example: `start_time=2013-03-06T11:00:00Z`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"transaction_id","Description":"Filters the response to a single transaction, by ID.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"SuccessResponseType":{"Type":"EventList","VariableName":"","Description":"List of webhooks events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks-events","Visible":true}

import requests

class EventListRequest (requests.Request):
    """
    Lists webhook event notifications. Use query parameters to filter the response.
    """

    def __init__(self):
        super(EventListRequest, self).__init__(method="GET", url="/v1/notifications/webhooks-events")

    

    def endTime(self, endTime):
        self.url += self.url + "end_time=" + str(endTime) + "&"
        return self

    def eventType(self, eventType):
        self.url += self.url + "event_type=" + str(eventType) + "&"
        return self

    def pageSize(self, pageSize):
        self.url += self.url + "page_size=" + str(pageSize) + "&"
        return self

    def startTime(self, startTime):
        self.url += self.url + "start_time=" + str(startTime) + "&"
        return self

    def transactionId(self, transactionId):
        self.url += self.url + "transaction_id=" + str(transactionId) + "&"
        return self
    
