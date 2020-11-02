import tableauserverclient as TSC
tableau_auth = TSC.TableauAuth('kavita.arora.vips@gmail.com', 'tabanalytics@813', site_id='datatoanalyticsdev747767')
server = TSC.Server('https://10ax.online.tableau.com')

with server.auth.sign_in(tableau_auth):

    # get the workbook item from the site
   all_workbooks_items = server.workbooks.get()
 # print names of first 100 workbooks
   print(workbook.name for workbook in all_workbooks_items)
