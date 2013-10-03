.. _implementation-notes:

====================
Implementation Notes
====================

.. note:: This document is a brief and fairly technical discussion of how the system works under
   ideal conditions. It is also known as a "theory of operation" document. It should describe key
   algorithms, technology dependencies, and operational issues. Much of the content of this document
   can be drawn from design documents. This document will be used by the QA, technical support, and
   operations groups. The goal is to give those groups the information they need to understand,
   manage, or begin to troubleshoot the system (i.e., recognize certain behavior as normal or
   abnormal). If significantly more information is needed, it should be organized into a larger
   "operations guide".

Type of Implementation
======================

.. todo:: Fill in information that will help other engineers understand this system at-a-glance.
   Feel free to use relevant technical terms and name specific technology platforms.

.. +--------------------------+----------------------------------------------------+
.. | Type of system:          | Desktop GUI application                            |
.. |                          | Unix-style command                                 |
.. |                          | Server-side web application                        |
.. |                          | Web service                                        |
.. |                          | Client-side applet                                 |
.. |                          | Embedded application                               |
.. |                          | Reusable library                                   |
.. |                          | Reusable class framework                           |
.. |                          | Browser Plug-in                                    |
.. +--------------------------+----------------------------------------------------+
.. | Programming Language(s): | Java                                               |
.. |                          | Perl, Unix shell scripts                           |
.. +--------------------------+----------------------------------------------------+
.. | Data Storage:            | Flat files using XML                               |
.. |                          | Flat files using Java properties file format       |
.. |                          | Flat files using Java object serialization format  |
.. |                          | SQL database: MySQL                                |
.. +--------------------------+----------------------------------------------------+
.. | UI Technologies:         | Java Swing                                         |
.. |                          | XHTML, CSS, JavaScript                             |
.. +--------------------------+----------------------------------------------------+
.. | Security Technologies:   | Authentication: None needed                        |
.. |                          | Authentication: Local username and password file   |
.. |                          | Authentication: LDAP                               |
.. |                          | Authorization: Operating system file ownership and |
.. |                          | read-write-execute flag                            |
.. |                          | Authorization: Access control lists                |
.. |                          | Encryption: None needed                            |
.. |                          | Encryption: SSL                                    |
.. +--------------------------+----------------------------------------------------+

Runtime Environment
===================

.. todo:: List and describe runtime objects that make up a running system. These objects may be
   referred to by name in the sections below.

.. +----------------------+--------------------------------------------------------------------------+
.. | Processes:           | Main application process                                                 |
.. |                      | Client and server processes                                              |
.. |                      | Cron tasks                                                               |
.. |                      | Operating system services or drivers                                     |
.. +----------------------+--------------------------------------------------------------------------+
.. | Configuration Files: | PRODUCTNAME.conf: stores application configuration in Java properties    |
.. |                      | file format.                                                             |
.. |                      | Section of httpd.conf: configures components of the Apache webserver     |
.. +----------------------+--------------------------------------------------------------------------+
.. | Database Tables:     | TABLE_ONE: Each row represents a ...                                     |
.. |                      | TABLE_TWO: Each row represents a ...                                     |
.. |                      | TABLE_THREE: Each row represents a ...                                   |
.. |                      | See the persistence design document.                                     |
.. +----------------------+--------------------------------------------------------------------------+
.. | Data Files:          | \*.ext: Data files saved by the user on their local hard disk.           |
.. |                      | /var/PRODUCTNAME/upload-XXXX.dat: Files uploaded to the server.          |
.. +----------------------+--------------------------------------------------------------------------+
.. | Temporary Files:     | /tmp/PRODUCTNAME.pid: Process ID of the currently running server process |
.. |                      | /tmp/upload-XXXX.dat: Files uploaded to the server before they are       |
.. |                      | processed.                                                               |
.. +----------------------+--------------------------------------------------------------------------+
.. | Log Files:           | error.log: Serious errors are put in the normal Apache error log. Must   |
.. |                      | be writable by Unix user httpd.                                          |
.. |                      | PRODUCTNAME.log: Messages indicating the progress of normal operations   |
.. |                      | and some errors. Must be writable by Unix user httpd                     |
.. |                      | Log files are rotated nightly. Old logs are archived in ANOTHER          |
.. |                      | LOCATION.                                                                |
.. +----------------------+--------------------------------------------------------------------------+

