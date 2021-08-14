def handle_follow(event) -> None:
    """Event - User follow LINE Bot

    Args:
        event (LINE Event Object): Refer to https://developers.line.biz/en/reference/messaging-api/#follow-event
    """
    user_id = event.source.user_id
    print(f"User follow! user_id: {user_id}")


def handle_unfollow(event) -> None:
    """Event - User ban LINE Bot

    Args:
        event (LINE Event Object): Refer to https://developers.line.biz/en/reference/messaging-api/#unfollow-event
    """
    user_id = event.source.user_id
    print(f"User leave! user_id: {user_id}")