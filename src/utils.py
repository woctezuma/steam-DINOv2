def retrieve_file_index(app_id, filtered_app_ids):
    try:
        file_index = filtered_app_ids.index(app_id)
    except ValueError:
        file_index = None
    return file_index
