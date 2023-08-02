import steamspypi

TARGET_RANKING = 'top100in2weeks'


def get_top_100(target=TARGET_RANKING):
    data = steamspypi.download({'request': target})
    app_ids = list(data.keys())

    return app_ids
