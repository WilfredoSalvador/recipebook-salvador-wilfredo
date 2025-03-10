"""
Module importing app configuration for UserAccounts.
"""
from django.apps import AppConfig


class UseraccountsConfig(AppConfig):
    """
    Class for setting name and app configuration of UserAccounts app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserAccounts'
