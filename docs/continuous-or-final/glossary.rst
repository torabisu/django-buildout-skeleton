========
Glossary
========

.. glossary::

   Chipping away
      The process of removing sample text from templates when that text does not apply to the
      current project. Often some of the sample text will be kept or revised to fit the current
      project. Even if the sample text does not fit the current project, it provides a reusable
      example of how to phrase that type of description. The term "chipping away" comes from an old
      joke: when a sculptor is asked how he carved a marble statue of a horse, he replies "It was
      easy, I just started with a big block of marble and chipped away everything that did not look
      like a horse."

   Attached worksheet
      The idea is similar to filling in an IRS form and using worksheets to calculate subtotals or
      make specific decisions. That is to say, there is a hierarchy to the templates: there are the
      main templates, and then worksheets for specific topics. We have divided the information into
      several files so that each file is focused on one topic, and so that each file can be worked
      on by one person in a reasonable amount of time.

   Process impact
      The process impact box on each template explains where the current template fits into the
      software development process. It usually includes a brief comment on who should create the
      document, and who would be expected to make use of it. You can change the process impact box,
      but you should not need to.

   Checklist
      There are two kinds of checklists:

      * Many of the templates have a section with questions that help you check your work in that
        template. Often the sample answers to the questions prompt you to take some corrective
        action.

      * For design and code review meetings, there are links to guidelines and checklists that help
        you identify common errors in those artifacts.

   Sticky note
      The idea is similar to a post-it note attached to a document that tells you do "sign here" or
      fill in a certain part. There are two types of sticky notes:

      TODO: Instructs you on how to fill in the template. This is the minimum that you need to do.
      One of the main goals of ReadySET is to help your team quickly carry out basic software
      engineering activities. The TODO sticky notes make that easy by making the templates more
      self-explanatory.

      TIP: Helps you think of better ways to fill in the template. One of the other main goals of
      ReadySET is to help your team make better decisions that can make your whole project more
      successful. The TIP sticky notes help with that.

      After you have done what the sticky note says, you can delete the sticky note. In the HTML
      file, they are marked with class="todo" or class="tip".

   API (Application Program Interface)
      An API is a set of functions that one software component makes available to other software
      components. That allows other programs to "call" this program via direct function calls, or
      more indirect communications such as SOAP messages.

   SOAP (Simple Object Access Protocol)
      SOAP is the message format used by standard web services. It entails sending an XML document
      to a server in order to invoke an operation on the server-side. More information on SOAP.

   Change Control Board (CCB)
      A group of people who review proposed changes to the project requirements and/or source code
      to accept or reject changes in each particular release. Proposed changes are usually rejected
      if they introduce too much risk or would trigger additional effort (e.g., the need to redo a
      lot of testing on new code). A CCB is usually composed of managers and representatives of
      other stakeholders such as the QA group and key customers.

   Feature Complete
      A release is called "feature complete" when the development team agrees that no new features
      will be added to this release. New features may still be suggested for later releases. More
      development work needs to be done to implement all the features and repair defects.

   Code Complete
      A release is called "code complete" when the development team agrees that no entirely new
      source code will be added to this release. There may still be source code changes to fix
      defects. There may still be changes to documentation and data files, and to the code for test
      cases or utilities. New code may be added in a future release.

   Internal Release Number
      An internal release number is the number that the development team gives each release.
      Internal release numbers typically count up logically, i.e., they do not skip numbers. They
      may have many parts: e.g., major, minor, patch-level, build number, RC number.

   External Release Number
      External release numbers are the numbers that users see. Often, they will be the same as the
      internal release number. That is especially true if the product being built is a component
      intended to be reused by another engineering group in the same development organization.
      External release numbers can be different for products that face competition. External release
      number are simpler, and may not count up logically. E.g., a certain major ISP jumped up to
      version 8 of their client software because their competition had released version 8. Later,
      the competition used version "10 Optimized" rather than "10.1" or "11".

   Release Number
      The term "release number" by itself refers to an external release number. Users normally are
      not aware of the existence of any internal release numbers.

   Feature specification
      A feature specification focuses on one feature of a software product and completely describes
      how that feature can be used. It includes a brief description of the purpose of the feature,
      the input and output, and any constraints. Individual bullet items give precise details on all
      aspects of the feature. One feature may be used in many different ways as part of many
      different use cases.

   Use case
      The main part of a use case is a set of steps that give an example of how an actor can use the
      product to succeed at a goal. These steps are called the "Main success scenario", and they
      include both user intentions and system responses. One use case may show how the actor uses
      several features to accomplish a goal.

   Actor
      A user or an external system that uses the system being built.

   Correctness
      This design correctly matches the given requirements.

   Feasibility
      This design can be implemented and tested with the planned amount of time and effort.

   Understandability
      Developers can understand this design and correctly implement it.

   Implementation phase guidance
      This design divides the implementation into components or aspects that can correspond to
      reasonable implementation tasks.

   Modularity
      Concerns are clearly separated so that the impact of most design changes would be limited to
      only one or a few modules.

   Extensibility
      New features or components can be easily added later.

   Testability
      It is easy to test components of this design independently, and information is available to
      help diagnose defects.

   Efficiency
      The design enables the system to perform functions with an acceptable amount of time, storage
      space, bandwidth, and other resources.

   Ease of integration
      The components will work together.

   Capacity matching
      The architecture deploys components onto machines that provide needed resources with
      reasonable total expense.

   Expressiveness
      It allows for storage of all valid values and relationships

   Ease of access
      Application code to access stored data is simple

   Reliability
      Stored data cannot easily be corrupted by defective code, concurrent access, or unexpected
      process termination

   Data capacity
      The system can store the amount of data needed.

   Data security
      Protection of sensitive user and corporate data from unauthorized access or modification

   Performance
      Data can be accessed quickly

   Interoperability
      The database or data files can be accessed and updated by other applications

   Intrusion prevention
      Prevent, e.g., hackers opening a command shell on our server.

   Abuse prevention
      Prevention of abuse (e.g., using our system to send spam).

   Auditability
      All changes can be accounted for later.

   Understandability and learnability
      Users can reasonably be expected to understand the UI at first sight. Users will be able to
      discover additional features without aid from other users or documentation, and they will be
      able to recall what they have learned.

   Task support and efficiency
      The UI is well matched to the users' tasks and it can be used with a reasonable number of
      clicks and keystrokes.

   Safety
      Users are not likely to accidentally produce an undesired result (e.g., delete data, or send a
      half-finished email).

   Consistency and familiarity
      Users can apply their knowledge of similar UIs or UI standards to this system.

   Bug
      n. Deprecated since 1991. See defect.

   Error
      v. A mistaken thought in the developer's mind. Often caused by miscommunication or bad
      assumptions. Errors can create defects. E.g., a developer might erroneously think that the
      square root of -4 is -2.

   Defect
      n. The result of the developer's error embodied in the product source code, initial data, or
      documents. E.g., a square root function which allows negative numbers as arguments is
      defective. Defects can be removed by changing the source code, initial data, or document.

   Fault
      n. The execution of defective code. E.g., if a certain input is provided to defective code, it
      may cause an exception, or go into an infinite loop, or store an incorrect value in an
      internal variable. A fault is not normally visible to users, only the failure is visible.

   Failure
      n. The user-visible result of a fault. E.g., an error message or an incorrect result. This is
      evidence that can be reported in a defect report. Developers use failure evidence during
      debugging to eventually find and remove defects.

   Functionality > Correctness
       Correctness is the most basic quality goal. It means that, when valid inputs are given and
       the system is in a valid state and under reasonable load, the system's behavior and results
       will be correct.

   Functionality > Robustness
      Robustness is the system's ability to gracefully handle invalid inputs. It should never be
      possible for any user input to crash the system or corrupt data, even if that user input is
      abnormal, unexpected, or malicious.

   Functionality > Accuracy
      Accuracy refers to the mathematical precision of calculations done by the system. Any system
      that does numeric calculations must consider accuracy, e.g., financial or scientific
      applications.

   Functionality > Compatibility
      Systems that claim to follow standards or claim compatibility with existing systems must
      adhere to the relevant file formats, protocols, and APIs. The relevant standards are linked at
      the top of this document.

   Functionality > Factual correctness
      Is the data in the system a true representation of the real world? Any system that contains
      initial data or gathers data about the real world should be sure that the data is factually
      correct. E.g., a tax preparation program should embody correct and up-to-date facts about tax
      law.

   Usability > Understandability and Readability
      Users need to understand the system to use it. The basic metaphor should be understandable and
      appropriate to user tasks. Some defects in understandability include unclear metaphors, poor
      or hard-to-see labels, lack of feedback to confirm the effects of user actions, and missing or
      inadequate on-line help.

   Usability > Learnability and Memorability
      Every user interface contains some details that users will need to learn and remember. E.g.,
      Alt-F to open the "File" menu. UI cues and rules can make these details easier to learn and
      remember. E.g., the "F" is underlined and, as a rule, the first letter is usually the
      accelerator key.

   Usability > Task support
      This is the quality of match between user tasks and the system's UI. Task support defects are
      cases where the system forces the user to take unnatural steps to accomplish a task or where
      the user is given no support for a difficult step in a task. E.g., must the user invent an
      8-character filename for their "Christmas card list"? E.g., must users total their own tax
      deductions?

   Usability > Efficiency
      Users should be able to accomplish common tasks with reasonable effort. Common tasks should be
      possible with only one or two steps. The difficulty of each step should also be considered.
      E.g., does the user have to remember a long code number or click on a very small button?

   Usability > Safety
      Humans are error-prone, but the negative effects of common errors should be limited. E.g.,
      users should realize that a given command will delete data, and be asked to confirm their
      intent or have the option to undo.

   Usability > Consistency and Familiarity
      Users should be able to apply their past experience from other similar systems. This means
      that user interface standards should be followed, and common conventions should be used
      whenever possible. Also, UI elements that appear in several parts of the UI should be used
      consistently, unless another UI quality takes priority. E.g., if most currency entry fields do
      not require a dollar-sign, then one that does demand it is a consistency defect, unless there
      is a real chance that the user is dealing with another currency on that step in his/her task.

   Usability > Subjective satisfaction
      Users should feel generally satisfied with the UI. This is a subjective quality that sums up
      the other user interface qualities as well as aesthetics.

   Security
      The system should allow usage only by authorized users, and restrict usage based on
      permissions. The system should not allow users to side-step security rule or exploit security
      holes. E.g., all user input should be validated and any malicious input should be rejected.

   Reliability > Consistency under load
      Every system has some capacity limits. What happens when those limits are exceeded? The system
      should never lose or corrupt data.

   Reliability > Consistency under concurrency
      Systems that allow concurrent access by multiple users, or that use concurrency internally,
      should be free of race conditions and deadlock.

   Reliability > Availability under load
      Every system has some capacity limits. What happens when those limits are exceeded? The system
      should continue to service those requests that it is capable of handling. It should not crash
      or stop processing all requests.

   Reliability > Longevity
      The system should continue to operate as long as it is needed. It should not gradually use up
      a limited resource. Example longevity defects include memory leaks or filling the disk with
      log files.

   Efficiency
      The system's operations should execute quickly, with reasonable use of machine and network
      resources. E.g., if one user does one operation, it should execute efficiently.

   Scalability
      Scalability is a general quality that holds when the system continues to satisfy its
      requirements when various usage parameters are increased. E.g., a file server might be
      scalable to a high number of users, or to very large files or very high capacity disks.
      Several specific scalability goals are listed below.

   Scalability > Performance under load
      This is a specific type of scalability goal dealing with the performance of the system at
      times when it is servicing many requests from many users.

   Scalability > Large data volume
      This is a specific type of scalability goal dealing with the ability for the system to handle
      large data sets. Operations should continue to be correct and efficient as data set size
      increases. Furthermore, the user interface should still be usable as the data presented to
      users increases in length.

   Operability
      The long-term needs of system administrators should be reliably supported. E.g., is the system
      easy to install? Can the administrator recover from a crash? Is there sufficient log output to
      diagnose problems in the field? Can the system's data be backed up without downtime? Can the
      system be upgraded practically?

   Maintainability > Understandability
      Will it be easy for (future) developers to understand how the system works?

   Maintainability > Evolvability
      Can the system easily be modified and extended over time?

   Maintainability > Testability
      Can the system easily be tested? Do the requirements precisely specify possible inputs and the
      desired results? Can the system be tested in parts? When failures are observed, can they be
      traced back to defects in specific components (i.e., debugging)? Is testing practical with the
      available testing tools?