==============
User Interface
==============

Overview
========

.. todo:: Answer the questions below to help you design the user interface features of your system.
   Some example text is provided. Add or delete text as needed.

.. question:: What are the most important facts that a developer should know about the user
   interface of this system?

.. PARAGRAPH OR BULLETS

.. question:: What are the ranked goals for the user interface of this system?

.. 1. Understandability and learnability
.. 2. Task support and efficiency
.. 3. Safety
.. 4. Consistency and familiarity

Metaphors, Exemplars, and Standards
===================================

.. question:: What is the central metaphor of this UI design?

.. PARAGRAPH

.. question:: What existing systems have user interfaces similar to the UI you want to build? What
   specific aspects are similar?

.. * amazon.com: Our e-commerce site will have stores and departments, and search like this site.
.. * Microsoft Office: We will use configurable toolbars the same way Office 2000 does.
.. * EXISTING-UI: DESCRIPTION

.. question:: What UI design standards, guidelines, and styles are you following?

.. * Microsoft UI guidelines
.. * Java UI guidelines
.. * Mac UI guidelines
.. * W3C Accessibility guidelines

Task Models
===========

.. question:: What types of users will use this system?

.. See the user needs document.

.. question:: What types of tasks will those users perform?

.. See the use case suite.

Content Model / Interaction Contexts
====================================

.. todo:: List interaction contexts. Each interaction context is a "place" where users see
   information and where they select commands or options. In a graphical user interface, a
   interaction context will eventually be implemented as a window or dialog box. In other
   applications, an interaction context may be implemented as, e.g., a web page, a voice menu
   prompt, or a physical control panel.

.. note:: Each interaction context is an exclusive mode: the user can only use one interaction
   context at a time. All the components within one context are visible and usable at the same time.
   E.g., if a window has three tabs, that is three interaction contexts because only one tab can be
   used at a time.

.. todo:: For each interaction context, list the abstract components within that context. Each
   component is a piece of information, or a user interface affordance. In a GUI, each abstract
   component will eventually become a widget, but the choice of specific widgets happens later.
   Choice of abstract components corresponds to step 2 in the HTML prototyping example demonstrated
   in class.

.. note:: Most high frequency use cases should be carried out in only one interaction contexts. A
   use case that requires three interaction contexts could be hard to use. However, interaction
   contexts with too many components can also be hard to use.

+---------------------+---------+-----------------------------------+
| Interaction Context | Purpose | Contents / Constraints / Behavior |
| --Abstract UI       |         |                                   |
| Components          |         |                                   |
+=====================+=========+===================================+
|                     |         |                                   |
+---------------------+---------+-----------------------------------+

Technical Constraints / Operational Contextualization
=====================================================

.. question:: What are your assumptions about the output devices?

.. We assume that the user has a 17-inch or larger screen with 1024x768 pixels that can display
.. thousands of colors (16 bit or more). We assume basic audio that can play simple sound files.

.. We make very few assumptions about the user's screen or web browser, other than the assumption that
.. they can view page somehow. We will not use any audio features.
.. 
.. This "pay-at-the-pump" system has a 320x200 16-color display and can beep.

.. question:: What are your assumptions about the input devices that you will use?

.. We assume only that the user has a standard keyboard and mouse.
.. This "pay-at-the-pump" system has digits 0-9, "OK", "Cancel", and four menu buttons along the
.. right-hand edge of the screen.

.. question:: What are your assumptions about the amount of time users will spend on tasks?

.. Use cases UC-02 and UC-04 are expected to take a few minutes each. Use case UC-00 should take less
.. than 5 seconds each. All other use cases should take less than 30 seconds each.

.. question:: What windowing systems, UI libraries, or other UI technologies will you use?

.. Standard Java Swing with no extra libraries.
.. Simple HTML and CSS with simple GIF images.

User Interface Checklist
========================

.. todo:: Answer the following questions to help evaluate the design. You may add or remove
   questions to fit your project.

Understandability and learnability
----------------------------------

.. question:: Are there any labels of icons that are likely to be misunderstood?

.. 1-3 SENTENCES

.. question:: Is the user's current place and state clearly visible? E.g., wizard step 2 of 5, or
   edit-mode vs. play-mode.

.. 1-3 SENTENCES

.. question:: Are advanced options clearly separated from the most commonly used options?

.. 1-3 SENTENCES

.. question:: Are there no invisible options or commands? E.g., hold down the control key when
   opening a dialog box to see advanced options.

.. 1-3 SENTENCES

Task Support and Efficiency
---------------------------

.. question:: Which use cases force the user to work through more than two interaction contexts?

.. 1-3 SENTENCES

.. question:: Which use cases force the user to perform slow or difficult UI steps? E.g., entering a
   long code number like an ISBN. E.g., long mouse-drag operations.
   
.. 1-3 SENTENCES

Safety
------

.. question:: Are there any dangerous or irreversible actions that are done with only one step?

.. 1-3 SENTENCES

Consistency and Familiarity
---------------------------

.. question:: Do UI elements in your system work the same as they do in the existing example systems
   you identified?

.. 1-3 SENTENCES

.. question:: Do all elements in your system that appear the same, actually function the same?

.. 1-3 SENTENCES

.. question:: Do all elements in your system that appear the same, actually function the same?

.. 1-3 SENTENCES

.. question:: Are all elements share consistent visual characteristics such as font and color
   scheme, unless there is a reason for them to differ?

.. 1-3 SENTENCES

.. question:: Are labels used consistently throughout the system? E.g., not "forward/back" in some
   contexts and "next/prev" in others.
   
.. 1-3 SENTENCES