import tableauserverclient as TSC

server=TSC.Server('https://10ax.online.tableau.com')
server.use_server_version()
tableau_auth=TSC.TableauAuth('kavita.arora.vips@gmail.com','tabanalytics@813',site_id='datatoanalyticsdev747767')

with server.auth.sign_in(tableau_auth):
    #create new project
    new_project = TSC.ProjectItem("Project_name","Desc")
    new_project = server.projects.create(new_project)
