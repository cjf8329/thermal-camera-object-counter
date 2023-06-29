import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "ENTER ID HERE"

def main(clusters):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        for x in range(2, len(clusters)+1):
            print("updating")
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A{x}",
                                   valueInputOption="USER_ENTERED", body={"values": [[f"{x-1}"]]}).execute()
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!B{x}",
                                   valueInputOption="USER_ENTERED", body={"values": [[f"{clusters[x-1][1]}"]]}).execute()
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!C{x}",
                                   valueInputOption="USER_ENTERED", body={"values": [[f"{clusters[x-1][0]}"]]}).execute()

    except HttpError as error:
        print(error)


if __name__ == "__main__":
    #main([(0.3, 35), (0.4, 45), (0.5, 55)])
    pass
