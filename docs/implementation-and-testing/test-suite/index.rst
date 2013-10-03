.. _test-suite:

==========
Test Suite
==========

.. note:: This is a test suite for manual system testing. It is just one activity in the overall QA
   plan. A test case suite is simply a table of contents for the individual test cases. Organizing
   the suite of test cases by priority, functional area, actor, business object, or release can help
   identify parts of the system that need additional test cases.

.. todo:: Before writing individual test cases, list the test cases that you think you will need.
   Organize them in a way that will purposely leave visible blanks on this page if you are missing
   use cases. Choose one or more of the organizations show below.

.. note:: Refer back to your use cases document. Use them for ideas and make sure that you cover all
   of them. Remember that test cases are more precise than use cases, test cases should reference
   specific details of your implementation, and there may be several test cases for a given use
   case.

.. note:: The test case suite can be organized into nested lists according to other coverage
   criteria, e.g., by actor. Or, it can be organized into tables that consider two aspects at a
   time, e.g., business objects vs. actor. If a certain section of the tree or table does not need
   test cases, explicitly mark it "N/A". Otherwise, if a section needs more test cases than you have
   written yet, mark it "TODO". If one cell or list item contains many tests, break that section out
   into its own table, as done for the enrollment feature below.

Test Cases by Business Object and Operation
===========================================

+-------------+-----+---------------+------+--------+--------+-------+
| BO / Action | Add | List / Browse | Edit | Delete | Search | Other |
+=============+=====+===============+======+========+========+=======+
|             |     |               |      |        |        |       |
+-------------+-----+---------------+------+--------+--------+-------+


Test Cases by Feature Priority
==============================

.. todo:: Use this outline to make sure that high priority features are adequately tested.  List
   features by priority, and then list the test cases for each feature. If a feature needs more
   test cases, note that with "TODO".
   
Essential
---------

.. * F-01: student-add-1 student-add-2 student-add-3
.. * F-02: enroll-1 enroll-2 enroll-3 enroll-priority-1 enroll-priority-2 enroll-restricted-1

Expected
--------

.. * F-22: student-search-1 student-search-2 course-search-1
.. * F-23: room-add-1 room-add-2 room-edit-1 TODO

Desired
-------

.. * F-31: inst-eval-1 inst-eval-2

Test Cases by Use Case Priority
===============================

.. todo:: Use this outline to make sure that high priority use cases are adequately tested. List use
   cases by priority, and then list the test cases for each use case. If a use case needs more test
   cases, note that with "TODO".

Essential
---------
.. 
.. * UC-01: student-add-1 student-add-2
.. * UC-01: student-add-3
.. * UC-02: enroll-1
.. * UC-03: enroll-2
.. * UC-04: enroll-3
.. * UC-05: enroll-priority-1 enroll-priority-2
.. * UC-06: enroll-restricted-1
  
Expected
--------

.. * UC-22: student-search-1 student-search-2
.. * UC-23: course-search-1
.. * UC-30: room-add-1 room-add-2
.. * UC-31: room-edit-1 TODO
.. * UC-32: TODO
.. * UC-33: TODO

Desired
-------

.. * UC-40: inst-eval-1 inst-eval-2