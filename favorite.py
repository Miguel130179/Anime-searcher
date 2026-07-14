def favoritar():
   if not os.path.exists('/storage/emulated/0/anime_search/favoritos.json'):
    with open('favoritos.json','w') as archive:
        print("2")
        
   with open('historico.json','r')as arq:
           
        
        
        
       
           desempacotado = json.load(arq)
           print(desempacotado)
        
        
           lista = []
        
            
           chosen = input("digite um anime para favoritar:")
       
        
           if chosen in desempacotado['animes']:
                   
             
           
        
           
           #o erro tem como base a linha 66
                   lista.append(chosen)
           
                   dict1 ={
           
                   "title":lista
                   }
                   larg =0
                   with open("favoritos.json","r") as readf:
                           
                  
                           larg = len(readf.readlines())
                           if larg ==0:
                                   
                      
                                   basic_structure ={
                                   "lista":[]
                                   }
                   
                                   with open("favoritos.json","w") as readfav:
                                           
                          
                                           json.dump(basic_structure,readfav,indent =4)
                   with open("favoritos.json","r") as favorite:
                           
                  
                           mia= json.load(favorite)
                           mia['lista'].append(chosen)
                           with open("favoritos.json","w") as fav:
                                   
                      
                                   json.dump(mia,fav,indent =4)
                
                
                
                
                
           else:
                  
                  print("erro")
           
           
       
            
            
            