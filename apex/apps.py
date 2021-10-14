from django.apps import AppConfig
# from employee_timer import job
# import apex.signals
class ApexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apex'
    def ready(self):
        import apex.signals
        from employee_timer import job
        job.start()
