import elastic

host = "localhost:9200"
index = "dmp-glads2_mm"
#test1(host, "dmp-glads2_mm-prod-2016-10-30")
#delete_index(host, "dmp-glads2_mm-prod-2016-11-02")

inds = elastic.get_indices(host)
parsed = None
if inds != None:
    parsed = elastic.parse_indices(inds)
print len(parsed)
i = 0
s = 0
q = 0
if parsed != None:
    for line in parsed:
        if len(line) >=8:
            splt = line[2].split('-')
            #print i, line[2], preaty_num(int(line[7]))
            #if len(splt)>2 and (splt[1]=='glads2_mm' or splt[1]=='glads2_gp' or splt[1]=='glads2_vk' or splt[1]=='glads2_ok'):
            if len(splt)>2 and splt[2]=='srv_dev':
                print i, line[2], elastic.preaty_num(int(line[7]))
                s += int(line[7])
                q += 1
                #elastic.delete_index(host, line[2])
        i += 1
print 'count', elastic.preaty_num(q), 'sum', elastic.preaty_num(s)
                
