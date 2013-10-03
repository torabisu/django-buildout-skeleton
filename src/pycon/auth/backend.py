import logging

from django_auth_ldap.backend import LDAPBackend


logger = logging.getLogger(__name__)


class ActiveDirectoryBackend(LDAPBackend):
    pass