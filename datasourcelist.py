import tableauserverclient as TSC
tableau_auth = TSC.TableauAuth('kavita.arora.vips@gmail.com','tabanalytics@813',site_id='datatoanalyticsdev747767')
server = TSC.Server('https://10ax.online.tableau.com')

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])


 
 
                  

