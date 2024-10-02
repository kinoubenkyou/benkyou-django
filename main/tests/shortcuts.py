def format_datetime(datetime_):
    return (
        f"{datetime_.day}"
        f" {datetime_.strftime("%b")}"
        f" {datetime_.year:04}"
        f" {datetime_.strftime("%I:%M:%S %p %z")}"
    )
