from elastic import ask_delete_index, get_indices, parse_indices


host = "localhost:9200"
products = {                                \
    'glads2_mm' : ['dev', 'test', 'prod'],  \
    'glads2_vk' : ['dev', 'test', 'prod'],  \
    'glads2_ok' : ['dev', 'test', 'prod'],  \
    'glads2_gp' : ['dev', 'test', 'prod'],  \
    'glads2_fb' : ['dev', 'test', 'prod'],  \
    'glads2_win' : ['dev', 'test', 'prod'], \
    'glads2_ios' : ['dev', 'test', 'prod'], \
    'glads2_ndr' : ['dev', 'test', 'prod']  \
}


def clear():
    inds = get_indices(host)
    parsed = None
    if inds != None:
        parsed = parse_indices(inds)
    if parsed != None:
        for line in parsed:
            if len(line) >=8:
                splt = line[2].split('-')
                
                if len(splt)>3 and splt[1] in products and splt[5] == '03':
                    #print line[2], line[7]
                    ask_delete_index(host, line[2])

              
clear()
