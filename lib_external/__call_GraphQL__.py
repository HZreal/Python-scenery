import graphene
# 针对 Graph（图状数据）进行查询
# GraphQL 是一种用于 API 的查询语言，也是一种服务器端运行时，用于使用您为数据定义的类型系统执行查询。GraphQL 不依赖于任何特定的数据库或存储引擎，而是由您现有的代码和数据支持。
# https://graphql.org/
# 对应python的api如包graphene，当然还有很多其他的



class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])            # "Hello World"


