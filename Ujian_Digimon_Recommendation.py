from flask import Flask, render_template,request,redirect,abort
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('menu.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    nama = []
    stage = []
    typee = []
    attribute = []
    image = []
    nama_asli = []
    stage_asli = []
    typee_asli = []
    attribute_asli = []
    image_asli = []
    
    df = pd.read_json('digimon.json')

    df = df[['digimon','stage','type','attribute','image']]

    def combine_features(row):
        return str(row['stage'])+' '+str(row['type'])+' '+str(row['attribute'])

    df['combined_features'] = df.apply(combine_features, axis =1)

    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df['combined_features'])

    cosine_sim = cosine_similarity(count_matrix)

    body = request.form
    namaDigi = body['nama'].lower()
    namaDigi = namaDigi.capitalize()

    indexSukaDigimon = df[df['digimon'] == namaDigi].index.values[0]

    similar_digimon = list(enumerate(cosine_sim[indexSukaDigimon]))

    sorted_similar_digimon = sorted(similar_digimon, key=lambda x:x[1],reverse=True)
    if namaDigi not in list(df['digimon']):
        return redirect('/error')

    for i in sorted_similar_digimon[:7]:
        if df.iloc[i[0]]['digimon'] != namaDigi:
            nama.append(df.iloc[i[0]]['digimon'])
            stage.append(df.iloc[i[0]]['stage'])
            typee.append(df.iloc[i[0]]['type'])
            attribute.append(df.iloc[i[0]]['attribute'])
            image.append(df.iloc[i[0]]['image'])
    for j in sorted_similar_digimon[:7]:
        if df.iloc[j[0]]['digimon'] == namaDigi:
            nama_asli.append(df.iloc[j[0]]['digimon'])
            stage_asli.append(df.iloc[j[0]]['stage'])
            typee_asli.append(df.iloc[j[0]]['type'])
            attribute_asli.append(df.iloc[j[0]]['attribute'])
            image_asli.append(df.iloc[j[0]]['image'])

    return render_template('hasil.html',data={
        'nama': nama, 'stage':stage, 'type' :typee,'attribute':attribute,'image':image,
        'namas': nama_asli, 'stages':stage_asli, 'types':typee_asli,'attributes':attribute_asli,'images':image_asli
    })

@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)