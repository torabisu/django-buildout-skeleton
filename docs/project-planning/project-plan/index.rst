.. _project-plan:

============
Project Plan
============

.. note:: This plan will be used to evaluate and manage the project. Key assumptions that affect
   the plan should be documented here. The project plan should be updated throughout the life-time
   of the project.

.. todo:: Fill in the information above and below. Add or remove rows as needed. Use the worksheet
   to help identify and scope resource needs.

Summary of Project
==================

.. ONE OR TWO SENTENCES HERE. For more information see the Project proposal.
.. 
.. IF YOU PLAN TO ORGANIZE YOUR WORK ACCORDING TO A ROUGH BREAKDOWN OF SOFTWARE COMPONENTS, BRIEFLY
.. DESCRIBE THOSE COMPONENTS HERE. FOUR TO TEN BULLETS.

Summary of Methodology
======================

.. question:: What general development approach will be used?

.. THREE TO FIVE SENTENCES OR BULLETS HERE. COVER GENERAL APPROACH, IMPORTANT ASSUMPTIONS, KEY
.. PRACTICES, AND PROJECT COORDINATION CONTROLS. For more information see the Software Development
.. Methodology.

.. question:: How will the project team be organized?

.. The development team will consist of ...
.. The change control board will consist of ...

.. question:: What development and collaboration tools will be use?

.. We plan to use the following tools extensively through out the project:
.. 
.. * Project website
.. * Project mailing lists
.. * Issue tracking system
.. * Version control system
.. * Automated build system
.. * Automated unit test system

.. question:: How will changes be controlled?

.. * Requests for requirements changes will be tracked in the issue tracker
.. * The change control board (CCB) will review requested changes and authorize work on them as
..   appropriate
.. * After the feature complete milestone, no new features will be added to this release.
.. * After the code complete milestone, no entirely new product source code will be added to this
..   release.
.. * All source code commit log messages must refer to a specific issue ID, after the feature
..   complete milestone.

.. question:: How will this plan be updated?

.. This project plan will be updated as needed throughout the project. It will be placed under
.. version control and instructions for accessing it will be on the project website. Any change to
.. the plan will cause an automatic notification to be sent to a project mailing list.

Work Breakdown Structure and Estimates
======================================

.. todo:: List tasks that will be needed for this project. Keep dividing tasks into subtasks until
   you feel that you have enough detail to expose risks and make reasonable estimates in ideal
   engineering hours.

.. todo:: Label each step uniquely to show its position in the WBS, e.g., Step 1.1.4.A. Use numbers
   for steps that you intend to do in sequence, and use letters for steps that you intend to do in
   parallel. E.g., Step 1.1 comes before Steps 1.2.A and 1.2.B, but those two steps may be done in
   parallel, and Step 1.3 will be done after all 1.2.* steps have been finished. Don't worry about
   renumbering if you delete a step.

.. +--------+--------------------------------------------+----------+
.. | Step   | Description                                | Estimate |
.. +========+============================================+==========+
.. | 1.     | Inception                                  |          |
.. +--------+--------------------------------------------+----------+
.. | 1.1.   | Requirements gathering                     | 30h      |
.. +--------+--------------------------------------------+----------+
.. | 1.2.   | Requirements specification                 | 20h      |
.. +--------+--------------------------------------------+----------+
.. | 1.3.   | Requirements validation                    | 10h      |
.. +--------+--------------------------------------------+----------+
.. | 2.     | Elaboration                                |          |
.. +--------+--------------------------------------------+----------+
.. | 2.1.   | High-level design                          | 5h       |
.. +--------+--------------------------------------------+----------+
.. | 2.2.   | Low-level design (break down by component) |          |
.. +--------+--------------------------------------------+----------+
.. | 2.2.A. | Object design                              | 10h      |
.. +--------+--------------------------------------------+----------+
.. | 2.2.B. | User interface design                      | 10h      |
.. +--------+--------------------------------------+------+
.. | 2.2.C. | Model design                         | 3h   |
.. +--------+--------------------------------------+------+
.. | 2.3.   | Design review and evaluation         | 5h   |
.. +--------+--------------------------------------+------+
.. | 3.     | Construction                         |      |
.. +--------+--------------------------------------+------+
.. | 3.1.   | System implementation                |      |
.. +--------+--------------------------------------+------+
.. | 3.1.A. | Components TBD                       |      |
.. +--------+--------------------------------------+------+
.. | 3.1.Z. | Integrate components                 | 5h   |
.. +--------+--------------------------------------+------+
.. | 3.2.   | Technical documentation              | 10h  |
.. +--------+--------------------------------------+------+
.. | 3.3.   | User documentation                   | 10h  |
.. +--------+--------------------------------------+------+
.. | 3.4.   | Testing                              |      |
.. +--------+--------------------------------------+------+
.. | 3.4.1. | Test planning                        | 10h  |
.. +--------+--------------------------------------+------+
.. | 3.4.2. | Test code implementation             | 30h  |
.. +--------+--------------------------------------+------+
.. | 3.4.3. | Test execution                       | 10h  |
.. +--------+--------------------------------------+------+
.. | 3.5.   | Implementation review and evaluation | 15h  |
.. +--------+--------------------------------------+------+
.. | 4.     | Transition                           |      |
.. +--------+--------------------------------------+------+
.. | 4.1.   | Release packaging                    | 3h   |
.. +--------+--------------------------------------+------+
.. | 4.2.   | Documentation for other groups       | 3h   |
.. +--------+--------------------------------------+------+
.. | 5.     | Reflection                           |      |
.. +--------+--------------------------------------+------+
.. | 5.1.   | Postmortem report                    | 10h  |
.. +--------+--------------------------------------+------+
.. | Total  |                                      | 188h |
.. +--------+--------------------------------------+------+

