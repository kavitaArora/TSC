import tableauserverclient as TSC
tableau_auth = TSC.TableauAuth('kavita.arora.vips@gmail.com', 'tabanalytics@813', site_id='datatoanalyticsdev747767')
server = TSC.Server('https://10ax.online.tableau.com')

with server.auth.sign_in(tableau_auth):
        # get all projects on site
        all_project_items, pagination_item = server.projects.get()
        print([proj.name for proj in all_project_items])
