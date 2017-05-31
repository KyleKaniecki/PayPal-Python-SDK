# PayPal SDK 2.0.0-alpha

This is a preview of how PayPal SDKs will look in the next major version. We've simplified the interface to only provide
simple model objects and blueprints for HTTP calls. This repo currently only contains functionality for working with webhooks
to serve as an example of the API going forward.

### Getting a list of webook events

```python
import paypal_sdk
import paypal_core

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
```

*NOTE*: This API is still in alpha, is subject to change, and should not be used in production.
