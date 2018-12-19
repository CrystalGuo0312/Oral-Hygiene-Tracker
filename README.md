# README #

ELEC562 Oral Hygiene Tracker

## Credentials ##
If you want to access, login with patient and dentint accounts to see what each can do. I've mainly focused on creating the patient's functionality so far.

### Patient ###
Username: alice
Password: 1234qwer

### Doctor ###
Username: bob
Password: 1234qwer

### Admin ###
Username: joseph
Password: 1234qwer

BTW: I've been adding all the records so far using the admin view. We still need to create forms for everything (see 'What needs to be done?' section)

## What 's been done ##

* Set up the urls/views for the majority of pages
* Set up data model
* Login and logout controls
* Patients can look at announcements
* Patients can look at their oral hygiene records + detailed view
* Patients can view some oral hygiene info (this'll have to be changed)
* Patients can view their dentist and clinic contact info
* Patients can post in discussion forum (lifted entirely from another open source project lol)
* Patients can view embedded youtube videos

## What needs to be done? ##

* Front end design (!!!)
* Registering accounts (perhaps if a dentist attempts to register, create a dentist object in the database, then the admin manually has to create user object, link it with dentist object, and email password)
* We may want to change from username login to email login (I don't know how easy this is with django)
* Patients logging oral hygiene
* Dentists sending announcements
* Dentists viewing patients and their oral hygiene records
* Dentists approving/denying patient requests
* Security around not allowing a patient to visit dentist pages and vice versa, also ensuring they're logged in for each page (via @login_required)
* Probably more that I'm forgetting
