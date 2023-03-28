"""
CREADO POR CARLOS RICARDO VILLENA CABREJOS
"""
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

creds = Credentials.from_service_account_file('api-python-380220-366fd91b39ae.json')

analytics = build('analyticsreporting', 'v4', credentials=creds)

report = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': '242748645',
                'dateRanges': [{'startDate': '2023-02-01', 'endDate': '2023-02-28'}],
                'metrics': [{'expression': 'ga:pageviews'}],
                'dimensions': [{'name': 'ga:pagePath'}],
                'dimensionFilterClauses': [
                    {
                        'filters': [
                            {
                                'dimensionName': 'ga:dimension3',  # Nombre de la dimensión personalizada
                                'expressions': ['Nkpzc3R5WkhMYTM1ZzFsZmVIQlR3UT09'],  # Valor a comparar
                                'operator': 'EXACT'  # Operador de comparación
                            }
                        ]
                    }
                ]
            }]
    }
).execute()

for report in report.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
        dimensions = row.get('dimensions', [])
        metrics = row.get('metrics', [])

        for i, values in enumerate(metrics):
            print('URL: ', dimensions[0], 'Pageviews: ', values.get('values')[0])
