from neo4j import GraphDatabase

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "rootroot"))

def get_results(tx):
    query = "match(n:City)-[t:TWINNED_WITH]-(n1:City) return n.name, n1.name order by n.name"
    names = []
    names2 = []
    results = tx.run(query)
    for x in results:
        names.append(x['n.name'])
        names2.append(x['n1.name'])
    x=0
    final=[]
    while x < len(names):
        final.append(names[x] + " <-> " + names2[x])
        x=x+1
    return final

def main():
    connect()
    with driver.session() as session:
        final = session.read_transaction(get_results)
        for x in final:
            print(x)
        #print(final)

if __name__ == "__main__":
    main()
