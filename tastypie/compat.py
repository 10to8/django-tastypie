import django

def get_module_name(meta):
    return getattr(meta, 'model_name', None) or getattr(meta, 'module_name')

# commit_on_success replaced by atomic in Django >=1.8
atomic_decorator = getattr(django.db.transaction, 'atomic', None) or getattr(django.db.transaction, 'commit_on_success')
