from neo4j import GraphDatabase

URI = 'bolt://127.0.0.1:7687'
USERNAME = 'neo4j'
PASSWORD = '123456'


class Neo4jConnection():
    def __init__(self, uri=None, username=None, password=None):
        self.uri = uri or URI
        self.username = username or USERNAME
        self.password = password or PASSWORD
        self.driver = GraphDatabase.driver(uri=self.uri, auth=(self.username, self.password))

    def run_cypher(self, cypher, params=None):
        if not params:
            params = {}
        with self.driver.session() as session:
            result = session.run(cypher, **params)
        return result.data()


def close(self):
    self.driver.close()


if __name__ == '__main__':
    config = {
        'uri': 'bolt://127.0.0.1:7687',
        'username': 'neo4j',
        'password': '123456',
    }
    cypher = '''MATCH (o:Order)-[rel:CONTAINS]->(p:Product) RETURN o, rel, p LIMIT 5;'''

    conn = Neo4jConnection(**config)
    data = conn.run_cypher(cypher)
    print(data)

    conn.close()
