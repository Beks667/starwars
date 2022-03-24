import requests
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime


count = {'count': 0, "next_page": 1, 'dates': []}
starwars = [count, ]


class StarItemView(APIView):

    def get(self, request):
        page = request.query_params.get('page', 1)
        if starwars[0]['next_page'] == int(page):
            url = f'https://swapi.dev/api/people/?page={page}'
            response = requests.get(url).json()
            starwars.append(response['results'])
            starwars[0]['count'] += 10
            starwars[0]['next_page'] += 1
            starwars[0]['dates'].append(datetime.today())
            with open('story.json', 'w') as file:
                file.write(str(starwars[0]))
                file.write('\n\n')
                for i in range(1, len(starwars)):
                    for j in starwars[i]:
                        file.write(str(j))
                        file.write('\n')
            return Response(starwars, status=status.HTTP_200_OK)
        return Response({"error": "Enter valid page"})

