f = "IP_Trace.tr"

tra_t = {}
rec_t = {}
d= {}


def get_details(line):
    parts = line.split()
    
    if "Payload" in parts:
        
        if parts[0] != 'd':
            m = int(parts[2][10:-27]) 
        #print m
            n = int(parts[23][7:])
            l= int(parts[25][7:-1]) 
            i_d= int(parts[13])
            
            
            
            key= str(n)+'.'+ str(l) +'.'+str(i_d) 
            
            if parts[0] == 't':
        	   if m==n-1:
        		  tra_t.update({key:parts[1]})
                
            #print tra_t
            if parts[0]== 'r':
        	   if m==l-1:
                    rec_t.update({key:parts[1]}) 
        		
    #print rec_t
  
    


with open(f) as data:
    
    while True:
        line = data.readline()
        if not line:
            break
        get_details(line)
for k1 in rec_t:
    for k2 in tra_t:
        if k1 == k2:
            d.update({k1: float(rec_t[k1])-float(tra_t[k1])})



maximum = max(d, key=d.get)  # Just use 'min' instead of 'max' for minimum.
print("Maximum Delay is:", d[maximum])
#minimum = min(d, key=d.get)
#print(minimum, d[minimum])
count = 0
_sum = 0
for key in d:
    count += 1
    _sum += d[key]

print('The Average Delay is:', _sum/count)
        #use_data()
#print tra_t
#print rec_t
#print d

#def use_data():
 #   pass

