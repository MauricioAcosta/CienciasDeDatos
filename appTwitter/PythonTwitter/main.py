import twitter
import pandas as pd
import numpy as np

api = twitter.Api(consumer_key='CGMxmM2ubhETj39Q8MVwlC8uJ',
                  consumer_secret='xYswZsui2RTEXHcGmDCZgkkunaezFcjNsu24gPt3FvXXorwzA2',
                  access_token_key='1138117225871814656-j8JK4ak8ahUeOR5Srf81YtNzv8hKXg',
                  access_token_secret='b87o7mB38h7qWczZhVwcUEGRkqjhzP6L3tw07njzzeo8O')


def search_tweets():
    ## Tweets that contain the word 'twitter'
    #results = api.GetSearch(
           # raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
    ## Tweets that contain the word 'science'
    results2 = api.GetSearch(
            raw_query="l=en&q=science%20&result_type=recent&esince%3A2019-06-15&count=10")
    print(type(results2))
    return results2 

def fromList_toDf(lista):
    dfObj=pd.DataFrame(lista)
    print("dfObj: ")
    print(dfObj.head())
    #print (len(lista))
    return dfObj

##################################################################################
#
# Lógica principal de procesamiento
# Objetivo: Traer tweets, almacenarlos en Dataframes y analizarlos
# Autor: Leidy Marcela Aldana 
#
##################################################################################

resultados=search_tweets()
#print("resultados[0]=",resultados[0])
#print("resultados[1]=",resultados[1])
datafram=fromList_toDf(resultados)
print("Dataframa")
print(datafram.columns)

