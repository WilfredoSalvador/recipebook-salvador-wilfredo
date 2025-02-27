"""Module importing app configuration for Django framework."""

from django.apps import AppConfig


class LedgerConfig(AppConfig):
    """Class configuring ledger into an application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ledger'
