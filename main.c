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

Hi feng,

Could you read the source code at first? You haven't init a object useing a class,Why not make a
change? Thanks.

BRs
Wufeng
i m p o r t   o s , s y s , c o m m a n d s  
  
 c l a s s   P e r s o n ( o b j e c t ) :  
 	 d e f   _ i n i t _ ( s e l f , n a m e ) :  
 	 	 s e l f . n a m e = n a m e  
 	 d e f   s a y h e l l o ( s e l f ) :  
 	 	 p r i n t   ' M y   n a m e   i s : ' , s e l f . n a m e  
 i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' :  
 	 a p p   =   P e r s o n ( ) ;  
 	 a p p . _ i n i t _ ( ' b i l l ' ) ;  
 	 a p p . s a y h e l l o ( ) ;  
 