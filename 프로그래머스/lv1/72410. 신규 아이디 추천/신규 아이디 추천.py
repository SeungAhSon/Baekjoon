import re
def solution(new_id):
    new_id = new_id.lower()

    A = re.compile('[0-9a-z_.\-]+')
    new_id = A.findall(new_id)
    new_id = ''.join(new_id)

    new_id = re.sub('\.\.+','.',new_id)
    
    while ".." in new_id:
        new_id.replace("..",".")
            
    
    new_id = new_id.strip('.')
    
    if new_id=="": new_id = "a"
    
    if len(new_id)>=16 :
        new_id = new_id[:15].rstrip('.')
    
    if len(new_id)<=2:
        new_id += new_id[-1]*(3-len(new_id))

    return new_id