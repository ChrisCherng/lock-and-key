# Lock & Key Escape Rooms

[Lock & Key Escape Rooms on Heroku](https://lock-and-key-escape.herokuapp.com/)

![The homepage of Lock & Key](https://res.cloudinary.com/chris-cherng/image/upload/v1663594264/Escape%20Room/ReadMe%20Images/main_xuqqjt.png)

This is the website for Lock & Key Escape rooms providing information on the escape room experiences on offer and allowing users to make a booking for a game.

An administration dashboard allows the administrators to create, amend and delete the information on each room, view bookings that have been made, and view any contact requests from users.

# Business

The Business goals describe the expected user and site owner goals - these drive the design, development, and deployment of the website application. The fulfilment of these goals determine the success of the application.

## External Users

The external users are potential and actual customers of the escape room. They are looking for information on the various rooms being offered at Lock & Key, as well as the ability to book a room.

## Site Owner

The site owners are looking to attract potential customers and be able to manage customer bookings and contact requests in order to engage to the users.

# User Stories

The following user stories have been created to ensure the goals of the users and owner are met.

| User Story | Goal |
| --- | --- |
| **User Story 001:** As a site user I want to be able to view the different escape rooms offered so that I can assess my options. | Finding information on the escape rooms |
| **User Story 002:** As a site user I want to be able to view more details about each room so that I can find out more. | Finding information on the escape rooms |
| **User Story 003:** As a site user I want to be able to contact the site owner so that I can ask any questions. | Finding information on the escape rooms |
| **User Story 004:** As a site user I want to be able to view which rooms are available to book. | Ability to book a room |
| **User Story 005:** As a site user I want to be able to book an escape room on an available date and time. | Ability to book a room |
| **User Story 006:** As a site owner I want to be able to manage the escape room information to ensure it is up to date. | Attract potential customers |
| **User Story 007:** As a site owner I want to be able to manage bookings for the escape room in order to plan for upcoming customers. | Manage customer bookings |
| **User Story 008:** As a site owner I want to be able to manage and view contact requests so that relevant action can be taken. | Manage contact requests |

The implementation of these user stories was managed using Trello (see Documentation Tools below).

# Features

Below is a summary of the features on the Lock & Key Escape Rooms website, split between users and administrators.

## Users

A user is a (potential) customer for Lock & Key. There is no requirement for the user to make an account or sign-in as this may discourage any potential customer from making an enquiry or booking.

- All pages in the public site (i.e. not the administration site) include:
    - a navigation bar displaying the name of the company, along with links to contact the administrators and book a room.
    ![The navigation bar with "Lock & Key" and links to contact and book](https://res.cloudinary.com/chris-cherng/image/upload/v1663592973/Escape%20Room/ReadMe%20Images/navigation_dq6gnr.png)

    - a footer with the business address and social media links.
    ![The footer with the company address, links to social media, and copyright information](https://res.cloudinary.com/chris-cherng/image/upload/v1663592967/Escape%20Room/ReadMe%20Images/footer_wudad0.png)

- All pages are responsive to difference devices including mobile, tablet and desktop.
- Home Page with:
    - introductory information.
    ![The homepage showing the introductory messages](https://res.cloudinary.com/chris-cherng/image/upload/v1663592974/Escape%20Room/ReadMe%20Images/homepage_yd0zei.png)

    - a list of all currently available escape rooms with a summary of what each one is about.
    ![The homepage showing two available rooms](https://res.cloudinary.com/chris-cherng/image/upload/v1663592974/Escape%20Room/ReadMe%20Images/homepage-room-cards_obt8if.png)

- Room Detail pages for each available room with:
    - a more detailed description of the room.
    - a link to the booking page.
    ![The detailed page for Medieval Madness with additional description and booking button](https://res.cloudinary.com/chris-cherng/image/upload/v1663593349/Escape%20Room/ReadMe%20Images/detail-page_zxf7ux.png)

- Contact Page with:
    - a form to contact the site administrators.
    ![The contact form](https://res.cloudinary.com/chris-cherng/image/upload/v1663594011/Escape%20Room/ReadMe%20Images/contact-page_qq1dej.png)

- Booking Page with:
    - a form to complete the relevant information for the booking.
    - a list of times for the selected day and room which are and are not available to book.
    ![The booking form](https://res.cloudinary.com/chris-cherng/image/upload/v1663594015/Escape%20Room/ReadMe%20Images/booking-form_gsdg3y.png)

## Administrators

An administrator is a manager of Lock & Key Escape Rooms. This requires the use of a superuser account username and password, as this is no public-facing information.

- [Administration Page](https://lock-and-key-escape.herokuapp.com/admin/) with:
    - the ability to create, view, update and delete the escape room information visible on the public site.
    ![an image of the rooms admin page](https://res.cloudinary.com/chris-cherng/image/upload/v1663592366/Escape%20Room/ReadMe%20Images/admin-rooms_ibjaow.png)

    - the ability to create, view, update and delete the bookings that have been made by users.
    ![an image of the bookings admin page](https://res.cloudinary.com/chris-cherng/image/upload/v1663592366/Escape%20Room/ReadMe%20Images/admin-bookings_igvfyg.png)

    - the ability to view and delete any contact requests from users from the contact form.
    ![an image of the contact request admin page](https://res.cloudinary.com/chris-cherng/image/upload/v1663592366/Escape%20Room/ReadMe%20Images/admin-contact_dphbsy.png)

# Technology

## Key Technology Used

The following key technologies and languages have been used as part of this website:

- [HTML 5](https://en.wikipedia.org/wiki/HTML): HyperText Markup Language, the standard markup language for documents designed to be displayed in a web browser
- [CSS 3](https://en.wikipedia.org/wiki/CSS): style sheet language used for describing the presentation of a document
- [JavaScript](https://www.javascript.com/): high-level, often just-in-time compiled language
- [jQuery](https://jquery.com/): JavaScript library
- [Python](https://www.python.org/): high-level, general-purpose programming language
- [Django](https://www.djangoproject.com/): Python-based open-source web framework
- [Postgresql](https://www.postgresql.org/): open-source database to hold back-end data
- [GitHub](https://github.com/): code repository
- [GitPod](https://www.gitpod.io/): integrated development environment (IDE)
- [Heroku](https://www.heroku.com/): deployment of the website and application

## Other Technology Used

Other third-party features have been utilised within this project as follows:

- [Google Icons](https://developers.google.com/fonts/docs/material_icons)
- [Materialize CSS](https://materializecss.com/)
- [Font Awesome](https://fontawesome.com/)
- [Summernote](https://summernote.org/): text editor for the admin view for rooms
- [Cloudinary](https://cloudinary.com/): media hosting
- [Whitenoise](http://whitenoise.evans.io/en/stable/): used to bring static files into Heroku deployed application

## Documentation Tools

### Trello Board

A Trello board was used to assist with the organisation of building the website. This included the user stories representing the key features that should be implemented. These were sorted into the following lists:

- To Do: features where no progress had been started.
- In Progress: features where progress has commenced, but not completed.
- Done: features that have been fully implemented.

![Image of Trello](https://res.cloudinary.com/chris-cherng/image/upload/v1663589179/Escape%20Room/ReadMe%20Images/trello_ln2jm3.png)

Each user story started in the To Do list, and was moved through to In Progress and Done as development continued. This assisted with ensuring the work was performed in an organised manner.

### Google Sheets

Google Sheets was used to assist with mapping out the data models:

![Google sheets with three tables for the different data models](https://res.cloudinary.com/chris-cherng/image/upload/v1663594518/Escape%20Room/ReadMe%20Images/models_qoewju.png)

# Testing

## Manual Testing

Manual use cases have been run to test the functionality of the website.

The tables below show the user stories, the associated use cases, the task script followed for the test, and whether this passed or failed. These have been split by user-related and owner-related functionality.

### User Testing

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 001:** As a site user I want to be able to view the different escape rooms offered so that I can assess my options. | PASS |
| + > **Use Case 001-001 (R in CRUD):** As a site user I want to be able to view a list of the escape rooms available. | PASS |
| + + + > **Task 1:** Open the home page -> scroll to the "Our Rooms" section -> the rooms should be visible in cards showing the room names | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 002:** As a site user I want to be able to view more details about each room so that I can find out more. | PASS |
| + > **Use Case 002-001 (R in CRUD):** As a site user I want to be able to select from a list of escape rooms. | PASS |
| + + + > **Task 1:** Open the home page -> scroll to the "Our Rooms" section -> the rooms should be visible in cards with a link for further information | PASS |
| + + + > **Task 2:** Navigate to the room cards from Task 1 -> click on the "More Info" button on one of the rooms -> a new page should open with additional information | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 003:** As a site user I want to be able to contact the site owner so that I can ask any questions. | PASS |
| + > **Use Case 003-001:** As a site user I want to be able to navigate to a contact page. | PASS |
| + + + > **Task 1:** Open the home page -> click "Contact Us" in the navigation bar -> a page titled "Get in Touch" with a contact form should be visible. | PASS |
| + > **Use Case 003-002 (C in CRUD):** As a site user I want to be able to send a message to the site owner. | PASS |
| + + + > **Task 1:** Open the home page -> click "Contact Us" in the navigation bar -> fill in the "name", "email" and "message" fields -> click submit -> a confirmation message should be visible | PASS |
| + > **Use Case 003-003:** As a site user I want the contact form to only submit if I have provided the correct information, to ensure my query can be responded to. | PASS |
| + + + > **Task 1:** Open the home page -> click "Contact Us" in the navigation bar -> fill in the "email" and "message" fields, omitting the "name" field -> click submit -> a prompt should appear to say the "name" field must be completed. | PASS |
| + + + > **Task 2:** Open the home page -> click "Contact Us" in the navigation bar -> fill in the "name" and "message" fields, omitting the "email" field -> click submit -> a prompt should appear to say the "email" field must be completed. | PASS |
| + + + > **Task 3:** Open the home page -> click "Contact Us" in the navigation bar -> fill in the "name" and "email" fields, omitting the "message" field -> click submit -> a prompt should appear to say the "message" field must be completed. | PASS |
| + + + > **Task 4:** Open the home page -> click "Contact Us" in the navigation bar -> fill in the "name"and "message" fields -> in the "email" field, add text that does not include the "@" symbol (i.e. not a valid email address) -> click submit -> a prompt should appear to say the "email" field is incorrect. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 004:** As a site user I want to be able to view which rooms are available to book. | PASS |
| + > **Use Case 004-001 (R in CRUD):** As a site user I want to be able to see times for a given room on a given date. | PASS |
| + + + > **Task 1:** Open the home page -> click "Book Now" in the navigation bar -> select a date -> select a room from the dropdown menu -> a list of possible times should appear. | PASS |
| + + + > **Task 2:** Open the home page -> scroll to the "Our Rooms" section -> select "More Info" on any room -> click "Book Now" in the room details page -> select a date -> select a room from the dropdown menu -> a list of possible times should appear. | PASS |
| + > **Use Case 004-002 (R in CRUD):** As a site user I want any times that have already been booked for a given date and room to be disabled for bookings. | PASS |
| + + + > **Task 1:** Open the home page -> click "Book Now" in the navigation bar -> select a date -> select a room from the dropdown menu -> a list of possible times should appear -> select one of the times -> complete the "name" and "email" fields -> click submit -> repeat these steps and the booked slot should be grey and unclickable. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 005:** As a site user I want to be able to book an escape room on an available date and time. | PASS |
| + > **Use Case 005-001:** As a site user I want to be able to view the booking page. | PASS |
| + + + > **Task 1:** Open the home page -> click "Book Now" in the navigation bar -> select a date -> the booking page should appear. | PASS |
| + + + > **Task 2:** Open the home page -> scroll to the "Our Rooms" section -> select "More Info" on any room -> click "Book Now" in the room details page -> select a date -> the booking page should appear. | PASS |
| + > **Use Case 005-002 (C in CRUD):** As a site user I want to be able to make a booking. | PASS |
| + + + > **Task 1:** Open the home page -> click "Book Now" in the navigation bar -> select a date -> select a room from the dropdown menu -> a list of possible times should appear -> select one of the times -> complete the "name" and "email" fields -> click submit -> a "thank you for booking" page should be visible. | PASS |
| + > **Use Case 005-003:** As a site user I want the booking form to only submit if I have provided the correct information, to ensure an accurate booking. | PASS |
| + + + > **Task 1:** Open the home page -> click "Book Now" in the navigation bar -> select a date and click Next -> select a room from the dropdown -> fill in the "email" field, omitting the "name" field -> click submit -> a prompt should appear to say the "name" field must be completed. | PASS |
| + + + > **Task 2:** Open the home page -> click "Book Now" in the navigation bar -> select a date and click Next -> select a room from the dropdown -> fill in the "name" field, omitting the "email" field -> click submit -> a prompt should appear to say the "email" field must be completed. | PASS |
| + + + > **Task 3:** Open the home page -> click "Book Now" in the navigation bar -> select a date and click Next -> select a room from the dropdown -> fill in the "name" field -> in the "email" field, add text that does not include the "@" symbol (i.e. not a valid email address) -> click submit -> a prompt should appear to say the "email" field is incorrect. | PASS |

### Admin Testing

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 006:** As a site owner I want to be able to manage the escape room information to ensure it is up to date. | PASS |
| + > **Use Case 006-001 (R in CRUD):** As a site owner I want to be able to view the escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display. | PASS |
| + > **Use Case 006-002 (U in CRUD):** As a site owner I want to be able to amend the escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the title field -> click save -> go back into that room information to see the updated title -> check the website that the room has been updated with the new name | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the slug field -> click save -> go back into that room information to see the updated slug -> check the website that the room has been updated with the new slug in the URL | PASS |
| + + + > **Task 3:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the room description field -> click save -> go back into that room information to see the updated description -> check the website that the room has been updated with the new description | PASS |
| + + + > **Task 4:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> change the image field -> click save -> go back into that room information to see the updated image name -> check the website that the room has been updated with the new image on both the homepage and the room detail page | PASS |
| + + + > **Task 5:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the excerpt field  -> click save -> go back into that room information to see the updated excerpt -> check the website that the room has been updated with the new excerpt on the homepage | PASS |
| + + + > **Task 6:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the times field - this must be in the format "HH:MM:SS" separated by commas without spaces  -> click save -> go back into that room information to see the updated times -> check the website that the room has been updated with the new times on the booking page | PASS |
| + + + > **Task 7:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the status field -> click save -> go back into that room information to see the updated status -> check the website that the room has been updated with the new status, that is, if it is now set to "Live" it should be visible on the homepage, if set to "Draft" it should be not be visible on the homepage | PASS |
| + > **Use Case 006-003 (C in CRUD):** As a site owner I want to be able to create new escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on the "Add Room" button at the top right of the window -> complete the information for the title, slug, description, image, excerpt and times (times must be in the format "HH:MM:SS" separated by commas without spaces) -> click save -> go back into that room information to see the new room has been created | PASS |
| + + + > **Task 2:** Create a new room as per Task 1 above -> in the admin panel, select the room and update the "Status" field to "Live" -> click save -> check the website that the room is now visible on the homepage | PASS |
| + > **Use Case 006-004 (D in CRUD):** As a site owner I want to be able to delete an escape room in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> tick the box next the room to be deleted -> in the Action dropdown menu, select "Delete selected rooms" -> click Go -> click "Yes, I'm sure" -> check the dashboard that the room is no longer appearing -> if the room had a "Live" status, check that the room is no longer visible on the homepage | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on the room to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check the dashboard that the room is no longer appearing -> if the room had a "Live" status, check that the room is no longer visible on the homepage | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 007:** As a site owner I want to be able to manage bookings for the escape room in order to plan for upcoming customers. | PASS |
| + > **Use Case 007-001 (R in CRUD):** As a site owner I want to be able to view the booking information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details | PASS |
| + > **Use Case 007-002 (U in CRUD):** As a site owner I want to be able to update the booking information in the administrator dashboard (e.g. if a customer requires a change of booking). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the room selected field -> click save -> go back into the booking to see the updated room selected | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the name field -> click save -> go back into the booking to see the updated name | PASS |
| + + + > **Task 3:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the email field -> click save -> go back into the booking to see the updated email address | PASS |
| + + + > **Task 4:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the date -> click save -> go back into the booking to see the updated date selected | PASS |
| + + + > **Task 5:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the time -> update the date -> click save -> go back into the booking to see the updated time selected | PASS |
| + > **Use Case 007-003 (C in CRUD):** As a site owner I want to be able to create a booking in the administrator dashboard (e.g. if certain times need to be blocked off for staff training). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on "Add Booking" in the top right -> fill in the room, name, email, date and time fields (selecting a currently available time) -> set the booking type field to "Management Booked" -> click save -> check that this time for this room is no longer available on the booking page on the website | PASS |
| + > **Use Case 007-004 (D in CRUD):** As a site owner I want to be able to delete a booking in the administrator dashboard (e.g. if a customer contacts to cancel). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> tick on the booking(s) to be deleted -> in the Action dropdown, select "Delete selected bookings" -> click go -> click "Yes, I'm sure" -> check that the booking has been deleted from the list | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on the booking to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check that the booking has been deleted from the list | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 008:** As a site owner I want to be able to manage and view contact requests so that relevant action can be taken. | PASS |
| + > **Use Case 008-001 (R in CRUD):** As a site owner I want to be able to view the contact forms submitted by users in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> click on a contact item to see the details | PASS |
| + > **Use Case 008-002 (D in CRUD):** As a site owner I want to be able to delete contact forms submitted by users in the administrator dashboard (e.g. for spam, or if the request has been actioned). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> tick the form(s) to be deleted -> in the Action dropdown, select "Delete selected contact infos" -> click go -> click "Yes, I'm sure" -> check that the selected forms been deleted from the list | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> click on the form to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check that the selected forms been deleted from the list | PASS |

### "Negative Testing"

Negative testing was undertaken to determine whether the application could handle unwanted or unexpected user input. These tests were included within the following Use Cases:

- Use Case 003-003: As a site user I want the contact form to only submit if I have provided the correct information, to ensure my query can be responded to.
- Use Case 005-003: As a site user I want the booking form to only submit if I have provided the correct information, to ensure an accurate booking.

The tasks performed for these use cases all operated as expected and the tests passed.

### Bugs

TBC

#### Fixed Bugs

- 

## Code Validation

TBC

[W3C HTML Validator](https://validator.w3.org/)

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

[JSHint Validator](https://jshint.com/)

[PEP8 Validator](http://pep8online.com/)

[Python Syntax Checker](https://extendsclass.com/python-tester.html)

# Credits

## Acknowledgements

- [The Code Institute](https://codeinstitute.net/) for their tuition and support throughout.
- [TimeTrap Escape Rooms](https://www.timetrapescaperooms.com/) for permission to use their images.
- [Unsplash](https://unsplash.com/photos/Vp3oWLsPOss) lock image by iMattSmart.
- User "Gaff" on the Code Institute Slack for help with the layout and content of the ReadMe file.