===========
Persistence
===========

Overview
========

.. todo:: Answer the questions below to help you design needed persistence features. Some example
   text is provided. Add or delete text as needed.

.. question:: What are the most important facts that a developer should know about persistent data
   storage in this system?

.. PARAGRAPH OR BULLETS

.. question:: What are the ranked goals for persistence in this system?

.. 1. Expressiveness
.. 2. Ease of access
.. 3. Reliability
.. 4. Data capacity
.. 5. Data security
.. 6. Performance
.. 7. Interoperability

Central Database
================

.. question:: What is the logical database design?

.. The logical database design is described in this UML model or this ER diagram.

.. Additional logical constraints on the database are:

.. * Students can repeat a course (and thus have two records for the same course in their transcript),
..   if and only if they got a grade of "C-" or lower, or the course number is 198, 199, 298, or 299.
.. * A grade of "A+" is valid only for transcript entries during or after Fall 1990. Prior to that
..   term, the highest possible grade was an "A".
.. * LOGICAL CONSTRAINT THAT CANNOT BE EXPRESSED IN THE DIAGRAM
.. * LOGICAL CONSTRAINT THAT CANNOT BE EXPRESSED IN THE DIAGRAM

.. question:: What are the physical tables and views?

.. The physical database design is described in this UML model or this ER diagram.

.. question:: How will objects in the application be stored in the database?

.. We will use one database table for each class, and one row in the database for each persistent
.. instance of that class.
.. We will use a library to do our object-relational mapping. (E.g., torque, castor, JDO, ADO,
.. hibernate)

.. question:: What database access controls will be used?

.. A database user account has been created that has access to the needed application database tables.
.. The username and password for this account is stored in a configuration file read by the application
.. server. The database limits login by that user to only the IP-address used by the application
.. server.

.. question:: Is this application's central database accessible to other applications?

.. Yes. The database is an important point of interoperability for new applications to be added later.
.. The database itself provides support for access controls and checks validity constraints so that a
.. defective application cannot corrupt the database.
.. No. This database should always be accessed through this application. All relevant pieces of
.. information are available through the application interfaces. The database itself does not protect
.. against data corruption that could be caused by other applications.

File Storage
============

.. question:: What data needs to be stored in files?

.. Nothing is stored in files, everything is in the database.
.. The server stores most data in the database, but mailing list attachments are written to files on
.. the server hard disk.
.. All user documents are stored in files on their computer hard disk.

.. question:: What are the conventions for directory structure and file naming?

.. N/A
.. Files are stored on the server as /var/data/attachments/msgNNNN-MMM.dat.
.. Users store files anywhere on their computer, with the filename extension .TST.

.. question:: What file system access controls will be used?

.. N/A
.. Files for message attachments are only readable and writable by the mailing list archiving process
.. that runs as operating system user "archdaemon".
.. Users can use whatever file permissions they like.

.. question:: What file format will be used?

.. The XYZ standard file format.
.. A java .properties file.
.. A window's .ini file.
.. An XML file using this DTD file.
.. A simple text file with the following format: ...
.. A custom binary file in the following format: ...

Distributed Storage
===================

.. question:: What information (if any) will be stored on client machines? For how long?

.. A cookie will be stored on the user machine for the purpose of identifying a user session. When the
.. user logs out or closes their web browser, the cookie is deleted. Most browsers will not even write
.. this cookie to the disk.
.. The a cookie is stored on the user's computer that is equivalent to their password (but it is NOT
.. actually their password). This cookie is needed for the auto-login feature. The cookie lasts a
.. maximum of 30 days, and it can only be used from the same IP address.
.. User preferences for color scheme are stored in cookies in their browser. This information is not at
.. all sensitive, so it is kept indefinitely.
.. All the user data will be stored on files on their computers.

Persistence Mechanisms Checklist
================================

.. question:: Expressiveness: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Ease of access: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Reliability: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Capacity: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Security: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Performance: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Interoperability: To what extent has this been achieved?

.. 2-4 SENTENCES

.. question:: Has the persistence design been communicated to the development team and other
   stakeholders?

.. Yes, everyone understands. Feedback is welcome.
.. No, this is a risk that is noted in the Risk Management section.