class WordPressRouter(object):
    """
    A router that controls all database operations for wordpress.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == '_wordpress':
            return '_wordpress'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == '_wordpress':
            return '_wordpress'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        if db == '_wordpress':
            return model._meta.app_label == '_wordpress'
        elif model._meta.app_label == '_wordpress':
            return False
        return None
