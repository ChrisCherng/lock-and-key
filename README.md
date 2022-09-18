# Lock & Key Escape Rooms

[Lock & Key Escape Rooms on Heroku](https://lock-and-key-escape.herokuapp.com/)

This is the website for Lock & Key Escape rooms providing information on the escape room experiences on offer and allowing users to make a booking for a game.

An administration dashboard allows the administrators to create, amend and delete the information on each room, view bookings that have been made, and view any contact requests from users.

# Business

The Business goals describe the expected user and site owner goals - these drive the design, development, and deployment of the website application. The fulfilment of these goals determine the success of the application.

## External Users

The external users are potential and actual customers of the escape room. They are looking for information on the various rooms being offered at Lock & Key, as well as the ability to book a room.

## Site Owner

The site owners are looking to attract potential customers and provide a clear, simple website for the users.

# User Experience

## User Stories and Use Cases

# Features

Below is a summary of the features on the Lock & Key Escape Rooms website, split between users and administrators.

## Users

- All pages in the public site (i.e. not the administration site) include:
    - a navigation bar displaying the name of the company, along with links to contact the administrators and book a room.
    - a footer with the business address and social media links.
- Home Page with:
    - introductory information.
    - a list of all currently available escape rooms with a summary of what each one is about.
- Room Detail pages for each available room with:
    - a more detailed description of the room.
    - a link to the booking page.
- Contact Page with:
    - a form to contact the site administrators.
- Booking Page with:
    - a form to complete the relevant information for the booking.
    - a list of times for the selected day and room which are and are not available to book.

## Administrators

- Administration Page with:
    - the ability to create, view, update and delete the escape room information visible on the public site.
    - the ability to create, view, update and delete the bookings that have been made by users.
    - the ability to view and delete any contact requests from users from the contact form.

# Technology

# Testing

## Manual Testing

- Manual use cases have been run to test the functionality of the website.
- The table below shows the user stories, the associated use cases, the task script followed for the test, and whether this passed or failed.

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
| + + + > **Task 1:** Open the home page -> click "Contact Us" in the navigation bar -> fill in the "name", "email" and "message" fields -> click submit | PASS |
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
| **User Story 005:** As a site owner I want to be able to manage the escape room information to ensure it is up to date. | PASS |
| + > **Use Case 005-001 (R in CRUD):** As a site owner I want to be able to view the escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display. | PASS |
| + > **Use Case 005-002 (U in CRUD):** As a site owner I want to be able to amend the escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the title field -> click save -> go back into that room information to see the updated title -> check the website that the room has been updated with the new name | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the slug field -> click save -> go back into that room information to see the updated slug -> check the website that the room has been updated with the new slug in the URL | PASS |
| + + + > **Task 3:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the room description field -> click save -> go back into that room information to see the updated description -> check the website that the room has been updated with the new description | PASS |
| + + + > **Task 4:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> change the image field -> click save -> go back into that room information to see the updated image name -> check the website that the room has been updated with the new image on both the homepage and the room detail page | PASS |
| + + + > **Task 5:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the excerpt field  -> click save -> go back into that room information to see the updated excerpt -> check the website that the room has been updated with the new excerpt on the homepage | PASS |
| + + + > **Task 6:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the times field - this must be in the format "HH:MM:SS" separated by commas without spaces  -> click save -> go back into that room information to see the updated times -> check the website that the room has been updated with the new times on the booking page | PASS |
| + + + > **Task 7:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the status field -> click save -> go back into that room information to see the updated status -> check the website that the room has been updated with the new status, that is, if it is now set to "Live" it should be visible on the homepage, if set to "Draft" it should be not be visible on the homepage | PASS |
| + > **Use Case 005-003 (C in CRUD):** As a site owner I want to be able to create new escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on the "Add Room" button at the top right of the window -> complete the information for the title, slug, description, image, excerpt and times (times must be in the format "HH:MM:SS" separated by commas without spaces) -> click save -> go back into that room information to see the new room has been created | PASS |
| + + + > **Task 2:** Create a new room as per Task 1 above -> in the admin panel, select the room and update the "Status" field to "Live" -> click save -> check the website that the room is now visible on the homepage | PASS |
| + > **Use Case 005-004 (D in CRUD):** As a site owner I want to be able to delete an escape room in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> tick the box next the room to be deleted -> in the Action dropdown menu, select "Delete selected rooms" -> click Go -> click "Yes, I'm sure" -> check the dashboard that the room is no longer appearing -> if the room had a "Live" status, check that the room is no longer visible on the homepage | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on the room to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check the dashboard that the room is no longer appearing -> if the room had a "Live" status, check that the room is no longer visible on the homepage | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 006:** As a site owner I want to be able to manage bookings for the escape room in order to plan for upcoming customers. | PASS |
| + > **Use Case 006-001 (R in CRUD):** As a site owner I want to be able to view the booking information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details | PASS |
| + > **Use Case 006-002 (U in CRUD):** As a site owner I want to be able to update the booking information in the administrator dashboard (e.g. if a customer requires a change of booking). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the room selected field -> click save -> go back into the booking to see the updated room selected | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the name field -> click save -> go back into the booking to see the updated name | PASS |
| + + + > **Task 3:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the email field -> click save -> go back into the booking to see the updated email address | PASS |
| + + + > **Task 4:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the date -> click save -> go back into the booking to see the updated date selected | PASS |
| + + + > **Task 5:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the time -> update the date -> click save -> go back into the booking to see the updated time selected | PASS |
| + > **Use Case 006-003 (C in CRUD):** As a site owner I want to be able to create a booking in the administrator dashboard (e.g. if certain times need to be blocked off for staff training). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on "Add Booking" in the top right -> fill in the room, name, email, date and time fields (selecting a currently available time) -> set the booking type field to "Management Booked" -> click save -> check that this time for this room is no longer available on the booking page on the website | PASS |
| + > **Use Case 006-004 (D in CRUD):** As a site owner I want to be able to delete a booking in the administrator dashboard (e.g. if a customer contacts to cancel). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> tick on the booking(s) to be deleted -> in the Action dropdown, select "Delete selected bookings" -> click go -> click "Yes, I'm sure" -> check that the booking has been deleted from the list | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on the booking to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check that the booking has been deleted from the list | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 007:** As a site owner I want to be able to manage and view contact requests so that relevant action can be taken. | PASS |
| + > **Use Case 007-001 (R in CRUD):** As a site owner I want to be able to view the contact forms submitted by users in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> click on a contact item to see the details | PASS |
| + > **Use Case 007-002 (D in CRUD):** As a site owner I want to be able to delete contact forms submitted by users in the administrator dashboard (e.g. for spam, or if the request has been actioned). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> tick the form(s) to be deleted -> in the Action dropdown, select "Delete selected contact infos" -> click go -> click "Yes, I'm sure" -> check that the selected forms been deleted from the list | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> click on the form to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check that the selected forms been deleted from the list | PASS |

### "Negative Testing"

Negative testing was undertaken to determine whether the application could handle unwanted or unexpected user input. The following were performed:


### Bugs

#### Fixed Bugs

- 

## Code Validation

[W3C HTML Validator](https://validator.w3.org/)

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

[JSHint Validator](https://jshint.com/)

[PEP8 Validator](http://pep8online.com/)

[Python Syntax Checker](https://extendsclass.com/python-tester.html)

# Credits

## Media

- [Materialize CSS](https://materializecss.com/) including Google Fonts and Icons
- [Font Awesome](https://fontawesome.com/)
- [Summernote](https://summernote.org/)


## Acknowledgements

- [The Code Institute](https://codeinstitute.net/) for their tuition and support throughout.
- [TimeTrap Escape Rooms](https://www.timetrapescaperooms.com/) for permission to use their images.
- User "Gaff" on the Code Institute Slack for help with the layout and content of the ReadMe file.