.. _qa-plan:

=======
QA Plan
=======

.. todo:: For each release, update this file by filling in answers to the questions. In cases where
   multiple answers are already written, delete those answers that do not apply.

.. note:: This document specifies quality goals, selects strategies for assuring that those goals
   have been met, and details a plan of action to carry out those strategies.
      
Introduction
============

.. question:: Why is this QA plan needed?
   
.. "Quality" refers to all the good things that we would like to see in our product. We build a
.. quality product and assure its quality by keeping quality in mind all the time and performing the
.. selected activities below. Testing is one QA activity, but it is not the best or only one, other
.. QA activities include the use of style guides and checklists, review meetings, use of analysis
.. tools, and careful quality measurements and estimates. A plan is needed to select and coordinate
.. all the QA activities.

.. question:: What QA lessons were learned in previous releases?

.. None yet. This is the first release.
.. 
.. * Different browsers render the same HTML page differently, so we must test each version of each
..   supported browser.
.. * In a previous release, customers found that punctuation (e.g., quotation marks and less-than
..   signs) were entered and processed properly, but not displayed properly. From now on, we must
..   test both validation and display of special characters.
.. * Large datasets can sometimes make our system fail if the space used for temporary data is used
..   up. Our test plans should include more data volume tests.

.. question:: What is the scope of this QA plan?

.. All components and aspects of the system will be evaluated in this release.
.. 
.. There are many quality goals and approaches to assuring them. Since we have limited time and
.. resources for this release, we will focus on the following components and aspects:
.. 
.. * COMPONENT-1
.. * COMPONENT-2
.. * COMPONENT-3
.. * FEATURE-1
.. * FEATURE-2

.. todo:: Sum up the plan in a few sentences. The text below is just a sample.

.. question:: What is the summary of this plan?

.. In this release we will continue to use development practices that support all of our quality
.. goals, but we will focus on functional correctness and robustness. We will do that with the
.. following major activities:
.. 
.. * using if-statements to test preconditions and assert statements to test invariants and
..   postconditions
.. * conducting frequent reviews
.. * performing automated unit and regression testing with JUnit
.. * carrying out structured manual system testing
.. * keeping all issues up-to-date in an issue tracking database

Quality Goals for this Release
==============================

.. todo:: Add or edit goals to fit your project. Group them by priorities that make sense for your
   project on this particular release.

.. * Essential
.. 
..    * Functionality > Correctness
..    * Functionality > Robustness
.. 
.. * Expected
.. 
..    * Functionality > Accuracy
..    * Functionality > Compatibility
..    * Functionality > Factual correctness
..    * Usability > Understandability and Readability
..    * Usability > Learnability and Memorability
..    * Usability > Task support
..    * Usability > Efficiency
..    * Usability > Safety
..    * Usability > Consistency and Familiarity
..    * Usability > Subjective satisfaction
..    * Security
.. 
.. * Desired
.. 
..    * Reliability > Consistency under load
..    * Reliability > Consistency under concurrency
..    * Reliability > Availability under load
..    * Reliability > Longevity
..    * Efficiency
..    * Scalability
..    * Scalability > Performance under load
..    * Scalability > Large data volume
..    * Operability
..    * Maintainability > Understandability
..    * Maintainability > Evolvability
..    * Maintainability > Testability

QA Strategy
===========

.. todo:: Consider the activities listed below and delete those that are not applicable to your
   project. Edit and add new activities if needed. For each activity, specify the coverage or
   frequency that you plan to achieve. If you do not plan to perform an activity, write "N/A".

+----------+-----------------------+-------------+
| Activity | Coverage or Frequency | Description |
+==========+=======================+=============+
|          |                       |             |
+----------+-----------------------+-------------+


QA Strategy Evaluation
======================

.. todo:: Use the following table to evaluate how well your QA Strategy will assure your QA goals.

+------+---------------+------------+--------------+----------------+--------------+-----------------------+-------------------+
| Goal | Preconditions | Assertions | Buddy Review | Review Meeting | Unit Testing | Manual System Testing | Overall assurance |
+======+===============+============+==============+================+==============+=======================+===================+
|      |               |            |              |                |              |                       |                   |
+------+---------------+------------+--------------+----------------+--------------+-----------------------+-------------------+

