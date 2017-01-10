from elastic import delete_index
import datetime


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

def log(file_name, message):
    f = open('logs/' + file_name + '.log', 'a', 0)
    time = datetime.datetime.now().strftime("%H:%M:%S")
    msg = '['+time+'] '+message+'\n'
    f.write(msg)
    
    
def clear():
    file_name = "clean-" + str(datetime.date.today())
    delete_date = datetime.date.today() - datetime.timedelta(days=4)
    for product in products:
        for catalogue in products[product]:
            index = 'dmp-'+product+'-'+catalogue+'-'+str(delete_date)
            log(file_name, 'delte index ['+index+']')
            delete_index(host, index)

              
clear()
