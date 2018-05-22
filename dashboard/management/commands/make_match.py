from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from dashboard.views import make_match, chk_investment

class Command(BaseCommand):
    args = ''
    help = 'Check the Invetsment, and update necessary Investment daily'

    def handle(self, *args, **options):
        make_match()
        chk_investment()


