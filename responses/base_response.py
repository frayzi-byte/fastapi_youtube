def ok(data=None, message: str = "Success") -> dict:
    return {
        "message": message,
        "data": data,
    }
