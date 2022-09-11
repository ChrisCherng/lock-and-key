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


### Admin Testing

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