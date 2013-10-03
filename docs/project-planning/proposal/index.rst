.. _project-proposal:

================
Project Proposal
================

.. note:: This proposal, along with drafts of related documents, will be used by management to
   determine whether or not to approve work on this project. A clear and precise project plan helps
   set expectations that will be used later to evaluate the success of the project.

Background and Motivation
=========================

.. todo:: Replace the example text below with text that describes your project. What are the needs
   or problems that you are trying to address? Why do these needs (still) exist? Why are these
   problems worth solving? Who is the customer? Write 2-4 paragraphs.

.. question:: What is the setting and history behind this project?

.. Video games were originally designed and built as stand-alone systems with the user playing
.. against the machine. Although many advances have been made in game AI, humans still tend to enjoy
.. competing against other humans over a network. There is a social aspect to network gaming where
.. people form teams that play and leagues that play at scheduled times and keep scores over a
.. prolonged period.  This is important to video game vendors because it can result in increased
.. revenue and extend the sales life of their products.

.. question:: What is the problem to be addressed?

.. There are 100 million users on the Internet, and hundreds of websites dedicated to video game
.. playing teams, called "clans". If users have to explore to find the good clans that they can
.. join, it takes a lot of their time. There is a need for a faster way for users to find high
.. quality clan websites that interest them and that will allow them to join.

.. question:: What are some current approaches to this problem?

.. Users can tell each other about clan websites, but that is not scalable because it depends on
.. manual steps by people who may not be motivated or honest in their evaluations. There are already
.. some clan directory web sites, but they are not automated so they are always out of date and do
.. not rate the quality of the websites.
.. 
.. * Example of current manually maintained clan website
.. * Link to existing competitor

.. question:: Why is this problem worth solving or worth solving better?

.. A better clan directory service would be valuable because it could greatly increase player
.. satisfaction and allow them to spend more time playing and less time searching. Implementing a
.. better clan directory would cause players to use that website rather than the existing
.. directories.  The benefit to us could come in the form of revenue from advertising and service
.. fees from video game vendors.

.. question:: How will this product be better than previous approaches?

.. We add innovative new features. Our affiliate directory will be larger an more detailed. We will
.. offer built-in tools for managing membership and organizing events such as game nights or
.. tournaments.
.. 
.. Our system will have similar functionality, but it will have much better maintainability,
.. scalability, and security.
.. 
.. Our system will have similar functionality, but it is specifically aimed at a market segment that
.. is not served by competing products.
.. 
.. This is a "me-too" product that will go head-to-head with very similar competing products in the
.. same market. The market is large enough that we can be very happy with a share of it. Our unique
.. competitive advantages are in non-product area of our business such as sales, marketing,
.. partnerships, support, training, etc. The product will have some simple built-in "hooks" that
.. leverage those advantages.

.. question:: Where is there more information on this problem?

.. The following pages provide additional background and motivation:
.. 
.. * Magazine article on this topic
.. * Industry analysis's report on massive-multi-player game market
.. * Quotes from game players

Goal
====

.. question:: What is the goal of this project?

   .. note:: This should be relatively short since you can reference terms defined above.

.. This project will produce an engine for clan directory websites that allows players to quickly
.. find, evaluate, and join clans.

.. question:: What are the defining features and benefits of this product?

.. * Reusable website engine with functionality for creating, editing, deleting, searching,
..   categorizing, browsing, rating, and commenting on clans. This automates all clan operations and
..   ensures that users will always find information that is automatically up-to-date.
.. 
.. * The reusable website engine will have a highly configurable appearance that allows it to match
..   the look and feel of the game. This allows the reusable website engine to have a high-quality
..   appearance that is just as good as existing clan directories.
.. 
.. * The website engine will be secure and only allow users with the proper permissions to edit,
..   delete, or join a clan. This will prevent cheating or the submission of false information.

.. question:: Where are other documents that further explain the goal of this project?

.. * Mock-up
.. * Early user stories
.. * Quotes from potential customers
.. * Comparison to existing competitors
.. * Draft feature list

Scope
=====