Cell values in the table above are subjective estimates of the effectiveness of each activity. This
table helps to identify quality goals that are not being adequately assured.

Evaluation Cell Values
----------------------

* High: This activity gives a strong assurance that the goal has been met in development.
* Medium: This activity gives a medium assurance that the goal has been met in development.
* Low: This activity gives only a little assurance that the goal has been met in development.
* None: This activity does not address the goal.

Overall Assurance Values
------------------------

.. * Strong: The set of activities together provide strong assurance that the goal has been met in
..   development.
.. * Weak: The activities together provide limited assurance that the goal has been met in development.
.. * At-Risk: There is little or no assurance that this goal has been met.

.. note:: As a rule of thumb, it takes at least two "high" activities and one "medium" to give a
   "strong" overall rating. Likewise, it takes at least two "medium" and one "low" activities to
   rate a "weak" overall rating.

Plan of Action
==============

.. todo:: Adjust this plan to fit your project.  Once the plan is outlined, tasks should be
   assigned to individuals and tracked to completion.

.. 1. Preconditions and Assertions
.. 
..    * Refine requirements document whenever preconditions are not already determined
..    * Create validation functions for use by preconditions and assertions, as needed
..    * Write preconditions and assertions in code
.. 
.. 2. Review meetings
.. 
..    * Assign buddy reviewers whenever a change to a release branch is considered
..    * Select an at-risk document or section of code for weekly review meetings
..    * Each week, identify reviewers and schedule review meetings
..    * Reviewers study the material individually for 2 hours
..    * Reviewers meet to inspect the material for 2 hours
..    * Place review meeting notes in the repository and track any issues identified in review meetings
.. 
.. 3. Unit tests
.. 
..    * Set up infrastructure for easy execution of JUnit tests (this is just an Ant target)
..    * Create unit tests for each class when the class is created
..    * Execute unit tests before each commit. All tests must pass before developer can commit,
..      otherwise open new issue(s) for failed tests. These "smoke tests" will be executed in each
..      developer's normal development environment.
..    * Execute unit tests completely on each release candidate to check for regressions. These
..      regression tests will be executed on a dedicated QA machine.
..    * Update unit tests whenever requirements change
.. 
.. 4. System tests
.. 
..    * Design and specify a detailed manual test suite.
..    * Review the system test suite to make sure that every UI screen and element is covered
..    * Execute system tests completely on each release candidate. These system tests will be carried
..      out on a dedicated QA machine.
..    * Update system tests whenever requirements change
.. 
.. 5. QA Management
.. 
..    * Update this test plan whenever requirements change
..    * Document test results and communicate them to the entire development team
..    * Estimate remaining (not yet detected) defects based on current issue tracking data, defect
..      rates, and metrics on code size and the impact of changes.
..    * Keep all issues up-to-date in an issue tracking database. The issue tracker is available to all
..      project members here. The meaning of issue states, priorities, and other attributes are defined
..      in the SDM.

QA-Plan Checklist
=================

.. question:: Do the selected activities in the QA Strategy provide enough assurance that the
   project will meet it's quality goals?

.. Yes, if all activities are carried out as planned, we are confident that the quality goals will
.. be satisfied. We will, of course, adjust this plan as needed.
.. No, this plan leaves open several quality risks that have been noted in the Risk Management
.. section of the Project Plan.

.. question:: Have human resources been allocated to carry out the QA activities?

.. Yes, human resources have been allocated. They are listed in the Resource Needs document.
.. No, human resources have not been allocated. They are listed as "pending" in the Resource Needs
.. document.

.. question:: Have machine and software resources been allocated as needed for the QA activities?

.. Yes, the QA team will use desktop machines and servers that are already allocated to them.
.. Yes, a QA Lab has been set up. The needed machine and software resources are listed in the
.. Resource Needs document.
.. No, needed machine and software resources are listed as pending in the Resource Needs document.

.. question:: Has this QA Plan been communicated to the development team and other stakeholders?

.. Yes, everyone is aware of our prioritized quality goals for this release and understands how
.. their work will help achieve those goals. Feedback is welcome.
.. Yes, this document is being posted to the project website. Feedback is welcome.
.. No, some developers are not aware of the quality goals and planned QA activities for this
.. release. This is a risk that is noted in the Risk Management section of the Project Plan.