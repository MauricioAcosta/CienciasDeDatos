import matplotlib
matplotlib.use("Agg")
from django.shortcuts import render
from django.http import HttpResponse
from .models import Hashtags, Usuarios, Candidatos
import pandas as pd
import numpy as np
import tweepy
import json
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Create your views here.

def autenticacion():
    consumer_key = 'CGMxmM2ubhETj39Q8MVwlC8uJ'
    consumer_secret = 'xYswZsui2RTEXHcGmDCZgkkunaezFcjNsu24gPt3FvXXorwzA2'
    access_token = '1138117225871814656-j8JK4ak8ahUeOR5Srf81YtNzv8hKXg'
    access_token_secret = 'b87o7mB38h7qWczZhVwcUEGRkqjhzP6L3tw07njzzeo8O'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api

def home(request):
    return render(request, 'analiticas/index.html', context=None)

def analitica1(request):
    usuarios = Usuarios.objects.all()
    hashtags = Hashtags.objects.all()
    api = autenticacion()

    context = {
        'usuarios': usuarios,
        'hashtags': hashtags,
    }

    if request.method == 'POST':

        usuario = request.POST.get('usuario')
        hashtag = request.POST.get('hashtag')

        if usuario == 'Escoja uno' and hashtag=='Escoja uno':
            list_of_tweets = []
            for i in usuarios:
                for j in hashtags:
                    consul = tweepy.Cursor(api.search, q='from:'+str(i.arroba)+' '+str(j.hashtag)).items()
                    for tweet in consul:
                        dict_ = {'User': tweet.user.name,
                                'User_Name': tweet.user.screen_name,
                                'Text': tweet.text,
                                'Hashtag': j.hashtag
                                }
                        list_of_tweets.append(dict_)

            df1 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Text', 'Hashtag'])
            # plot data
            fig, ax = plt.subplots(figsize=(15,7))
            # use unstack()
            dff = df1.groupby(['User'])['Hashtag'].value_counts().unstack()
            dff.fillna(0, inplace=True)
            dff.plot(ax=ax).ylabel('Cantidad de hashtags')


            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=300)
            image_base641 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            context.update({'image_base641':image_base641})

            # plot data SCATTER
            fig, ax = plt.subplots(figsize=(15,7))
            # use unstack()
            dff = df1.groupby(['User'])['Hashtag'].value_counts()
            dff = dff.reset_index(name='Cantidad')
            dff.fillna(0, inplace=True)
            names = dff['User']
            values = dff['Hashtag']
            plt.scatter(names, values, c=dff['Cantidad'], s=(dff['Cantidad']*100))
            plt.colorbar()
            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=300)
            image_base642 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            context.update({'image_base642':image_base642})

        elif hashtag=='Escoja uno':
            list_of_tweets = []
            c=0
            consul = tweepy.Cursor(api.search, q='to:'+str(usuario)+' @'+str(usuario)).items()
            for tweet in consul:
                dict_ = {'User': tweet.user.name,
                        'User_Name': tweet.user.screen_name,
                        'Date': tweet.created_at,
                        'Text': tweet.text
                        }
                list_of_tweets.append(dict_)
            df2 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Date', 'Text'])

            fig, axes = plt.subplots(figsize=(20, 10))
            df3 = df2
            df3['Date'] = df3['Date'].astype(str).str[:10]
            df3 = df3['Date'].value_counts()
            df3 = df3.rename_axis('Date').reset_index(name='Count')
            df3['Date'] = pd.to_datetime(df3.Date)
            df3.sort_values(by=['Date'], inplace=True, ascending=True)
            dat = df3['Date']
            cou = df3['Count']
            plt.plot(dat, cou)
            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=300)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            context.update({'image_base64':image_base64})

        elif usuario == 'Escoja uno':
            list_of_tweets = []
            c=0
            consul = tweepy.Cursor(api.search, q='#'+str(hashtag), geocode="4.6097100,-74.0817500,500km").items()
            for tweet in consul:
                dict_ = {'User': tweet.user.name,
                        'User_Name': tweet.user.screen_name,
                        'Date': tweet.created_at,
                        'Text': tweet.text
                        }
                list_of_tweets.append(dict_)
            df4 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Date', 'Text'])

            fig, axes = plt.subplots(figsize=(30, 20))
            df5 = df4
            df5['Date'] = df5['Date'].astype(str).str[:10]
            df5 = df5['Date'].value_counts()
            df5 = df5.rename_axis('Date').reset_index(name='Count')
            df5['Date'] = pd.to_datetime(df5.Date)
            df5.sort_values(by=['Date'], inplace=True, ascending=True)
            dat = df5['Date']
            cou = df5['Count']
            plt.plot(dat, cou)
            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=300)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            context.update({'image_base64':image_base64})




    return render(request, 'analiticas/analitica1.html', context=context)

