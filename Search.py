import requests
import json
from dotenv import load_dotenv
import os
from favorite import favoritar 

load_dotenv('/storage/emulated/0/anime_search/.env')
    






class Animemanager():
   #chama as apis
    def __init__(self,caller):
       
        self.caller = caller    
        self.caller = input("digite o Anime procurado:")
       
        
        chamador = requests.get(f'https://api.jikan.moe/v4/anime?q={self.caller}').json()
        movie_api_key = os.environ['chavewatchmode']
        movie_caller = requests.get(f'https://api.watchmode.com/v1/search/?{movie_api_key}/name/Breaking').json()
        
        print(movie_caller)
        print(self.caller)
        
        self.Anime = self.caller
        self.caller = chamador
        
        
        
    def return_Anime(self):
        
        return self.Anime
        return self.caller
        
    def show_details(self):
        show = input('quer ver os detalhes?')
        if show == "Sim":
            print(f"Details list ====>",self.caller['data'][0])
            
            
            
            what_details = input("quais detalhes?")
            
            
            
            print(self.caller['data'][0][what_details])
    def create_base(self,base):
       
       
       if not os.path.exists('/storage/emulated/0/anime_search/historico.json'):
                
                with open("historico.json",'w') as cp:
                        
                        pass
        
        
       
       with open("historico.json","r") as arq:
          
           
                    
          larp = len(arq.readlines())
    ##criar estrutura base de json com array apartir daqu
                
          if larp ==0:

                        
               

               with open("historico.json","w") as arquivo:
                  
                           
                  print("open")
                  json.dump(base,arquivo,indent =4)
       return
    def add_anime(self):
        print(self.Anime)
        with open('historico.json','r') as arqh:
            
            
            reader = json.load(arqh)
            print(f"==>{reader['animes']}")
            if not self.Anime in reader['animes']:
                
                reader['animes'].append(self.Anime)
            else:
                print("já tem lá")
            print(reader)
            
            with open("historico.json","w") as hist:
                json.dump(reader,hist,indent = 4)
            
    def create_base_fav(self,base):
       
       if not os.path.exists('/storage/emulated/0/anime_search/favoritos.json'):
                
                with open("favoritos.json",'w') as arq:
                        
                        pass
        
        
       
       with open("favoritos.json","r") as arq:
          
           
                    
          larp = len(arq.readlines())
    ##criar estrutura base de json com array apartir daqu
                
          if larp ==0:

                        
               

               with open("favoritos.json","w") as arquivo:
                  
                           
                  print("open")
                  json.dump(base,arquivo,indent =4)
       return
       
    def add_to_favlist(self):
       
       the_chosed = input("digite quem vc quer favoritar")
       with open("favoritos.json","r") as arq:
           reader = json.load(arq)
           if  not the_chosed in reader['favoritos']:
               reader['favoritos'].append(the_chosed)
           else:
               print("Anime ja favoritado")
               
           with open("favoritos.json","w") as arq2:
               json.dump(reader,arq2,indent =4)
               return
       


            
            
            
        
        
def question():
    yesorno = input("quer favoritar algo(Sim ou não):")
    if yesorno == "Sim":
        
       umb.add_to_favlist()
    else:
        yesorno = input("tem certeza?")
        if yesorno.upper() == "SIM" or yesorno.upper() =="YES" :
            return
        else:
            question()

#chamadas



vasco ={
        "animes": [
        
        ]
        }
fav = {
 "favoritos":[
 
 ]
 }
umb = Animemanager("yes")
umb.show_details()
umb.create_base(vasco)
umb.add_anime()
umb.create_base_fav(fav)
question()


#pegar o anime e salvar no Json
#expandir o projeto