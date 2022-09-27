from django.apps import AppConfig


class SearchEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search_engine'
    def ready(self) -> None:
        from search_engine.loader import load_models
        from noticias.models import New

        load_models(New, 'title', 'body')
        return super().ready()
