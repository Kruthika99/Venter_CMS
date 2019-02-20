"""Helper functions for Venter modules."""

from django.contrib.auth.models import User
from .models import Organisation, Profile


def create_org():
    """Helper function for creating organisations during tests."""
    return Organisation.objects.create(organisation_name="Test Org")

def create_profile():
    """Helper function for creating test user and test profile."""
    user = User.objects.create_user('Test')
    org = create_org()
    return Profile.objects.create(user=user, organisation_name=org)
