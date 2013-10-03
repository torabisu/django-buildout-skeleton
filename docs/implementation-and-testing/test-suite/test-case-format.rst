================
Test Case Format
================

.. note:: This reference page documents the format of test cases and gives tips on writing test
   cases. You can copy and paste the sample test case into your test-cases.html file. This file
   itself should not be edited to hold specific test cases.

   This test case format is suitable for manual system test cases.

   The test cases should be written in enough detail that they could be given to a new team member
   who would be able to quickly start to carry out the tests and find defects.

unique-test-case-id: Test Case Title
====================================

+----------------------+--------------------------------------------------------------------------+
| Purpose:             | Short sentence or two about the aspect of the system is being tested. If |
|                      | this gets too long, break the test case up or put more information into  |
|                      | the feature descriptions.                                                |
+----------------------+--------------------------------------------------------------------------+
| Prereq:              | Assumptions that must be met before the test case can be run. E.g.,      |
|                      | "logged in", "guest login allowed", "user testuser exists".              |
+----------------------+--------------------------------------------------------------------------+
| Test Data:           | List of variables and their possible values used in the test case. You   |
|                      | can list specific values or describe value ranges. The test case should  |
|                      | be performed once for each combination of values. These values are       |
|                      | written in set notation, one per line. E.g.:                             |
|                      | loginID = {Valid loginID, invalid loginID, valid email, invalid email}   |
|                      | password = {valid, invalid, empty}                                       |
+----------------------+--------------------------------------------------------------------------+
| Steps:               | Steps to carry out the test. See step formating rules below.             |
|                      | 1. visit LoginPage                                                       |
|                      | 2. enter userID                                                          |
|                      | 3. enter password                                                        |
|                      | 4. click login                                                           |
|                      | 5. see the terms of use page                                             |
|                      | 6. click agree radio button at page bottom                               |
|                      | 7. click submit button                                                   |
|                      | 8. see PersonalPage                                                      |
|                      | 9. verify that welcome message is correct username                       |
+----------------------+--------------------------------------------------------------------------+
| Notes and Questions: | * NOTE                                                                   |
|                      | * QUESTION                                                               |
+----------------------+--------------------------------------------------------------------------+

Format of Steps
===============

Each step can be written very tersely using the following keywords:

login [as ROLE-OR-USER]
-----------------------

Log into the system with a given user or a user of the given type. Usually only stated explicitly
when the test case depends on the permissions of a particular role or involves a workflow between
different users.

visit LOCATION
--------------

Visit a page or screen. For web applications, LOCATION may be a hyperlink. The location should be a
well-known starting point (e.g., the Login screen), drilling down to specific pages should be part
of the test.

enter FIELD-NAME [as VALUE] [in SCREEN-LOCATION]
------------------------------------------------

Fill in a named form field. VALUE can be a literal value or the name of a variable defined in the
"Test Data" section. The FIELD-NAME itself can be a variable name when the UI field for that value
is clear from context, e.g., "enter password".

enter FIELDS
------------

Fill in all fields in a form when their values are clear from context or when their specific values
are not important in this test case.

click "LINK-LABEL" [in SCREEN-LOCATION]
---------------------------------------

Follow a labeled link or press a button. The screen location can be a predefined panel name or
English phrase. Predefined panel names are based on GUI class names, master template names, or
titles of boxes on the page.

click BUTTON-NAME [in SCREEN-LOCATION]
--------------------------------------

Press a named button. This step should always be followed by a "see" step to check the results.

see SCREEN-OR-PAGE
------------------

The tester should see the named GUI screen or web page. The general correctness of the page should
be testable based on the feature description.

verify CONDITION
----------------

The tester should see that the condition has been satisfied. This type of step usually follows a
"see" step at the end of the test case.

verify CONTENT [is VALUE]
-------------------------

The tester should see the named content on the current page, the correct values should be clear from
the test data, or given explicitly. This type of step usually follows a "see" step at the end of the
test case.

perform TEST-CASE-NAME
----------------------

This is like a subroutine call. The tester should perform all the steps of the named test case and
then continue on to the next step of this test case.

.. note:: Every test case must include a verify step at the end so that the expected output is very
   clear. A test case can have multiple verify steps in the middle or at the end. Having multiple
   verify steps can be useful if you want a smaller number of long tests rather than a large number
   of short tests.