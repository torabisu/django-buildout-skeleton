.. _resource-needs:

====================
Human Resource Needs
====================

.. note:: Based on the project plan and the worksheet below, this project will need the following
   resources to meet its goals. If fewer resources are available, the scope of the release should be
   reconsidered or the process must be changed.

.. todo:: Fill in the information above and below. Add or remove rows as needed. Use the worksheet
   to help identify and scope resource needs. These rows are just examples. The total effort listed
   in this example may not even match the totals given in other examples of related documents.
     
+------+----------+--------+--------+-----------------------------+
| Need | Resource | Amount | Status | Comments / Responsibilities |
+======+==========+========+========+=============================+
|      |          |        |        |                             |
+------+----------+--------+--------+-----------------------------+

Capital Needs
=============

+------+----------+--------+--------+-----------------------------+
| Need | Resource | Amount | Status | Comments / Responsibilities |
+======+==========+========+========+=============================+
|      |          |        |        |                             |
+------+----------+--------+--------+-----------------------------+

Possible Status Values
----------------------

* Pending: request is awaiting management decision
* Assigned: task has been assigned to a person in the issue tracker
* Allocated: capital request approved by management, but resource has not arrived
* Satisfied: request is satisfied, resource has arrived
* Rejected: requested resource will not be allocated, plan must be adjusted to work without this
  resource

Resource Needs Checklist
========================

.. The goal of this checklist is to help expose resource needs that might otherwise be missed. It does
.. not help with the actual estimated number of hours needed. Those estimates should be based on the
.. project plan.

.. todo:: Answer the questions below. If multiple sample answers are provided, chip away the ones
   that do not apply. Edit any provided answers as needed. Use this exercise to help you fill in the
   tables above.

.. question:: Does this project need more than a few days work?

.. Yes. A project manager role is needed to oversee the project.
.. No. The developers can manage their own work.

.. question:: Are the requirements already completely defined and validated?

.. Yes. No additional time is needed for requirements.
.. No. Effort is needed for requirements.

.. question:: What aspects of the system need to be designed?

.. General design. Group developer effort needed.
.. User interface. UI designer and domain experts effort needed.
.. Database design. Developer and DBA effort needed.
.. Security design. Developer and topic expert effort needed.
.. Other design. Developer, domain, and/or topic expert effort needed.

.. question:: Does the project plan include any new development?

.. Yes. Development resources are needed.
.. No. No developers are needed

.. question:: Does the project plan include complex configuration of existing components?

.. Yes. Component expert needed. Also need time to coordinate with development and operations teams.
.. No. No component experts are needed

.. question:: Does the development team have knowledge of all tools, components, and technologies to
   be used?

.. Yes. No training time needed.
.. No. Effort needed for training. Need training materials, courses, or time with experts or
.. mentors.
.. List specific training needs individually.

.. question:: Is the entire development team have an agreed upon software development methodology?

.. Yes. No effort needed for defining a methodology.
.. Yes. But, effort is needed to refine the methodology to the project at hand.
.. No. Effort needed to define and document a methodology and train all team members. Additional
.. effort needed for refinements throughout the project.

.. question:: Does the project plan include end-user documentation?

.. Yes. Technical writing resources must be allocated.
.. No.

.. question:: What is the complexity of the internal documentation?

.. Significant. Technical writing resources must be allocated.
.. Average. Developers can produce technical documents as they go.

.. question:: Will the technical support, training, operations, or services groups deal with the
   product of this project?

.. Yes. Effort must be allocated to train the staff in those groups.
.. No, but other developers will need training to reuse this component.
.. No. Effort put into producing good technical documentation should be enough.

.. question:: Will the product of this project be sold to customers, directly or indirectly?

.. Yes. The full SDM must be followed, including effort by a change control board and release
.. engineering.
.. No, it is for internal use only but it will be used repeatedly to help build a shipping product.
.. Release engineering and CCB effort is still needed.
.. No, it is for internal use only and will only be used once. Release engineering and CCB effort
.. not needed.

.. question:: Does the QA plan call for the running of automated unit tests?

.. Yes. Development effort will be needed to implement unit tests.
.. No. Additional QA effort will be needed for manual testing.

.. question:: Does the QA plan call for more than the running of automated unit tests?

.. Yes. QA effort will be needed.
.. No. Unit tests will be enough for this component, full QA can be done on products that use this
.. component.

.. question:: How many development workstations will be needed?

.. 1 per developer.
.. 1 per developer, plus extra for...

.. question:: What development servers are needed?

.. None.
.. One for the whole team.
.. One for the one aspect of development, another for another aspect.
.. One for the one branch of development, another for another branch.

.. question:: What database servers are needed?

.. None. No database is being used.
.. None. Database is integrated into product and does not require a separate server.
.. One for the whole team.
.. One for the developers, one for QA.
.. One for one branch of development, another for another branch.
.. One for the developers, one for QA, one for load testing.
.. One for each developer or tester, plus one for load testing.

.. question:: What machines are needed for automated testing?

.. None. Automated testing will not be done.
.. None. Automated testing will be done on workstations.
.. One for all nightly automated tests.
.. One for one aspect of nightly automated tests, another for another aspect.
.. One for one branch of development, another for another branch.

.. question:: What machines are needed for load testing?

.. None. Load testing will not be done.
.. None. Load testing will be done on workstations.
.. One machine will do all load testing.
.. Several machines needed to act as clients and servers.
.. One cluster of load testing machines for each branch of development.

.. question:: What development tools must be licensed for this project?

.. None. Everything is implemented by us.
.. None. All development tools are open source.
.. Some tools: IDE, database, testing tools. These tools have already been purchased, installed, and
.. configured.
.. Some tools: IDE, database, testing tools. Budget must be allocated to purchase these tools.
.. Effort must be allocated to research and select tools for purchase, install, and configure them.

.. question:: What software components must be licensed for this project?

.. None. Everything is implemented by us.
.. None. All reused components are open source.
.. Some components: database, server software, libraries. These components have already been
.. selected, purchased, installed, and configured.
.. Some components: database, server software, libraries. Effort must be allocated to research,
.. select, install and configure these components. Budget must be allocated to purchase them.

.. question:: Are any of the personnel assignments of capital allocations conditional?

.. Yes. All such conditions are written in the comments column above. We have a contingency plan
.. that will still achieve (an acceptable subset) of the project goals.
.. No. Management has set aside these resources as promised, and the needs of this project will take
.. priority over any other project that is likely to need the same resources.

.. question:: Have these resource assignments been communicated to the people being assigned and
   their managers?

.. Yes, everyone understands. Feedback is welcome.
.. No, this is a risk that is noted in the Risk Management section.
