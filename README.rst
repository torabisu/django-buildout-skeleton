========================
Django Buildout Skeleton
========================

A buildout skeleton (With example apps) to assist with a fresh Django deployment.  Presented at
PyConZA 2013.

Templates
=========

Templates removed due to Copywright, can get from https://wrapbootstrap.com/ and pull into
your own base.html / base-layout.html Django template files.

API
===

The API application runs through the INSTALLED_APPS, and looks in each application for an apy.py
file.  If found, it looks for all ViewSet's, and adds them to a global router.  This pulls all
API's into a single /api/ url.

Legacy Databases
================

https://docs.djangoproject.com/en/dev/topics/db/multi-db/ explains how to handle multiple databases,
have a look at the database routers section.

For pulling in your legacy database model, have a look at
https://docs.djangoproject.com/en/dev/howto/legacy-databases/



