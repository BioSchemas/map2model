from rdflib import ConjunctiveGraph

g = ConjunctiveGraph()

result = g.parse('http://schema.org/version/latest/schema.jsonld', format='json-ld')


qres = g.query("""prefix schema: <http://schema.org/>
                    select distinct * where { 
                        ?property schema:domainIncludes  schema:SoftwareApplication .
                        ?property schema:rangeIncludes  ?range .
                        ?property rdfs:label ?label .
                        ?property rdfs:comment ?description
                    }""")
temp_dic = {}
for row in qres:
    labels=row.labels.keys()
    labels_dic = {}
    for label in labels:
        labels_dic[label] = row[label]

    temp_dic.
print(temp_dic)










