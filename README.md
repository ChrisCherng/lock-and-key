# Lock & Key Escape Rooms

[Lock & Key Escape Rooms on Heroku](https://lock-and-key-escape.herokuapp.com/)

![The homepage of Lock & Key](https://res.cloudinary.com/chris-cherng/image/upload/v1663594264/Escape%20Room/ReadMe%20Images/main_xuqqjt.png)

This is the website for Lock & Key Escape rooms providing information on the escape room experiences on offer and allowing users to make a booking for a game as well as manage their bookings.

An administration dashboard allows the administrators to create, amend and delete the information on each room, view bookings that have been made, and view any contact requests from users.

# Business

The Business goals describe the expected user and site owner goals - these drive the design, development, and deployment of the website application. The fulfilment of these goals determine the success of the application.

## External Users

The external users are potential and actual customers of the escape room. They are looking for information on the various rooms being offered at Lock & Key, as well as the ability to book a room. In addition, they want to be able to manage their bookings.

## Site Owner

The site owners are looking to attract potential customers and be able to manage customer bookings and contact requests in order to engage to the users.

# User Stories

The following user stories have been created to ensure the goals of the users and owner are met.

| User Story | Goal |
| --- | --- |
| **User Story 001:** As a site user I want to be able to view the different escape rooms offered so that I can assess my options. | Finding information on the escape rooms |
| **User Story 002:** As a site user I want to be able to view more details about each room so that I can find out more. | Finding information on the escape rooms |
| **User Story 003:** As a site user I want to be able to contact the site owner so that I can ask any questions. | Finding information on the escape rooms |
| **User Story 004:** As a site user I want to be able to make an account, log in and log out. | Ability to book a room |
| **User Story 005:** As a site user I want to be able to view which rooms are available to book. | Ability to book a room |
| **User Story 006:** As a site user I want to be able to book an escape room on an available date and time. | Ability to book a room |
| **User Story 007:** As a site user I want to be able to be able to view my bookings. | Ability to manage own bookings |
| **User Story 008:** As a site user I want to be able to delete bookings I no longer need. | Ability to manage own bookings |
| **User Story 009:** As a site user I want to be able to amend the timing of my booking. | Ability to manage own bookings |
| **User Story 010:** As a site owner I want to be able to manage the escape room information to ensure it is up to date. | Attract potential customers |
| **User Story 011:** As a site owner I want to be able to manage bookings for the escape room in order to plan for upcoming customers. | Manage customer bookings |
| **User Story 012:** As a site owner I want to be able to manage and view contact requests so that relevant action can be taken. | Manage contact requests |

The implementation of these user stories was managed using Trello (see Documentation Tools below).

# Features

Below is a summary of the features on the Lock & Key Escape Rooms website, split between users and administrators.

## Users

A user is a (potential) customer for Lock & Key. The user will need to register for a (free) account in order to make and manage bookings.

- All pages in the public site (i.e. not the administration site) include:
    - a navigation bar displaying the name of the company, along with links to contact the administrators and login.
    ![The navigation bar with "Lock & Key" and links to contact and login](https://res.cloudinary.com/chris-cherng/image/upload/v1666459793/Escape%20Room/ReadMe%20Images/navigation-normal_gakhmy.png)

    - if the user is logged in, the navigation bar displays that they are logged in (by using their username), and provides additional links to make a booking, My Bookings (to manage bookings), and logout.
    ![he navigation bar with "Lock & Key" and links to contact, logout, book, manage bookings](https://res.cloudinary.com/chris-cherng/image/upload/v1666459866/Escape%20Room/ReadMe%20Images/navigation-loggedin_wdeczy.png)

    - a footer with the business address and social media links.
    ![The footer with the company address, links to social media, and copyright information](https://res.cloudinary.com/chris-cherng/image/upload/v1663592967/Escape%20Room/ReadMe%20Images/footer_wudad0.png)

- All pages are responsive to different devices including mobile, tablet and desktop.

    ![The homepage on mobile showing the introductory messages](https://res.cloudinary.com/chris-cherng/image/upload/v1666460179/Escape%20Room/ReadMe%20Images/mobile_de13gv.png)
    
    - the navigation bar becomes a hamburger menu on mobile devices.

    ![The sidebar navigation on mobile](https://res.cloudinary.com/chris-cherng/image/upload/v1666464051/Escape%20Room/ReadMe%20Images/mobile-loggedin_kruron.png)

- Home Page with:
    - introductory information.
    ![The homepage showing the introductory messages](https://res.cloudinary.com/chris-cherng/image/upload/v1663592974/Escape%20Room/ReadMe%20Images/homepage_yd0zei.png)

    - a list of all currently available escape rooms with a summary of what each one is about.
    ![The homepage showing two available rooms](https://res.cloudinary.com/chris-cherng/image/upload/v1663592974/Escape%20Room/ReadMe%20Images/homepage-room-cards_obt8if.png)

- Room Detail pages for each available room with:
    - a more detailed description of the room.
    - if not logged in, a link to sign in or sign up in order to make a booking.
    - if logged in, a link to the booking page.
    ![The detailed page for Medieval Madness with additional description and booking button](https://res.cloudinary.com/chris-cherng/image/upload/v1663593349/Escape%20Room/ReadMe%20Images/detail-page_zxf7ux.png)

- Contact Page with:
    - a form to contact the site administrators.
    - a confirmation page to confirm successful submission of the form.
    ![The contact form](https://res.cloudinary.com/chris-cherng/image/upload/v1663594011/Escape%20Room/ReadMe%20Images/contact-page_qq1dej.png)

- Registration Page with:
    - a form to fill in with information in order to register for an account.

- Log In Page with:
    - a form to fill in log in information in order to access the account.

- Booking Page with:
    - a form to complete the relevant information for the booking.
    - a list of times for the selected day and room which are and are not available to book (if unavailable, the button is greyed out and unselectable).
    - the time selected is highlighted in green.
    - a confirmation page to confirm a successful booking.
    ![The booking form](https://res.cloudinary.com/chris-cherng/image/upload/v1666464254/Escape%20Room/ReadMe%20Images/booking-form_cftqec.png)

- My Bookings Page with:
    - a list of upcoming bookings for the logged in account.
    - the ability to cancel or amend the time of upcoming bookings.
    - a confirmation page to confirm that the cancellation of amendment was successful.
    ![The My Bookings page showing a list of upcoming bookings with buttons to cancel or amend each](https://res.cloudinary.com/chris-cherng/image/upload/v1666464877/Escape%20Room/ReadMe%20Images/my-bookings_kk2aap.png)

## Administrators

An administrator is a manager of Lock & Key Escape Rooms. This requires the use of a superuser account username and password, as this is not public-facing information.

- [Administration Page](https://lock-and-key-escape.herokuapp.com/admin/) with:
    - the ability to create, view, update and delete the escape room information visible on the public site.
    ![an image of the rooms admin page](https://res.cloudinary.com/chris-cherng/image/upload/v1663592366/Escape%20Room/ReadMe%20Images/admin-rooms_ibjaow.png)

    - the ability to create, view, update and delete the bookings that have been made by users.
    ![an image of the bookings admin page](https://res.cloudinary.com/chris-cherng/image/upload/v1663592366/Escape%20Room/ReadMe%20Images/admin-bookings_igvfyg.png)

    - the ability to view and delete any contact requests from users from the contact form.
    ![an image of the contact request admin page](https://res.cloudinary.com/chris-cherng/image/upload/v1663592366/Escape%20Room/ReadMe%20Images/admin-contact_dphbsy.png)

# Design

## Research

To help with the design of the website, a number of other escape room sites were researched. This was used to understand what content is included and how it is laid out on each page. From this research, the following key elements were found on the majority of sites:

- Eye-catching images used consistently across all parts of the site.
- Clear up-front information on the escape rooms.
- Simple navigation at the top.
- Clean colours.

These principles were used as the base for the initial design.

## Wireframe Layouts

Using the findings from the research, basic wireframes were drawn in Google Slides for the main pages.

### Homepage

![wireframe of the homepage using simple boxes for each section](https://res.cloudinary.com/chris-cherng/image/upload/v1666718349/Escape%20Room/ReadMe%20Images/wireframe-home_zf3kzi.png)

The homepage sets the tone for the users and includes a clear navigation bar and eye-catching main image. An introductory section provides the key information for users, including those who have been to an escape room and those who have not.

A section on who would enjoy the experience breaks up the page with more graphical elements.

If the user is interested by this point, more information on the specific escape rooms can be found, with links to further detail.

Finally a footer with the business address and contact information is included to assist users with these key logistical items.

### Other Content

![wireframe of the content pages using simple boxes for each section](https://res.cloudinary.com/chris-cherng/image/upload/v1666718349/Escape%20Room/ReadMe%20Images/wireframe-content_sa7ebw.png)

This covers all sub-pages from the homepage, including login and booking. A clean simple layout would help the users not to be distracted from their purpose of using this page. The same navigation bar, main image and footer from the homepage is used in order to provide consistency for the user's experience, as well as providing easy access to the elements they may need from the navigation bar or footer.

## Themes and Colours

The overall styling of the website uses MaterializeCSS. This provides a simple, clean aesthetic to the website, as well as including a number of useful styling tools.

![The Materialize colors for blue darken-3 and darken-4](https://res.cloudinary.com/chris-cherng/image/upload/v1666719832/Escape%20Room/ReadMe%20Images/materialize-blue_l3bjeg.png)

The key colour used is the Materialize "blue darken-4" which is hex code #0d47a1. This is a deep blue that contrasts with the clean white of the majority of the site. Where a blue is needed, but this shade has already been used, "blue darken-3" (#1565c0) is used as a simple way to denote a difference, but without moving too far from the key business colour. For example, when making a booking, the time selection buttons use this slightly lighter shade of blue, to contrast the use of the main blue for the submit button. These colours work well with white text to give easily readable text.

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

### Google Slides

Google Slides was used for the initial wireframing for the website design. See the Design section above for more details.

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
| **User Story 004:** As a site user I want to be able to make an account, log in and log out. | PASS |
| + > **Use Case 004-001:** As a site user I want to be able to make an account. | PASS |
| + + + > **Task 1:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> complete the required information for username, first name, last name, email, password, and password confirmation -> click "Sign Up" -> it should log you in, demonstrated by the username in the top right | PASS |
| + > **Use Case 004-002:** As a site user I want the sign up form to only submit if I have provided the correct information, to ensure an accurate booking. | PASS |
| + + + > **Task 1:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, omitting the username field -> click "Sign Up" -> a prompt should appear to say the "username" field must be completed. | PASS |
| + + + > **Task 2:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, omitting the first name field -> click "Sign Up" -> a prompt should appear to say the "first name" field must be completed. | PASS |
| + + + > **Task 3:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, omitting the last name field -> click "Sign Up" -> a prompt should appear to say the "last name" field must be completed. | PASS |
| + + + > **Task 4:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, omitting the email field -> click "Sign Up" -> a prompt should appear to say the "email" field must be completed. | PASS |
| + + + > **Task 5:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, omitting the password field -> click "Sign Up" -> a prompt should appear to say the "password" field must be completed. | PASS |
| + + + > **Task 6:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, omitting the password confirmation field -> click "Sign Up" -> a prompt should appear to say the "password confirmation" field must be completed. | PASS |
| + + + > **Task 7:** Open the home page -> click "Login" in the navigation bar -> click the "Sign Up" button -> fill in all fields, and in the email field, put in some text without an @ symbol -> click "Sign Up" -> a prompt should appear to say the email field must contain an @ symbol. | PASS |
| + > **Use Case 004-003:** As a site user, if I have an account, I want to be able to log in. | PASS |
| + + + > **Task 1:** Open the home page -> click "Login" in the navigation bar -> fill in the username and password per the account details created before -> click "Login" -> the homepage should be displayed. | PASS |
| + > **Use Case 004-004:** As a site user, if I have an account, I want to be able to see when I'm logged in. | PASS |
| + + + > **Task 1:** Open the home page -> click "Login" in the navigation bar -> fill in the username and password per the account details created before -> click "Login" -> the homepage should be displayed -> the text in the top right should show the username, to demonstrate being logged in. | PASS |
| + > **Use Case 004-005:** As a site user, if I am logged in, I want to be able to log out. | PASS |
| + + + > **Task 1:** Open the home page -> click "Login" in the navigation bar -> fill in the username and password per the account details created before -> click "Login" -> the homepage should be displayed -> the text in the top right should show the username, to demonstrate being logged in -> click "Logout" in the top right of the navigation bar -> the homepage should be displayed -> there should be no text in the top right navigation bar displaying the username. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 005:** As a site user I want to be able to view which rooms are available to book. | PASS |
| + > **Use Case 005-001 (R in CRUD):** As a site user I want to be able to see times for a given room on a given date. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "Book Now" in the navigation bar -> select a date -> select a room from the dropdown menu -> a list of possible times should appear. | PASS |
| + + + > **Task 2:** Open the home page -> log in as per user story 4 above -> scroll to the "Our Rooms" section -> select "More Info" on any room -> click "Book Now" in the room details page -> select a date -> select a room from the dropdown menu -> a list of possible times should appear. | PASS |
| + > **Use Case 005-002 (R in CRUD):** As a site user I want any times that have already been booked for a given date and room to be disabled for bookings. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "Book Now" in the navigation bar -> select a date -> select a room from the dropdown menu -> a list of possible times should appear -> select one of the times -> click submit -> repeat these steps and the booked slot should be grey and unclickable. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 006:** As a site user I want to be able to book an escape room on an available date and time. | PASS |
| + > **Use Case 006-001:** As a site user I want to be able to view the booking page. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "Book Now" in the navigation bar -> select a date -> the booking page should appear. | PASS |
| + + + > **Task 2:** Open the home page -> log in as per user story 4 above -> scroll to the "Our Rooms" section -> select "More Info" on any room -> click "Book Now" in the room details page -> select a date -> the booking page should appear. | PASS |
| + > **Use Case 006-002 (C in CRUD):** As a site user I want to be able to make a booking. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "Book Now" in the navigation bar -> select a date -> select a room from the dropdown menu -> a list of possible times should appear -> select one of the times -> click submit -> a "thank you for booking" page should be visible to confirm that the booking is successful. | PASS |


| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 007:** As a site user I want to be able to view my bookings. | PASS |
| + > **Use Case 007-001 (R in CRUD):** As a site user I want to be able to view what bookings I have. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "My Bookings" in the navigation bar -> a list of upcoming bookings for this account should be visible | PASS |
| + + + > **Task 2:** Open the home page -> log in as per user story 4 above -> make a new booking as per user story 6 above -> click "My Bookings" in the navigation bar -> the new booking should appear on the list | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 008:** As a site user I want to be able to delete bookings I no longer need. | PASS |
| + > **Use Case 008-001 (D in CRUD):** As a site user I want to be able to delete the booking I no longer need. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "My Bookings" in the navigation bar -> a list of upcoming bookings for this account should be visible -> click "Cancel" on the booking to be deleted -> a confirmation page should appear to confirm the deletion -> click on "My Bookings" and the booking selected should no longer be on the list. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 009:** As a site user I want to be able to amend the timing of my booking. | PASS |
| + > **Use Case 009-001 (U in CRUD):** As a site user I want to be able to amend the timing of the booking. | PASS |
| + + + > **Task 1:** Open the home page -> log in as per user story 4 above -> click "My Bookings" in the navigation bar -> a list of upcoming bookings for this account should be visible -> click "Amend Time" on the booking to be amended -> select the updated time for the booking -> click "Amend Time" -> a confirmation page should appear to confirm that the update has been made -> click on "My Bookings" and the booking selected should have the updated time. | PASS |

### Admin Testing

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 010:** As a site owner I want to be able to manage the escape room information to ensure it is up to date. | PASS |
| + > **Use Case 010-001 (R in CRUD):** As a site owner I want to be able to view the escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display. | PASS |
| + > **Use Case 010-002 (U in CRUD):** As a site owner I want to be able to amend the escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the title field -> click save -> go back into that room information to see the updated title -> check the website that the room has been updated with the new name | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the slug field -> click save -> go back into that room information to see the updated slug -> check the website that the room has been updated with the new slug in the URL | PASS |
| + + + > **Task 3:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the room description field -> click save -> go back into that room information to see the updated description -> check the website that the room has been updated with the new description | PASS |
| + + + > **Task 4:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> change the image field -> click save -> go back into that room information to see the updated image name -> check the website that the room has been updated with the new image on both the homepage and the room detail page | PASS |
| + + + > **Task 5:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the excerpt field  -> click save -> go back into that room information to see the updated excerpt -> check the website that the room has been updated with the new excerpt on the homepage | PASS |
| + + + > **Task 6:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the times field - this must be in the format "HH:MM:SS" separated by commas without spaces  -> click save -> go back into that room information to see the updated times -> check the website that the room has been updated with the new times on the booking page | PASS |
| + + + > **Task 7:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on one of the rooms and the detailed information should display -> make a change to the status field -> click save -> go back into that room information to see the updated status -> check the website that the room has been updated with the new status, that is, if it is now set to "Live" it should be visible on the homepage, if set to "Draft" it should be not be visible on the homepage | PASS |
| + > **Use Case 010-003 (C in CRUD):** As a site owner I want to be able to create new escape room information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on the "Add Room" button at the top right of the window -> complete the information for the title, slug, description, image, excerpt and times (times must be in the format "HH:MM:SS" separated by commas without spaces) -> click save -> go back into that room information to see the new room has been created | PASS |
| + + + > **Task 2:** Create a new room as per Task 1 above -> in the admin panel, select the room and update the "Status" field to "Live" -> click save -> check the website that the room is now visible on the homepage | PASS |
| + > **Use Case 010-004 (D in CRUD):** As a site owner I want to be able to delete an escape room in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> tick the box next the room to be deleted -> in the Action dropdown menu, select "Delete selected rooms" -> click Go -> click "Yes, I'm sure" -> check the dashboard that the room is no longer appearing -> if the room had a "Live" status, check that the room is no longer visible on the homepage | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Rooms" section in the sidebar -> a list of all rooms should be visible -> click on the room to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check the dashboard that the room is no longer appearing -> if the room had a "Live" status, check that the room is no longer visible on the homepage | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 011:** As a site owner I want to be able to manage bookings for the escape room in order to plan for upcoming customers. | PASS |
| + > **Use Case 011-001 (R in CRUD):** As a site owner I want to be able to view the booking information in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details | PASS |
| + > **Use Case 011-002 (U in CRUD):** As a site owner I want to be able to update the booking information in the administrator dashboard (e.g. if a customer requires a change of booking). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the room selected field -> click save -> go back into the booking to see the updated room selected | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the name field -> click save -> go back into the booking to see the updated name | PASS |
| + + + > **Task 3:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the email field -> click save -> go back into the booking to see the updated email address | PASS |
| + + + > **Task 4:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the details -> update the date -> click save -> go back into the booking to see the updated date selected | PASS |
| + + + > **Task 5:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on a booking to see the time -> update the date -> click save -> go back into the booking to see the updated time selected | PASS |
| + > **Use Case 011-003 (C in CRUD):** As a site owner I want to be able to create a booking in the administrator dashboard (e.g. if certain times need to be blocked off for staff training). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on "Add Booking" in the top right -> fill in the room, name, email, date and time fields (selecting a currently available time) -> set the booking type field to "Management Booked" -> click save -> check that this time for this room is no longer available on the booking page on the website | PASS |
| + > **Use Case 011-004 (D in CRUD):** As a site owner I want to be able to delete a booking in the administrator dashboard (e.g. if a customer contacts to cancel). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> tick on the booking(s) to be deleted -> in the Action dropdown, select "Delete selected bookings" -> click go -> click "Yes, I'm sure" -> check that the booking has been deleted from the list | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Bookings" section in the sidebar -> a list of all bookings should be visible -> click on the booking to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check that the booking has been deleted from the list | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 012:** As a site owner I want to be able to manage and view contact requests so that relevant action can be taken. | PASS |
| + > **Use Case 012-001 (R in CRUD):** As a site owner I want to be able to view the contact forms submitted by users in the administrator dashboard. | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> click on a contact item to see the details | PASS |
| + > **Use Case 012-002 (D in CRUD):** As a site owner I want to be able to delete contact forms submitted by users in the administrator dashboard (e.g. for spam, or if the request has been actioned). | PASS |
| + + + > **Task 1:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> tick the form(s) to be deleted -> in the Action dropdown, select "Delete selected contact infos" -> click go -> click "Yes, I'm sure" -> check that the selected forms been deleted from the list | PASS |
| + + + > **Task 2:** Navigate to the admin site (homepage/admin) -> login using superuser account -> click on the "Contact Infos" section in the sidebar -> a list of all contact form submissions should be visible -> click on the form to be deleted -> click the "Delete" button at the bottom of the page -> click "Yes, I'm sure" -> check that the selected forms been deleted from the list | PASS |

### "Negative Testing"

Negative testing was undertaken to determine whether the application could handle unwanted or unexpected user input. These tests were included within the following Use Cases:

- Use Case 003-003: As a site user I want the contact form to only submit if I have provided the correct information, to ensure my query can be responded to.
- Use Case 004-002: As a site user I want the sign up form to only submit if I have provided the correct information, to ensure an accurate booking.

The tasks performed for these use cases all operated as expected and the tests passed.

### Bugs

No unfixed bugs have been currently identified in the code.

#### Fixed Bugs

A number of bugs were fixed as part of the development process, including:
- In the site deployed to Heroku, the custom CSS overriding MaterializeCSS was not being applied. This was due to the static files not being picked up in Heroku. This was resolved through the implementation of the Whitenoise plugin.
- In the selection for a booking date, the datepicker would allow a user to select today, and potentially book a slot that has already passed. This has been fixed by creating a javascript variable for tomorrow's date, and setting that as the earliest selectable date.
- When booking a room, if there was a booking for that room on that day, it would duplicate the time selection buttons for the number of bookings. This was solved by refactoring the code for bringing through the buttons to separate out the buttons for booked and not booked.

## Code Validation

### HTML 
[W3C HTML Validator](https://validator.w3.org/)

The HTML was validated using the above validator, by running each key page on the site and viewing the source. This was then pasted into the validator for testing.

| Page | Exceptions | Comments |
| --- | --- | --- |
| Homepage | None | N/A |
| Room Detail | None | N/A |
| Contact | None | N/A |
| Contact Confirmation | None | N/A |
| Register Account | Tag closures in row 58 | Error arises due to a unordered list element being included within a paragraph element (with elements in between these tags being opened). This is code from Django forms and operates correctly. No issues noted. |
| Log In | None | N/A |
| Booking Page - Date Selection | None | N/A |
| Booking Page - Time Selection | Duplicate IDs | Due to method of disabling booked slots. Functionality works as intended. |
| Booking Confirmation | None | N/A |
| My Bookings | None | N/A |
| My Bookings - Amend Timing | Duplicate IDs | Due to method of disabling booked slots. Functionality works as intended. |
| My Bookings - Amend Timing Confirmation | None | N/A |
| My Bookings - Cancellation Confirmation | None | N/A |

### CSS
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

The majority of the CSS styling uses MaterializeCSS. An additional style.css file has been used to override any relevant stylings. No errors found in the style.css file.

### JavaScript
[JSHint Validator](https://jshint.com/)

JavaScript has been used within the base.html template file for a number of jQuery elements. The validator provides the following metrics:

- There are 6 functions in this file.
- Function with the largest signature take 2 arguments, while the median is 0.
- Largest function has 9 statements in it, while the median is 3.
- The most complex function has a cyclomatic complexity value of 3 while the median is 1.

No errors or warnings were raised (note: the "new JavaScript features (ES6)" is turned on in the Configure menu).

### Python
[PEP8 Validator](http://pep8online.com/)

The PEP8 Online validator is unavailable at the time of writing. The pycodestyle linter was used to detect any PEP8 issues in python files. This has been used on python files which have been written bespoke for this project - standard python files (e.g. those included withing standard Django) have not been tested.

- admin.py
- forms.py
- models.py
- urls.py
- views.py

No exceptions have been identified for these files in the "Problems" tab, except for views.py which includes the following item:

- *class does not have an 'object' member*: this test is looking to detect the 'objects' attribute in the class-based data models, and is created automatically by Django. However pylint cannot trace the Django code creating the 'objects' and there is providing the exception message. As the object is created, no issues noted with this item.

[Python Syntax Checker](https://extendsclass.com/python-tester.html)

The Python files above were pasted into the the Python Syntax checker. No exceptions were noted except for the models.py where syntax errors were noted for the use of Python f-strings. These are a relatively new addition to Python and have not been implemented in this check. Therefore, no issues have been identified.

## General Validator Checks

### [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
Lighthouse is a Google open-source, automated tool for improving the quality of web pages, providing metrics on the pages. The key pages on Lock & Key were tested with the results as below for desktop and mobile. Note that these scores are estimates and can change depending on a number of factors, so may differ if run independently.

Desktop:

| Page | Performance | Accessibility | Best Practises | SEO |
| --- | --- | --- | --- | --- |
| Homepage | 72 | 97 | 92 | 90 |
| Contact | 97 | 94 | 92 | 89 |
| Room Detail | 86 | 92 | 92 | 90 |
| Registration | 97 | 94 | 92 | 89 |
| Log In | 97 | 94 | 92 | 89 |
| Booking Date | 97 | 94 | 92 | 89 |
| Booking Time | 97 | 94 | 92 | 89 |
| My Bookings | 97 | 97 | 92 | 89 |

Mobile:

| Page | Performance | Accessibility | Best Practises | SEO |
| --- | --- | --- | --- | --- |
| Homepage | 74 | 97 | 92 | 87 |
| Contact | 77 | 94 | 92 | 85 |
| Room Detail | 74 | 97 | 92 | 86 |
| Registration | 77 | 94 | 92 | 87 |
| Log In | 76 | 94 | 92 | 86 |
| Booking Date | 98 | 94 | 92 | 85 |
| Booking Time | 99 | 94 | 92 | 85 |
| My Bookings | 76 | 96 | 92 | 85 |

The key observations from Lighthouse were as follows:

**Performance:** Slow loading of images, with the use of png files. The observation suggests the use WebP or JPEG. It should be noted that some of the images are not loaded for mobile users which improves the performances. The performance figures are generally good with no critical issues identified.

**Accessibility:** Some background and foreground colours not having sufficient contrast ratios. This is discussed in further detail in the Wave section below. The scores for accessibility are all very high, so no critical issues have arisen.

**Best Practises:** No significant or critical issues identified across all pages.

**SEO:** Uncrawlable links. This primarily relates to the burger menu when in mobile view which does not have a href due to the way it is built in MaterializeCSS. This does not need to be crawlable. No critical issue identified here.

These scores show there are no vital or significant issues with the performance, accessibility, practise or SEO of the website.

### [Wave](https://wave.webaim.org/)
Wave is an evaluation tool that helps authors make their web content more accessible to individuals with disabilities. The key pages on Lock & Key were tested with the following results:

| Page | Errors | Contract Errors | Notes |
| --- | --- | --- | --- |
| Homepage | 0 | 0 |  |
| Contact | 0 | 3 | Contrast errors relate to the field names when unclicked as they are a light grey. The icons and colouring of the text when clicked ensure this continues to be accessible. |
| Room Detail | 0 | 0 |  |
| Registration | 0 | 6 | Contrast errors relate to the field names when unclicked as they are a light grey per Materialize themes. |
| Log In | 0 | 2 | Contrast errors relate to the field names when unclicked as they are a light grey per Materialize themes. |
| Booking Date | 1 | 1 | Error relates to an empty "Next" button - however this has the "Next" text in, therefore no exception. Contrast errors relate to the field names when unclicked as they are a light grey per Materialize themes. |
| Booking Time | 2 | 1 | The first error relates to an empty form label for the dropdown for room selection - however this is correct using Materialize CSS. The second error relates to an empty "Submit" button - however this has the "Submit" text in, therefore no exception. Contrast errors relate to the field names when unclicked as they are a light grey per Materialize themes. |
| My Bookings | 0 | 0 |  |

No significant accessibility issues identified from the testing performed.

# Deployment

This website was deployed to Heroku using the following steps:

- Create a new Heroku app.
- Set configuration variables in Heroku for the database (postgresql), cloudinary, and other required keys.
- Link the Heroku app to the GitHub repository.
- Select "Deploy".
- Set "Automatic Deploys" to ensure the latest version is used when code is pushed to the repository.

# Credits

## Acknowledgements

- [The Code Institute](https://codeinstitute.net/) for their tuition and support throughout.
- [TimeTrap Escape Rooms](https://www.timetrapescaperooms.com/) for permission to use their images.
- [Unsplash](https://unsplash.com/photos/Vp3oWLsPOss) lock image by iMattSmart.
- User "Gaff" on the Code Institute Slack for help with the layout and content of the ReadMe file.
- My partner Scott for his ongoing support throughout the course.