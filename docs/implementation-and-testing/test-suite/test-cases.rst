==========
Test Cases
==========



login-1: Normal User Login
==========================

+----------------------+---------------------------------------------------------------------------+
| Purpose:             | Test that users can log in with the proper username or email address and  |
|                      | their password.                                                           |
+----------------------+---------------------------------------------------------------------------+
| Prereq:              | User is not already logged in.                                            |
|                      | User testuser exists, and account is in good standing.                    |
+----------------------+---------------------------------------------------------------------------+
| Test Data:           | usernameOrEmail = {testuser, bogususer, testuser@nospam.com,              |
|                      | test@user@nospam.com, empty}                                              |
|                      | password = {valid, invalid, empty}                                        |
+----------------------+---------------------------------------------------------------------------+
| Steps:               | Steps to carry out the test. See step formating rules below.              |
|                      | 1. visit LoginPage                                                        |
|                      | 2. enter userID                                                           |
|                      | 3. enter password                                                         |
|                      | 4. click login                                                            |
|                      | 5. see the terms of use page                                              |
|                      | 6. click agree radio button at page bottom                                |
|                      | 7. click submit button                                                    |
|                      | 8. see PersonalPage                                                       |
|                      | 9. verify that welcome message is correct username                        |
+----------------------+---------------------------------------------------------------------------+
| Notes and Questions: | * This assumes that user has not agreed to terms-of-use already.          |
|                      | * Does this work without browser cookies?                                 |
+----------------------+---------------------------------------------------------------------------+

login-2: Locked-out User Login
==============================

ETC ETC