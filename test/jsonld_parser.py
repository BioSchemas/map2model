from rdflib import ConjunctiveGraph

def __get_class_name(temp_uri):
    return temp_uri.replace("http://schema.org/","")

def __add_property(props_dic, prop_desc):
    if prop_desc['prop_name'] in props_dic:
        t_prop_name = prop_desc['prop_name']
        props_dic[t_prop_name]['exp_type'].append(prop_desc['exp_type'])
    else:
        props_dic[prop_desc['prop_name']]=prop_desc
        props_dic[prop_desc['prop_name']]['exp_type'] = [prop_desc['exp_type']]
    return props_dic

def __get_class_props(class_name, graph):

    qres = graph.query("""prefix schema: <http://schema.org/>
                        select distinct * where { 
                            ?property schema:domainIncludes  schema:%s .
                            ?property schema:rangeIncludes  ?exp_type .
                            ?property rdfs:label ?prop_name.
                            ?property rdfs:comment ?description
                        }""" % class_name)
    temp_dic = {}
    for row in qres:
        labels=row.labels.keys()
        labels_dic = {}
        for label in labels:
            labels_dic[label] = str(row[label])
        temp_dic=__add_property(temp_dic, labels_dic)

    return temp_dic

def __get_parent_type(class_name, graph):

    qres = graph.query("""prefix schema: <http://schema.org/>
                          select ?supclass where{
                          ?class rdfs:label ?label .
                          ?class rdfs:subClassOf ?supclass .
                          filter (?label='%s')
                        }""" % class_name)
    resp_arr=[]

    for row in qres:
        resp_arr.append(str(row['supclass']))
    return resp_arr[0].replace('http://schema.org/', '')

def __get_properties(class_name, graph, properties):

    if(class_name=='Thing'):
        properties[class_name]=__get_class_props(class_name, graph)
        return properties
    else:
        temp_props = __get_class_props(class_name, graph)
        properties[class_name] = temp_props
        parent_type = __get_parent_type(class_name, graph)
        __get_properties(parent_type, graph, properties)




query_type="CreativeWork"
g = ConjunctiveGraph()
g.parse('http://schema.org/version/latest/schema.jsonld', format='json-ld')
props_dic={}
__get_properties(query_type, g, props_dic)
print(props_dic)