Deliverables in this Release
============================

.. todo:: List project deliverables in detail, with delivery dates.

.. TODO: Add table

Schedule for this Release
=========================

.. todo:: Make the rows in this table match the steps in your WBS above. If you have a large number
   of detailed steps, you can skip the most detailed ones. The columns of the table represent weeks
   of calendar time. For each cell in the table, enter the number of hours ideal engineering time
   that the team will spend on that task that week. Total your hours across and down.

.. note:: These hours should total to the same as the total of the hours listed in your resource
   needs document. And, the hours for each type of effort resources needed should correspond to the
   sum for each type of task.

.. TODO: Add table

Risk Management
===============

.. todo:: List and rank the major risks of this project, and what you plan to do to mitigate each
   risk. If you don't plan to do anything to mitigate the risk, state that. Use the risk list below,
   or the risks worksheet.
   
.. The main risks of this project are:
.. 
.. 1. There is a potential conflict between the goals of a high-quality appearance and one that is
..    completely customizable. We can only succeed if players find the web site appealing, and game
..    vendors can customize it with no more effort than would be needed to build a static website. We
..    already have a design in mind that will address this risk and we will review it with a web site
..    designer who worked for a game vendor site.
.. 
.. 2. There are significant technical difficulties in building a web site and web application. This
..    will be a risk because one person on our team has much experience with the relevant tools and
..    technologies. Although the others will learn, we will certainly make some mistakes and suboptimal
..    choices. We will address this risk by scoping the project such that we have enough time to train
..    and to review the design and implementation.
.. 
.. 3. The schedule for this project is very short. We will manage this by planning a conservatively
..    scoped functional core and series of functional enhancements that can be individually slipped to
..    later releases if needed.
.. 
.. 4. The performance of the system will be significantly impacted by the decisions made during the
..    database design task. None of our current team members has experience with database optimization.
..    To address this, we will arrange a review meeting with an experienced DBA or hire a consultant
..    from the database vendor.
.. 
.. 5. We could be underestimating known tasks. HOW TO AVOID/MITIGATE?
.. 
.. 6. We could be underestimating the impact of unknown tasks. HOW TO AVOID/MITIGATE?
.. 
.. 7. We could be underestimating the dependencies between tasks. HOW TO AVOID/MITIGATE?
.. 
.. 8. We could have misunderstood the customer's requirements. HOW TO AVOID/MITIGATE?
.. 
.. 9. The customer could change the requirements. HOW TO AVOID/MITIGATE?
.. 
.. 10. We could face major difficulties with the technology chosen for this project. HOW TO
..     AVOID/MITIGATE?
.. 
.. 11. We could have low quality that demands significant rework. HOW TO AVOID/MITIGATE?
.. 
.. 12. We could incorrectly assess our progress until it is too late to react. HOW TO AVOID/MITIGATE?
.. 
.. 13. We could lose resources. E.g., team members could get sick, spend time on other projects, or
..     quit. HOW TO AVOID/MITIGATE?
.. 
.. 14. There may be a mis-alignment of stakeholder goals or expectations. HOW TO AVOID/MITIGATE?

Project Planning Dependencies
=============================

.. question:: Does this project conflict or compete for resources with any other project?

.. No, this is the only project that we are working on.
.. Yes, and we have determined how many hours each person can actually dedicate to this project.

.. question:: Are the same human or machine resources allocated to maintenance of past versions
   and/or planning of future versions during this release time period?

.. No, this is the first release and we will not plan the next release.
.. Yes, we predict that team members will spend an average of 20% of their time maintaining previous
.. releases and planning future releases during this release time frame. Some weeks may be higher if
.. an urgent patch to a previous release is needed.

.. question:: Does this project depend on the success of any other project?

.. No, this project stands alone.
.. Yes, project P1 must provide library L, and project P2 must prove the usability of feature F,
.. and...

.. question:: Does any other project depend on this project?

.. No, project is not producing any components that will be used in other current projects.
.. Yes, we must produce library L for our project and support users of L in projects P1 and P2.

.. question:: Are there any other important dependencies that will affect this project?

.. No, everything is covered above.
.. Yes. DETAILS....