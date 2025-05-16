def default_serializer(data):
    return {"count": len(data), "data": data}


def summary_serializer(events, critical_count, speeds):
    return {
        "total_events": len(events),
        "critical_events": critical_count,
        "average_speed": round(sum(speeds) / len(speeds), 2) if speeds else 0,
        "max_speed": max(speeds) if speeds else None,
        "min_speed": min(speeds) if speeds else None,
    }
