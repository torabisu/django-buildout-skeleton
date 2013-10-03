.. _software-requirements-specification:

===================================
Software Requirements Specification
===================================

.. note:: The SRS precisely defines the software product that will be built. Decisions made in
   writing the SRS are based on information in the project proposal and user needs documents. The
   SRS sets requirements that must be satisfied by the system design. The SRS is verified and
   validated by activities outlined in the QA plan.

Introduction
============

.. todo:: Provide a brief overview of this release of the product. You can copy text from the
   project proposal, paste it here, and shorten it.

.. PARAGRAPH
.. 
.. PARAGRAPH

For more information, see :ref:`project-proposal`

Use Cases
=========

.. ONE PARAGRAPH OVERVIEW
.. 
.. Details:
.. 
.. * Actors are described in the user needs document.
.. * The use case suite lists all use cases in an organized way.

Functional Requirements
=======================

.. ONE PARAGRAPH OVERVIEW
.. 
.. Details:
.. 
.. * The feature set lists all features in an organized way.

Non-Functional Requirements
===========================

.. todo:: Describe the non-functional requirements for this release. Some examples are provided
   below.

.. question:: What are the usability requirements?

.. Our main criteria for making the system usable is the difficulty of performing each high-frequency
.. use case. Difficulty depends on the number of steps, the knowledge that the user must have at each
.. step, the decisions that the user must make at each step, and the mechanics of each step (e.g.,
.. typing a book title exactly is hard, clicking on a title in a list is easy).
.. 
.. The user interface should be as familiar as possible to users who have used other web applications
.. and Windows desktop applications. E.g., we will follow the UI guidelines for naming menus, buttons,
.. and dialog boxes whenever possible.
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * Government customers will demand section508 compliance
.. * Support learnability with principles of Instructive Interaction
.. * The customer wants extensive on-line help, but is not demanding a printed manual.

.. question:: What are the reliability and up-time requirements?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What are the safety requirements?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What are the security requirements?

.. Access will be controlled with usernames and passwords.
.. 
.. Only administrator users will have access to administrative functions, average users will not.
.. 
.. Details:
.. 
.. * Passwords must be 4-14 characters long
.. * We will not use encrypted communications (SSL) for this website
.. * DETAIL

.. question:: What are the performance and scalability requirements requirements?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What are the maintainability and upgradability requirements?

.. Maintainability is our ability to make changes to the product over time. We need strong
.. maintainability in order to retain our early customers. We will address this by anticipating several
.. types of change, and by carefully documenting our design and implementation.
.. 
.. Upgradability is our ability to cost-effectively deploy new versions of the product to customers
.. with minimal downtime or disruption. A key feature supporting this goal is automatic download of
.. patches and upgrade of the end-user's machine. Also, we shall use data file formats that include
.. enough meta-data to allow us to reliably transform existing customer data during an upgrade.
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What are the supportability and operability requirements?

.. Supportability is our ability to provide cost effective technical support. Our goal is to limit our
.. support costs to only 5% of annual licensing fees. The product's automatic upgrade feature will help
.. us easily deploy defect fixes to end-users. The user guide and product website will include a
.. troubleshooting guide and checklist of information to have at hand before contacting technical
.. support.
.. 
.. Operability is our ability to host and operate the software as an ASP (Application Service
.. Provider). The product features should help us achieve our goal of 99.9% uptime (at most 43 minutes
.. downtime each month). Key features supporting that are the ability to do hot data backups, and
.. application monitoring.
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What are the business life-cycle requirements?

.. The business life-cycle of a product includes everything that happens to that product over a period
.. of several years, from initial purchase decision, through important but infrequent use cases, until
.. product retirement. Key life-cycle requirements are listed below.
.. 
.. Details:
.. 
.. * Customers must be able to manage the number of licenses that they have and make informed decisions
..   to purchase more licenses when needed
.. * The product shall support daily operations and our year-end audit
.. * The customer data shall be stored in a format that is still accessible even after the application
..   has been retired

Environmental Requirements
==========================

.. todo:: Describe the environmental requirements for this release. Environmental requirements
   describe the larger system of hardware, software, and data that this product must work within.
   Some examples are provided below.

.. question:: What are the system hardware requirements?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What are the system software requirements?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * DETAIL
.. * DETAIL
.. * DETAIL

.. question:: What application program interfaces (APIs) must be provided?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * We must implement this standard API.
.. * DETAIL
.. * DETAIL

.. question:: What are the data import and export requirements?

.. PARAGRAPH
.. 
.. PARAGRAPH
.. 
.. Details:
.. 
.. * The system will store all data in a standard SQL database, where it can be accessed by other
..   programs.
.. * The system will store all data in an XML file, using a standard DTD.
.. * The system will read and write valid .XYZ files used by OTHER APPLICATION
.. * DETAIL