token_payload = {
    "name": "alexQA"
}

invalid_mandatory_field_token_payload = {
    "username": "alexQA"
}

wrong_format_token_payload = {
    "username": 23423
}
create_meme_payload = {
    "text": "google joke",
    "url": "https://images.app.goo.gl/6apzw1kD4LwQJVJK6",
    "tags": ["it meme"],
    "info": {
        "key1": "picture",
        "key2": "humor"

    }
}

default_meme_payload = {
    "text": "the boys meme",
    "url": "https://images.app.goo.gl/2nbTMdAqdM4r9eCp7",
    "tags": ["tv show"],
    "info": {
        "key1": "homelander",
        "key2": "dark humor"

    }
}

create_meme_payload_without_text_field = {
    "text": "google joke",
    "url": "https://images.app.goo.gl/6apzw1kD4LwQJVJK6",
    "tags": ["it meme"],
    "info": {
        "key1": "picture",
        "key2": "humor"

    }
}

create_meme_payload_with_wrong_format_tag_field = {
    "text": "google joke",
    "url": "https://images.app.goo.gl/6apzw1kD4LwQJVJK6",
    "tags": 123,
    "info": {
        "key1": "picture",
        "key2": "humor"

    }
}

update_meme_payload = {
    "id": "",
    "text": "first april joke ",
    "url": "https://images.app.goo.gl/nZwBM2H44pPf5uVb7",
    "tags": [" we are family"],
    "info": {
        "key1": "epam",
        "key2": "community"

    }
}

update_alien_meme_payload = {
    "id": 1320,
    "text": "first april joke ",
    "url": "https://images.app.goo.gl/nZwBM2H44pPf5uVb7",
    "tags": [" we are family"],
    "info": {
        "key1": "epam",
        "key2": "community"

    }
}

update_meme_payload_with_invalid_id = {
    "id": "test",
    "text": "first april joke ",
    "url": "https://images.app.goo.gl/nZwBM2H44pPf5uVb7",
    "tags": [" we are family"],
    "info": {
        "key1": "epam",
        "key2": "community"

    }
}