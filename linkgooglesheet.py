import gspread 
from oauth2client.service_account import ServiceAccountCredentials as sac
auth_json="testvps-452508-d0edd1e9840b.json"
gs_scopes=['https://spreadsheets.google.com/feeds']
cr=sac.from_json_keyfile_name(auth_json,gs_scopes)
gs_client=gspread.authorize(cr)
spreadsheet_key='1hm8cbTXtImtYFNamyb1UKe7Xf3uLEs1V6zGsge9FGWY'
sheet=gs_client.open_by_key(spreadsheet_key)
wks=sheet.sheet1
wks.clear()
listtitle=["Name","phone"]
wks.append_row(listtitle)
listdata=["BOXI","0981-805082"]
wks.append_row(listdata)