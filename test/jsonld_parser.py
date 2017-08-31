from rdflib import ConjunctiveGraph

g = ConjunctiveGraph()

result = g.parse('http://schema.org/version/latest/schema.jsonld', format='json-ld')


qres = g.query("""prefix schema: <http://schema.org/>
                    select distinct * where { 
                        ?property schema:domainIncludes  schema:SoftwareApplication .
                        ?property schema:rangeIncludes  ?range .
                        ?property rdfs:label ?label .
                    } order by ?property """)

for row in qres:
    print(row)










