Q1: hello,can you help me ?
sure
But,what is your question?


Q2：

class Person(object):
        def _init_(self,name):
            self.name=name
        def sayhello(self):
            print 'My name is:',self.name
if __name__ == '__main__':   
    c=Person("bill")
    print c
	
	
	
	 c=Person("bill")这句错误，但是
	我要调用类里面的sayhello（）函数，怎么把name这个参数传进去。
	
	 c=Person()
    print c.sayhello（"bill"）  这样子也不行