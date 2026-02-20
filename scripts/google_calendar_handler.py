import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def add_google_calendar_event(
    summary: str = "Test Event",
    start_time: str = "2026-02-19T12:00:00",
    end_time: str = "2026-02-19T13:00:00",
    description: str = "This is to test out the google api and it works!",
    location: str = None,
):
    """
    Add a new event to Alex's Google Calendar.

    This function creates a calendar event with the specified details.
    Times should be provided in ISO 8601 format.

    Parameters:
        summary: The title or summary of the calendar event
        start_time: The start date and time in ISO 8601 format (e.g., '2026-02-19T10:00:00')
        end_time: The end date and time in ISO 8601 format (e.g., '2026-02-19T11:00:00')
        description: Optional description or notes for the event
        location: Optional location for the event
    """

    try:
        scopes = ["https://www.googleapis.com/auth/calendar.events"]
        credentials = None
        token_path = os.path.join(os.path.dirname(__file__), "..", "token.pickle")
        credentials_path = os.path.join(os.path.dirname(__file__), "..", "credentials.json")

        if os.path.exists(token_path):
            with open(token_path, "rb") as token_file:
                credentials = pickle.load(token_file)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)
                credentials = flow.run_local_server(port=0)
            with open(token_path, "wb") as token_file:
                pickle.dump(credentials, token_file)

        service = build("calendar", "v3", credentials=credentials)

        event = {
            "summary": summary,
            "start": {"dateTime": start_time, "timeZone": "America/Chicago"},
            "end": {"dateTime": end_time, "timeZone": "America/Chicago"},
        }
        if description:
            event["description"] = description
        if location:
            event["location"] = location

        created_event = service.events().insert(calendarId="primary", body=event).execute()

        return {
            "success": True,
            "message": f"Event '{summary}' created from {start_time} to {end_time}",
            "event_data": created_event,
        }

    except Exception as error:
        print(f"Error in adding Google Calendar event: {error}")
        return {"success": False, "error": str(error)}