from neo4j import GraphDatabase


driver = GraphDatabase.driver(uri='bolt://127.0.0.1:7687', auth=('neo4j', '123456'))

with driver.session() as session:
    result = session.run('MATCH (o:Order)-[rel:CONTAINS]->(p:Product) RETURN o, rel, p LIMIT 5;')
    all_data = result.data()
    print(all_data, type(all_data))
    # record = result.single()
    # print('hash----', hash(record))
    # print('record_data-----', record.data())
    # remain_data = result.data()
    # print(remain_data)

def parse_all_data(all_data):
    for item in all_data:
        # print('-----item-----', item)
        # for key, value in item.items():
        #     print('key--------->', key)
        #     print('value--------->', value)


        o = item.get('o')
        print('o------------', o)  # 字典

        rel = item.get('rel')
        print('rel------------', rel)         # 三元元祖, rel[0]和rel[2]是点   rel[1]是关系 'CONTAINS'
        # for i in rel:
        #     print('------rel内元素---------', i)

        p = item.get('p')
        print('p------------', p)  # 字典

        print('#######################################################################\n')


parse_all_data(all_data)


driver.close()




