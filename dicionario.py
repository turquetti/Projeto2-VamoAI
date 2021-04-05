import requests
import json

# dicionario = {'projects': {'totalCount': 145, 'projects': [{'id': 11692, 'lastUpdated': '2021-4-1'}, {'id': 14654, 'lastUpdated': '2021-3-29'}, {'id': 10577, 'lastUpdated': '2021-3-29'}, {'id': 79552, 'lastUpdated': '2021-3-29'}, {'id': 11772, 'lastUpdated': '2021-3-29'}, {'id': 10686, 'lastUpdated': '2021-3-29'}, {'id': 33080, 'lastUpdated': '2021-3-29'}, {'id': 93846, 'lastUpdated': '2021-3-29'}, {'id': 10535, 'lastUpdated': '2021-3-29'}, {'id': 10576, 'lastUpdated': '2021-3-29'}, {'id': 93845, 'lastUpdated': '2021-3-29'}, {'id': 33078, 'lastUpdated': '2021-3-29'}, {'id': 11874, 'lastUpdated': '2021-3-29'}, {'id': 14651, 'lastUpdated': '2021-3-29'}, {'id': 11696, 'lastUpdated': '2021-3-29'}, {'id': 11771, 'lastUpdated': '2021-3-29'}, {'id': 10730, 'lastUpdated': '2021-3-26'}, {'id': 94217, 'lastUpdated': '2021-3-25'}, {'id': 93202, 'lastUpdated': '2021-3-25'}, {'id': 32426, 'lastUpdated': '2021-3-25'}, {'id': 10759, 'lastUpdated': '2021-3-24'}, {'id': 94205, 'lastUpdated': '2021-3-23'}, {'id': 94225, 'lastUpdated': '2021-3-23'}, {'id': 93142, 'lastUpdated': '2021-3-18'}, {'id': 32947, 'lastUpdated': '2021-3-18'}, {'id': 96802, 'lastUpdated': '2021-3-9'}, {'id': 92009, 'lastUpdated': '2021-3-3'}, {'id': 96538, 'lastUpdated': '2021-3-3'}, {'id': 96547, 'lastUpdated': '2021-3-3'}, {'id': 96517, 'lastUpdated': '2021-3-1'}, {'id': 96503, 'lastUpdated': '2021-3-1'}, {'id': 96497, 'lastUpdated': '2021-3-1'}, {'id': 96546, 'lastUpdated': '2021-3-1'}, {'id': 96495, 'lastUpdated': '2021-3-1'}, {'id': 96494, 'lastUpdated': '2021-3-1'}, {'id': 96535, 'lastUpdated': '2021-3-1'}, {'id': 96492, 'lastUpdated': '2021-3-1'}, {'id': 96540, 'lastUpdated': '2021-3-1'}, {'id': 96523, 'lastUpdated': '2021-3-1'}, {'id': 96496, 'lastUpdated': '2021-3-1'}, {'id': 96522, 'lastUpdated': '2021-3-1'}, {'id': 96519, 'lastUpdated': '2021-3-1'}, {'id': 96501, 'lastUpdated': '2021-3-1'}, {'id': 96506, 'lastUpdated': '2021-3-1'}, {'id': 96504, 'lastUpdated': '2021-3-1'}, {'id': 96536, 'lastUpdated': '2021-3-1'}, {'id': 96537, 'lastUpdated': '2021-3-1'}, {'id': 96499, 'lastUpdated': '2021-3-1'}, {'id': 96534, 'lastUpdated': '2021-3-1'}, {'id': 96514, 'lastUpdated': '2021-3-1'}, {'id': 90908, 'lastUpdated': '2021-3-1'}, {'id': 96530, 'lastUpdated': '2021-3-1'}, {'id': 96541, 'lastUpdated': '2021-3-1'}, {'id': 96505, 'lastUpdated': '2021-3-1'}, {'id': 96508, 'lastUpdated': '2021-3-1'}, {'id': 96529, 'lastUpdated': '2021-3-1'}, {'id': 96515, 'lastUpdated': '2021-3-1'}, {'id': 96527, 'lastUpdated': '2021-3-1'}, {'id': 96533, 'lastUpdated': '2021-3-1'}, {'id': 96521, 'lastUpdated': '2021-3-1'}, {'id': 96614, 'lastUpdated': '2021-3-1'}, {'id': 96623, 'lastUpdated': '2021-3-1'}, {'id': 96509, 'lastUpdated': '2021-3-1'}, {'id': 96545, 'lastUpdated': '2021-3-1'}, {'id': 96531, 'lastUpdated': '2021-3-1'}, {'id': 96502, 'lastUpdated': '2021-3-1'}, {'id': 96544, 'lastUpdated': '2021-3-1'}, {'id': 96510, 'lastUpdated': '2021-3-1'}, {'id': 96525, 'lastUpdated': '2021-3-1'}, {'id': 96532, 'lastUpdated': '2021-3-1'}, {'id': 96498, 'lastUpdated': '2021-3-1'}, {'id': 96516, 'lastUpdated': '2021-3-1'}, {'id': 96500, 'lastUpdated': '2021-3-1'}, {'id': 96513, 'lastUpdated': '2021-3-1'}, {'id': 90959, 'lastUpdated': '2021-3-1'}, {'id': 96520, 'lastUpdated': '2021-3-1'}, {'id': 96526, 'lastUpdated': '2021-3-1'}, {'id': 96542, 'lastUpdated': '2021-3-1'}, {'id': 96493, 'lastUpdated': '2021-3-1'}, {'id': 96511, 'lastUpdated': '2021-3-1'}, {'id': 96121, 'lastUpdated': '2021-2-12'}, {'id': 94237, 'lastUpdated': '2021-2-12'}, {'id': 94239, 'lastUpdated': '2021-2-12'}, {'id': 94216, 'lastUpdated': '2021-2-12'}, {'id': 94228, 'lastUpdated': '2021-2-12'}, {'id': 94224, 'lastUpdated': '2021-2-12'}, {'id': 96111, 'lastUpdated': '2021-2-9'}, {'id': 93297, 'lastUpdated': '2021-2-8'}, {'id': 96641, 'lastUpdated': '2021-2-8'}, {'id': 11722, 'lastUpdated': '2021-2-5'}, {'id': 96897, 'lastUpdated': '2021-2-4'}, {'id': 96905, 'lastUpdated': '2021-2-4'}, {'id': 96907, 'lastUpdated': '2021-2-4'}, {'id': 93847, 'lastUpdated': '2021-2-3'}, {'id': 93844, 'lastUpdated': '2021-2-3'}, {'id': 96906, 'lastUpdated': '2021-1-28'}, {'id': 96122, 'lastUpdated': '2021-1-22'}, {'id': 96118, 'lastUpdated': '2021-1-22'}, {'id': 96605, 'lastUpdated': '2021-1-19'}, {'id': 96231, 'lastUpdated': '2021-1-19'}, {'id': 95927, 'lastUpdated': '2021-1-19'}, {'id': 95922, 'lastUpdated': '2021-1-19'}, {'id': 96642, 'lastUpdated': '2021-1-13'}, {'id': 95872, 'lastUpdated': '2021-1-13'}, {'id': 90768, 'lastUpdated': '2021-1-13'}, {'id': 94802, 'lastUpdated': '2021-1-13'}, {'id': 95892, 'lastUpdated': '2021-1-13'}, {'id': 40649, 'lastUpdated': '2021-1-13'}, {'id': 95031, 'lastUpdated': '2021-1-12'}, {'id': 94810, 'lastUpdated': '2021-1-11'}, {'id': 94060, 'lastUpdated': '2021-1-11'}, {'id': 93951, 'lastUpdated': '2021-1-11'}, {'id': 96435, 'lastUpdated': '2021-1-11'}, {'id': 93934, 'lastUpdated': '2021-1-11'}, {'id': 94047, 'lastUpdated': '2021-1-11'}, {'id': 95523, 'lastUpdated': '2021-1-11'}, {'id': 91923, 'lastUpdated': '2021-1-11'}, {'id': 94921, 'lastUpdated': '2021-1-11'}, {'id': 95868, 'lastUpdated': '2021-1-11'}, {'id': 94930, 'lastUpdated': '2021-1-11'}, {'id': 91736, 'lastUpdated': '2021-1-11'}, {'id': 93902, 'lastUpdated': '2021-1-11'}, {'id': 95691, 'lastUpdated': '2021-1-11'}, {'id': 95496, 'lastUpdated': '2021-1-11'}, {'id': 10498, 'lastUpdated': '2021-1-11'}, {'id': 14193, 'lastUpdated': '2021-1-11'}, {'id': 94099, 'lastUpdated': '2021-1-11'}, {'id': 94951, 'lastUpdated': '2021-1-11'}, {'id': 93854, 'lastUpdated': '2021-1-11'}, {'id': 95642, 'lastUpdated': '2021-1-11'}, {'id': 96432, 'lastUpdated': '2021-1-11'}, {'id': 96224, 'lastUpdated': '2021-1-11'}, {'id': 88581, 'lastUpdated': '2021-1-11'}, {'id': 96436, 'lastUpdated': '2021-1-11'}, {'id': 95660, 'lastUpdated': '2021-1-11'}, {'id': 13634, 'lastUpdated': '2021-1-11'}, {'id': 94178, 'lastUpdated': '2021-1-11'}, {'id': 94017, 'lastUpdated': '2021-1-11'}, {'id': 95651, 'lastUpdated': '2021-1-11'}, {'id': 14405, 'lastUpdated': '2021-1-11'}, {'id': 95591, 'lastUpdated': '2021-1-11'}, {'id': 93289, 'lastUpdated': '2021-1-11'}, {'id': 93910, 'lastUpdated': '2021-1-11'}, {'id': 96747, 'lastUpdated': '2021-1-11'}, {'id': 96810, 'lastUpdated': '2021-1-8'}]}}

# lista = []

# for i in range(0, dicionario['projects']['totalCount'] + 1):
#     for j in dicionario['projects']['projects'][i-1].values():
#         if type(j) == int:
#             lista.append(j)
import pandas as pd

quantidade = 2
dic = {}
for i in range(0, quantidade):
    r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=F8pxcg3lpaCoKgUISPrEQZwVKGY5G2IOdukbywfu&count={quantidade}')
    resp = r.json()
    
    df = pd.read(resp)
#    print(resp)
    df.head()

# def infos(self, quantidade):
#     for i,j in self.model.retorna_json(quantidade)[0].items():
#         if i == 'url':
#             self.dic_infos['Url'] = j
#         if i == 'title':
#             self.dic_infos['Title'] = j
#         if i == 'date':
#             self.dic_infos['Date'] = j
#         if i == 'explanation':
#             self.dic_infos['Explanation'] = j
#         self.lista_projetos.append(self.dic_infos)
#     print(self.lista_projetos)
#     return self.lista_projetos




