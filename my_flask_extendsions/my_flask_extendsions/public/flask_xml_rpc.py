"""url:https://pythonhosted.org/Flask-XML-RPC/
Of course, the register_function() method can take a name if you want to use 
dotted names, but it’s easier to use namespaces. 
You get a namespace by calling the namespace() method with the prefix you want (without the dot).
"""
from flask_xmlrpc import XMLRPCHandler, Fault
handler = XMLRPCHandler('api')
handler.connect(app, '/api')

@handler.register
def hello(name="world"):
    if not name:
        raise Fault("unknown_recipient", "I need someone to greet!")
    return "Hello, %s!" % name


blog = handler.namespace('blog')

@blog.register
def add_post(title, text):
    # do whatever...
    pass



"""

Testing Your API
The easiest way to test your application is with the XMLRPCTester. It takes a werkzeug.TestClient and the path to your responder. When called with the method and params, it will marshal it, make a fake POST request to the responder with the client, and demarshal the result for you, returning it or a Fault.

If you’re using a unittest-based setup like the one described in the Flask documentation, you could use the XMLRPCTester like:

"""

def test_hello(self):
    tester = XMLRPCTester(self.app, '/api')
    assert tester('hello') == 'Hello, world!'
    assert tester('hello', 'Steve') == 'Hello, Steve!'
    fault = tester('hello', '')
    assert fault.faultCode == 'unknown_recipient'



"""

Using Your API
Practically all programming languages can use XML-RPC. In Python, you can call XML-RPC methods with the standard library xmlrpclib module.


:import xmlrpclib
:server = xmlrpclib.ServerProxy('http://localhost:5000/')
:server.hello()
:server.hello('Steve')

"""
