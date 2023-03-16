import time
def start_time():   
    a=str(time.ctime()).split()
    data=''
    data=data+a[0]+' '
    mon=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if mon.index(a[1])+1>=10:
        data=data+a[2]+'.'+str(mon.index(a[1])+1)+'.'
    else:
        data=data+a[2]+'.0'+str(mon.index(a[1])+1)+'.'
    data+=a[4]
    return data
    