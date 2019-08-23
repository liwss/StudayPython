# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/12/4 15:49
# @describe : 


from tornado import gen
import tornado.httpclient
import tornado.ioloop
import tornado.concurrent
import certifi


@gen.coroutine
def call_server():
    tornado.httpclient.AsyncHTTPClient().configure(None, defaults=dict(ca_certs=certifi.old_where()))
    http_client = tornado.httpclient.AsyncHTTPClient()
    url = 'https://testapi.taxrating.net/Services/V02/SureTax.asmx/PostRequest'
    body = """request=<?xml version="1.0" encoding="UTF-8"?><Request xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><ClientNumber>000000911</ClientNumber> <BusinessUnit></BusinessUnit> <ValidationKey>f35fcde8-d112-4192-b4ba-86169bfe887a</ValidationKey> <DataYear>2019</DataYear> <DataMonth>07</DataMonth> <TotalRevenue>25.25</TotalRevenue> <ReturnFileCode>0</ReturnFileCode> <ClientTracking>PORTAL001</ClientTracking> <IndustryExemption></IndustryExemption> <ResponseGroup>03</ResponseGroup> <ResponseType>D2</ResponseType> <ItemList> <Item> <LineNumber>USCAZ1000009</LineNumber> <InvoiceNumber></InvoiceNumber> <CustomerNumber>000000911</CustomerNumber> <OrigNumber></OrigNumber> <TermNumber></TermNumber> <BillToNumber></BillToNumber> <Zipcode>19107</Zipcode> <Plus4>0000</Plus4> <P2PZipcode></P2PZipcode> <P2PPlus4></P2PPlus4> <TransDate>07/28/2019</TransDate> <Revenue>25.25</Revenue> <Units>1</Units> <UnitType>00</UnitType> <Seconds>1</Seconds> <TaxIncludedCode>1</TaxIncludedCode> <TaxSitusRule>04</TaxSitusRule> <TransTypeCode>500002</TransTypeCode> <SalesTypeCode>R</SalesTypeCode> <RegulatoryCode>05</RegulatoryCode> <TaxExemptionCodeList> <string>00</string></TaxExemptionCodeList></Item></ItemList></Request>"""
    response = yield http_client.fetch(request=url, method='POST', body=body)
    print response.body                           # python2+使用
    # print(str(response.body, encoding='utf-8'))     # python3+使用


# async def call_server1():
#     """python3.5新增关键字async和await，等价于gen的装饰器写法，也被称为原生协程"""
#     http_client = tornado.httpclient.AsyncHTTPClient()
#     response = await http_client.fetch(request='http://127.0.0.1:8000/index', method='POST', body='test')
#     print(str(response.body, encoding='utf-8'))     # python3+使用


if __name__ == '__main__':
    tornado.ioloop.IOLoop.instance().run_sync(call_server)
