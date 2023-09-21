
a = 'world'

b = 'hello %s' % a
c = f'hello {a}'
d = 'hello {}'.format(a)
e = 'hello {a}'.format(a=a)
f = 'hello---->%(aaa)s' % {'aaa': a}     # %(aaa)s 中的aaa的值映射到a

print(b, c, d, e, f, sep='\n')