.. todo:: Replace the sample text below with a clear statement of the scope of your project. What
   are the high-level things that you plan to do, and that you will not do? What are your important
   simplifying assumptions? Try to guard against reasonable misunderstandings that might arise if
   you did not explain the scope. It can take the form of a paragraph, bullet list, in/out list,
   and/or UML context diagram.

.. We want to focus on the web application itself, and the features of that application that help build
.. a good gaming community.
.. 
.. See the context diagram.
.. 
.. * Work with common servers and browsers that we are already familiar with.
.. * Allow easy customizations of fonts and colors, with the same basic page layout.
.. * Enough security to greatly discourage abuse
.. * The web site content discusses a game, but it will not need to actually integrate with any game
..   software
.. 
.. +------------------------------------------------+-------------------------------------------------+
.. | In Scope                                       | Out of Scope                                    |
.. +================================================+=================================================+
.. | Building a web application for use with        | Building a new web server or application server |
.. | standard web servers and application servers   |                                                 |
.. +------------------------------------------------+-------------------------------------------------+
.. | Working the most popular browsers              | Working with uncommon or outdated browsers      |
.. +------------------------------------------------+-------------------------------------------------+
.. | Security in the form of user accounts,         | Special security against hackers. Finding or    |
.. | passwords, and permissions                     | patching security holes in existing software    |
.. |                                                | components.                                     |
.. +------------------------------------------------+-------------------------------------------------+
.. | One simple sample look-and-feel and            | Our own high-quality look-and-feel. A library   |
.. | instructions for customization                 | of look-and-feel options.                       |
.. +------------------------------------------------+-------------------------------------------------+
.. | Database and server load and data volume that  | Managing a cluster of servers.                  |
.. | can be handled by one computer.                |                                                 |
.. +------------------------------------------------+-------------------------------------------------+
.. | Keeping track of which users are in which      | Tracking all user activity on the site and      |
.. | clans                                          | producing custom reports                        |
.. +------------------------------------------------+-------------------------------------------------+
.. | Displaying advertisements to visitors. Billing | Automatically selecting ads that fit the        |
.. | advertisers for impressions.                   | visitor's interests. On-line management of      |
.. |                                                | advertising or real-time reporting to           |
.. |                                                | advertisers. Participating in existing banner   |
.. |                                                | advertising affiliate networks.                 |
.. +------------------------------------------------+-------------------------------------------------+

Deliverables
============

.. todo:: Briefly list project deliverables. When you are done, what will you deliver to the
   customer? This can be copied from the draft project plan and simplified to reduce technical
   detail.

.. * Clan website directory engine
.. * Customization guide
.. * Sample look-and-feel
.. * On-line help for end users
.. * Command-line advertising configuration tool and report generator

Risks and Rewards
=================

.. todo:: Briefly list and rank major risks. Risks are detailed in the draft project plan. For this
   proposal document, you should select the most important risks from the project plan and explain
   them in non-technical terms.

.. question:: What are the main risks of this project?

.. 1. There is a potential conflict between the goals of a high-quality appearance and one that is
..    completely customizable. We can only succeed if players find the web site appealing, and game
..    vendors can customize it with no more effort than would be needed to build a static website.
..    We already have a design in mind that will address this risk and we will review it with a web
..    site designer who worked for a game vendor site.
.. 
.. 2. There are significant technical difficulties in building a web site and web application. This
..    will be a risk because one person on our team has much experience with the relevant tools and
..    technologies. Although the others will learn, we will certainly make some mistakes and
..    suboptimal choices. We will address this risk by scoping the project such that we have enough
..    time to train and to review the design and implementation.
.. 
.. 3. The schedule for this project is very short. We will manage this by planning a conservatively
..    scoped functional core and series of functional enhancements that can be individually slipped
..    to later releases if needed.

.. question:: What are the main rewards if this project succeeds?

.. If we accomplish the elements of our plan, our clan directory website engine will replace
.. existing clan directory websites and generate traffic which will result in advertising revenue
.. and/or hosting fees paid by game vendors. Our ability to overcome the challenges above will
.. determine time to market, the speed of adoption, the amount of web traffic, and thus the
.. generated revenue over time.

Project Plan
------------

See :ref:`project-plan` and :ref:`resource-needs`.
