def add_google_calendar_event(
    summary: str,
    start_time: str,
    end_time: str,
    description: str = None,
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
        # TODO: Implement actual Google Calendar API integration
        # For now, return a placeholder response
        event_data = {
            "summary": summary,
            "start_time": start_time,
            "end_time": end_time,
        }

        if description:
            event_data["description"] = description

        if location:
            event_data["location"] = location

        return {
            "success": True,
            "message": f"Event '{summary}' would be created from {start_time} to {end_time}",
            "event_data": event_data,
        }

    except Exception as error:
        print(f"Error in adding Google Calendar event: {error}")
        return {"success": False, "error": str(error)}
