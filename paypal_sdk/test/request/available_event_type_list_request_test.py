# This class was generated on Wed, 31 May 2017 14:25:30 PDT by version 0.01 of Braintree SDK Generator
# available_event_type_list.py
# DO NOT EDIT
# @type request
# @json {"Name":"available-event-type.list","Description":"Lists available events to which any webhook can subscribe. For a list of supported events, see [Webhook event names](/docs/integration/direct/webhooks/event-names/).","Parameters":[],"RequestType":null,"SuccessResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks-event-types","Visible":true}

import unittest
import paypal_sdk
import paypal_core

class AvailableEventTypeListRequestTest(unittest.TestCase):

    def testAvailableEventTypeListRequest(self):
        environment = paypal_core.PayPalEnvironment("AYSq3RDGsmBLJE-otTkBtM-jBRd1TCQwFf9RGfwddNXWz0uFU9ztymylOhRS",
                                                    "EGnHDxD_qRPdaLdZz8iCr8N7_MzF-YHPTkjs6NKYQvQSBngp4PTTVWkPZRbL",
                                                    paypal_core.PayPalEnvironment.SANDBOX)
        client = paypal_core.PayPalHttpClient(environment)
        request = paypal_sdk.AvailableEventTypeListRequest()
        try:
            response = client.execute(request)
        except IOError as ioe:
            if ioe.headers:
                print ioe.headers["paypal-debug-id"]
            else:
                print ioe

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.result.event_types), 1)


if __name__ == "__main__":
    unittest.main()