Implementation of Specific Features
===================================

.. todo:: Write short descriptions of interesting or unexpected algorithms, limiting assumptions,
   or any other implementation detail that will impact the work of other groups. E.g., long-running
   operations that must not be interrupted. E.g., start up or shutdown scripts that are
   automatically run by the operating system.

.. * Feature name: 1-3 SENTENCE DESCRIPTION
.. * Feature name: 1-3 SENTENCE DESCRIPTION
.. * Feature name: 1-3 SENTENCE DESCRIPTION
..    * DETAILS
..    * DETAILS
..    * DETAILS
.. * Feature name: 1-3 SENTENCE DESCRIPTION
..    * DETAILS
..    * DETAILS
..    * DETAILS

Operational Procedures
======================

.. todo:: Briefly describe procedures that should be followed by operations engineers when the
   system is being run in an ASP production environment.

.. +----------------------+----------------------------------------------------------------------+
.. | Install:             | See the Installation guide                                           |
.. +----------------------+----------------------------------------------------------------------+
.. | Upgrade:             | See the Installation guide                                           |
.. +----------------------+----------------------------------------------------------------------+
.. | Start Server:        | 1. STEP                                                              |
.. |                      | 2. STEP                                                              |
.. |                      | 3. STEP                                                              |
.. +----------------------+----------------------------------------------------------------------+
.. | Stop Server:         | 1. STEP                                                              |
.. |                      | 2. STEP                                                              |
.. |                      | 3. STEP                                                              |
.. +----------------------+----------------------------------------------------------------------+
.. | Reload Config Files: | 1. STEP                                                              |
.. |                      | 2. STEP                                                              |
.. |                      | 3. STEP                                                              |
.. +----------------------+----------------------------------------------------------------------+
.. | Monitor Activity:    | Watch the PRODUCTNAME.log and error.log.                             |
.. +----------------------+----------------------------------------------------------------------+
.. | Periodic Cleanup:    | On rare occasion, /tmp/upload-XXXX.dat files can be left behind. Any |
.. |                      | such files that are more than a day old can safely be removed.       |
.. +----------------------+----------------------------------------------------------------------+

Security
========

.. todo:: Write notes on security to help operations engineers keep the system secure while it is in
   operation.

.. We take the following precautions to make the system secure:
.. 
.. * STEP
.. * STEP
.. * STEP
.. 
.. The security of the system depends on the following external factors:
.. 
.. * STEP
.. * STEP
.. * STEP

Performance and Scalability
===========================

.. todo:: Write notes on performance and scalability to help operations engineers operate the system
   efficiently.

.. NOTES ON PERFORMANCE.
.. NOTES ON SCALABILITY.

Implementation Notes Checklist
==============================

.. question:: Do these implementation notes provide enough information for operations engineers?

.. Yes, these notes have been reviewed by the operations team and requested changes have been
.. incorporated.
.. No, these notes only summarize parts of a larger operations manual.
.. No, a member of the development team is available on-call whenever the operations team may need
.. help. This is listed in the Resource Needs document and in the on-call schedule.

.. question:: Have these implementation notes been communicated to the operations and development
   teams and other stakeholders?

.. Yes, everyone has had a chance to review them. Feedback is welcome.
.. Yes, it has been posted to the project website.
.. No, some developers or operations engineers are not aware of this document. This is a risk that is
.. noted in the Risk Management section of the Project Plan.