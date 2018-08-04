from lxml import etree

# 生成tree对象
tree = etree.parse('xpath.html')
print(tree)
#<lxml.etree._ElementTree object at 0x000000000252B388>

ret = tree.xpath('//div[@class="hero"]/text()')
"""
扩展:
        def xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables): # real signature unknown; restored from __doc__
        
        xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)
        
                XPath evaluate in context of document.
        
                ``namespaces`` is an optional dictionary with prefix to namespace URI
                mappings, used by XPath.  ``extensions`` defines additional extension
                functions.
        
                Returns a list (nodeset), or bool, float or string.
        
                In case of a list result, return Element for element nodes,
                string for text and attribute values.
        
                Note: if you are going to apply multiple XPath expressions
                against the same document, it is more efficient to use
                XPathEvaluator directly.
        
        pass
"""
ret_1 = tree.xpath('//div[@class="hero"]//text()')
# print(ret_1)
# string = ''.join(ret).replace('\t','').replace('\n','')
# print(ret)
# print(string)