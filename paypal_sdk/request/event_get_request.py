# This class was generated on Wed, 31 May 2017 14:25:30 PDT by version 0.01 of Braintree SDK Generator
# event_get.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.get","Description":"Shows details for a webhook event notification, by ID.","Parameters":[{"Type":"string","VariableName":"event_id","Description":"The ID of the webhook event notification for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"SuccessResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks-events/{event_id}","Visible":true}

import requests

class EventGetRequest (requests.Request):
    """
    Shows details for a webhook event notification, by ID.
    """

    def __init__(self):
        super(EventGetRequest, self).__init__(method="GET", url="/v1/notifications/webhooks-events/{event_id}")

    

    def eventId(self, eventId):
        self.url = self.url.replace("{event_id}", str(eventId))
        return self
    
