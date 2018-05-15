# coding=utf-8


import xml.dom.minidom


def parseXML(strbuf):
    dom = xml.dom.minidom.parseString(strbuf)
    soap = dom.documentElement
    value = []
    for i in ['SUCCESS', 'ERROR_MESSAGE']:
        itemlist = soap.getElementsByTagName(i)
        item = itemlist[0]
        value.append(item.firstChild.data)
    return """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header/>
  <soap:Body>
    <MOD_CATEGORYResponse xmlns="http://www.chinamobile.com/HSS/">
      <Result>
        <ResultCode>%s</ResultCode>
        <ResultDesc>%s</ResultDesc>
        <ResultData/>
      </Result>
    </MOD_CATEGORYResponse>
  </soap:Body>
</soap:Envelope>""" % (value[0], value[1])


if __name__ == "__main__":
    xml_str = """
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    	<soap:Body>
    		<ns2:checkBusiStateResponse xmlns:ns2="http://ws.webservices.friendone.com/">
    			<return xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xs="http://www.w3.org/2001/XMLSchema" xsi:type="xs:string">
    				<ROOT>
    					<SUCCESS>0</SUCCESS>
    					<RESULT>不存在</RESULT>
    					<ERROR_MESSAGE>统谈标签可能为空，或统谈标签数据有误</ERROR_MESSAGE>
    				</ROOT>
    			</return>
    		</ns2:checkBusiStateResponse>
    	</soap:Body>
    </soap:Envelope>
    """
    print parseXML(xml_str)




