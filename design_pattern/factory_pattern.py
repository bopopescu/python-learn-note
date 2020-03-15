class HttpMethod(object):
    def method(self):
        return NotImplemented("method must be implemented")


class GetHttpMethod(HttpMethod):
    def __init__(self):
        print('http get method')

    def method(self):
        print('Inside Get:method() method')


class PostHttpMethod(HttpMethod):
    def __init__(self):
        print('http post method')

    def method(self):
        print('Inside Post:method() method')


class PutHttpMethod(HttpMethod):
    def __init__(self):
        print('http put method')

    def method(self):
        print('Inside Put:method() method')


class HttpMethodFactory(object):

    @classmethod
    def get_http_method(cls, method):
        if method.lower() == 'get':
            return GetHttpMethod()
        if method.lower() == 'post':
            return PostHttpMethod()
        if method.lower() == 'put':
            return PutHttpMethod()


if __name__ == '__main__':
    method_factory = HttpMethodFactory()
    method_get = method_factory.getHttpmethod('get')
    method_put = method_factory.getHttpmethod('put')
    method_post = method_factory.getHttpmethod('post')
    method_get.method()
    method_put.method()
    method_post.method()
