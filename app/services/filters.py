def filter_event(event):
    filtered = {
        "activityID": event.get("activityID"),
        "startTime": event.get("startTime"),
        "note": event.get("note"),
        "link": event.get("link"),
        "cmeAnalysis": None,
    }

    cme_analyses = event.get("cmeAnalyses", [])
    for analysis in cme_analyses:
        if analysis.get("isMostAccurate"):
            filtered["cmeAnalysis"] = {
                "time21_5": analysis.get("time21_5"),
                "latitude": analysis.get("latitude"),
                "speed": analysis.get("speed"),
                "note": analysis.get("note"),
                "link": analysis.get("link"),
            }
            break

    return filtered
