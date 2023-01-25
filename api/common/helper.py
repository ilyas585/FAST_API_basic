from db.session import db_session


def check_token(token):
    if not isinstance(token, str):
        return {"message": "incorrect token", "details": "type is not string"}
    if not len(token.split('-')) == 5:
        return {"message": "incorrect token", "details": "token not with 5 blocks"}
    if token not in db_session.cache_by_token:
        return {"message": "Authorization error", "details": "token not in cashe"}
