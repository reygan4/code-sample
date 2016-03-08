letter = '0abcdefghijklmnopqrstuvwxz'
n = int(input()) 
center = letter[n]
left = ''
for i in xrange(n,0,-1):
    
    print '-' * ((i*2)-2) +  center +left+'-'  * ((i*2)-2)
   # print center[::-1]
    
    center += '-'+letter[i-1] 
    left = '-' + letter[i] + left
   # print center, lef
center = center[0:2*n-1]

for i in range(2,n+1):
   
    center = center[0:2*n-(2*i-1)]
 #   print center
  #  print center[-i::-1]
    print '-' * ((i*2)-2) +  center +center[-2::-1]+'-'  * ((i*2)-2)
    
