ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


def allowed_file(filename):
    return filename.split('.')[-1] in ALLOWED_EXTENSIONS
