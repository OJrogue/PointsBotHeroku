import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tutorial").sheet1  # Open the spreadsheet


# gets what armor toon has
def get_armor(row):
    armor = "None"
    for x in row[6:11]:
        if x == 'x':
            armor = "DL"
        else:
            armor = "None"
    if armor == "DL":
        for x in row[14:19]:
            if x == 'x':
                armor = "EDL"
            else:
                armor = "DL"
    return armor


# gets what armor toon has
def get_weapons(row):
    weapon = "None"
    for x in row[11:13]:
        if x == 'x':
            weapon = "DL"
        else:
            weapon = "None"
    if weapon == "DL":
        for x in row[20:22]:
            if x == 'x':
                weapon = "EDL"
            else:
                weapon = "DL"
    return weapon


# reads toon points
def read_points(name):
    try:
        names = sheet.col_values(1)
        lower_names = [item.lower() for item in names]
        row_number = lower_names.index(name) + 1
        row = sheet.row_values(row_number)

        name = row[0]
        ingame_class = row[1]
        points = row[4]
        armor = get_armor(row)
        weapons = get_weapons(row)
        if len(row) >= 19:
            echoes = row[19]
        else:
            echoes = 0

        return [name,ingame_class, points, armor,weapons,echoes]
    except ValueError:
        return False
