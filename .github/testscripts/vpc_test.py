import constellation_vpc as vpc

testsubnet = vpc.VPC(region="us-west-2", vpc_id="vpc-08ed1a1cd357c0dab", aws_session_token="IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIFS07HBOKb71UbXactPaJIECu8EWweC4TXQ9CB/VvlLoAiA7AmXozlLm/5/vdHZ6MALEd+KDHjN7wsmo95q5wjlKeSqUAghQEAMaDDE2MzAxNDIxNDgwOSIMgSt4aN7LsjI1zqbeKvEBILUxzEXecGEF8JQm7BKybdXk/ZWh+Krmqsgaa6u1HCT+0LP7SGp1XngnnsOLCp+X5SFAHtkusbQ5KnOqhaxXtuUu8jlMk2FlYqj56d+Bcckcw8NFm+0I6E83YfNieWf1KrS7xB8S9ZhUf71HVjYPV4O2XBkiR+UUaSyyl/rORnKk4mfe1eEXRr89AjkAeGQJiBx2lQ4aeW6YvUSAKmIipSM0H4a7txiynuhCS45AeA/gQzk3mwIPar0Qj0Ow9Jg/jT6g/ID0DdTAenkFJCBfQRX+UUncIg8weTDXE+PX06Qx89h5UznZ6PYN+DmSPUaWtjC0vtq1BjqeAbFzqteoY/U9ByULcxsPALgrQPLOcHbqezuBommZ0ZNEdAFRiDOO3Up0H0yfzvzF32bI4Il0fkegoWo0priD4km+0BWoQFIv0AHtGVEyqGY4YR8zxPP69oJ79tM8XSkU3jnwuwINpHZy1x3nZTxynm0zk86MtQMpM1+o1B3oHIJDpa47MjPg9YbGZwtVrIfQA7KyiqmIMsVXMLw3d9l4")
for x in testsubnet.subnets:
    print(x)