def analitica2(request):
    api = autenticacion()
    image_base64 = {}
    context = {
        'image_base64':image_base64
    }
    usuarios = Usuarios.objects.all()

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        palabra1 = request.POST.get('palabra1')
        palabra2 = request.POST.get('palabra2')


        if palabra1 != "":
            list_of_tweets = []
            for i in usuarios:
                consul = tweepy.Cursor(api.search, q='from:'+str(i.arroba)+' '+palabra1).items()
                for tweet in consul:
                    dict_ = {'User': tweet.user.name,
                            'User_Name': tweet.user.screen_name,
                            'Text': tweet.text,
                            }
                    list_of_tweets.append(dict_)

            df1 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Text',])
            dfRes = df1['User'].value_counts()
            usuariosDF = dfRes.index
            valores = dfRes.values
            fig, ax = plt.subplots()

            def func(pct, allvals):
                absolute = int(pct/100.*np.sum(allvals))
                return "{:.1f}%\n({:d} veces)".format(pct, absolute)
            wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores),
                                            textprops=dict(color="w"))
            ax.legend(wedges, usuariosDF,
                    title="Usuarios",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8)
            ax.set_title("Participacion con la palabra {} por usuario".format(palabra1))
            plt.plot()

            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=400)
            image_base641 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            image_base64.update({'image_base641':image_base641})
        if palabra2 != "":
            list_of_tweets = []
            for i in usuarios:
                consul = tweepy.Cursor(api.search, q='from:'+str(i.arroba)+' '+palabra2).items()
                for tweet in consul:
                    dict_ = {'User': tweet.user.name,
                            'User_Name': tweet.user.screen_name,
                            'Text': tweet.text,
                            }
                    list_of_tweets.append(dict_)

            df1 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Text',])
            dfRes = df1['User'].value_counts()
            usuariosDF = dfRes.index
            valores = dfRes.values
            fig, ax = plt.subplots()

            def func(pct, allvals):
                absolute = int(pct/100.*np.sum(allvals))
                return "{:.1f}%\n({:d} veces)".format(pct, absolute)
            wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores),
                                            textprops=dict(color="w"))
            ax.legend(wedges, usuariosDF,
                    title="Usuarios",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8)
            ax.set_title("Participacion con la palabra {} por usuario".format(palabra2))
            plt.plot()

            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=400)
            image_base642 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            image_base64.update({'image_base642':image_base642})

    return render(request, 'analiticas/analitica2.html', context=context)

def analitica3(request):
    api = autenticacion()
    image_base64 = {}
    candidatos = Candidatos.objects.all()
    context = {
        'candidatos': candidatos,
        'image_base64': image_base64,
    }

    if request.method == 'POST':
        palabra1 = request.POST.get('palabra1')
        palabra2 = request.POST.get('palabra2')
        palabra3 = request.POST.get('palabra3')

        if palabra1 != "":
            list_of_tweets = []
            for i in candidatos:
                consul = tweepy.Cursor(api.search, q='from:'+str(i.arroba)+' '+palabra1).items()
                for tweet in consul:
                    dict_ = {'User': tweet.user.name,
                            'User_Name': tweet.user.screen_name,
                            'Text': tweet.text,
                            }
                    list_of_tweets.append(dict_)

            df1 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Text',])
            dfRes = df1['User'].value_counts()
            candidatosDF = dfRes.index
            valores = dfRes.values
            fig, ax = plt.subplots()

            def func(pct, allvals):
                absolute = int(pct/100.*np.sum(allvals))
                return "{:.1f}%\n({:d} veces)".format(pct, absolute)
            wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores),
                                            textprops=dict(color="w"))
            ax.legend(wedges, candidatosDF,
                    title="candidatos",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8)
            ax.set_title("Utilización de la palabra {}".format(palabra1))
            plt.plot()

            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=400)
            image_base641 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            image_base64.update({'image_base641':image_base641})
        if palabra2 != "":
            list_of_tweets = []
            for i in candidatos:
                consul = tweepy.Cursor(api.search, q='from:'+str(i.arroba)+' '+palabra2).items()
                for tweet in consul:
                    dict_ = {'User': tweet.user.name,
                            'User_Name': tweet.user.screen_name,
                            'Text': tweet.text,
                            }
                    list_of_tweets.append(dict_)

            df1 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Text',])
            dfRes = df1['User'].value_counts()
            candidatosDF = dfRes.index
            valores = dfRes.values
            fig, ax = plt.subplots()

            def func(pct, allvals):
                absolute = int(pct/100.*np.sum(allvals))
                return "{:.1f}%\n({:d} veces)".format(pct, absolute)
            wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores),
                                            textprops=dict(color="w"))
            ax.legend(wedges, candidatosDF,
                    title="candidatos",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8)
            ax.set_title("Utilización de la palabra {}".format(palabra2))
            plt.plot()

            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=400)
            image_base642 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            image_base64.update({'image_base642':image_base642})
        if palabra3 != "":
            list_of_tweets = []
            for i in candidatos:
                consul = tweepy.Cursor(api.search, q='from:'+str(i.arroba)+' '+palabra3).items()
                for tweet in consul:
                    dict_ = {'User': tweet.user.name,
                            'User_Name': tweet.user.screen_name,
                            'Text': tweet.text,
                            }
                    list_of_tweets.append(dict_)

            df1 = pd.DataFrame(list_of_tweets, columns=['User', 'User_Name', 'Text',])
            dfRes = df1['User'].value_counts()
            candidatosDF = dfRes.index
            valores = dfRes.values
            fig, ax = plt.subplots()

            def func(pct, allvals):
                absolute = int(pct/100.*np.sum(allvals))
                return "{:.1f}%\n({:d} veces)".format(pct, absolute)
            wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores),
                                            textprops=dict(color="w"))
            ax.legend(wedges, candidatosDF,
                    title="candidatos",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8)
            ax.set_title("Utilización de la palabra {}".format(palabra3))
            plt.plot()

            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=400)
            image_base643 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            buf.close()
            #fig.show()
            image_base64.update({'image_base643':image_base643})


    return render(request, 'analiticas/analitica3.html', context=context)


def conexion(request):
    api = autenticacion()

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    return HttpResponse(public_tweets)


def prueba(request):
    api = autenticacion()
