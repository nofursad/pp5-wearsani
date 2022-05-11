<h1 align="center">WearSani - Genuine Quality Pashmina Scarves and Blankets</h1>

[View the live project here](https://pp5-wearsani.herokuapp.com/)

The WearSani project is a B2C e-commerce application which sells Pashmina scarves and blankets to end customers.  The site aims to present users with an attractive and intuitive online shopping experience and encourage return visits through features such as discounts, a newsletter, social media posts, and an easy to use user profile function to save customer details.

The site is implemented as a retail store where users can view, search and filter the products on offer, then select items to add to their shopping cart and purchase through a secure single payment.

General users can view details of the products available for purchase and can sign up to the company newletter. In addition, registered users can create a wishlist of products they may be interested in and a profile to keep track of delivery details and order history.

Admin users can manage the lists of products that they sell, this includes being able to add new product to the range, update pricing. A full description of the available functionality is included in this document.

The Web Marketing strategies used by the project are :
- Organic Social - through facebook
- Email - through a newletter subscription managed via Mailchimp

The structure and purpose of the WearSani project is based on the Code Institute Boutique Ado walkthrough example application.

<!-- ![Mockup](Sample image of index page) -->

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories :

* EPIC 01 : Registration and Account Management
  <details>
      <summary>User Stories for EPIC 01: </summary>

  - US101 : Register for an account
      - As a **site user** I can **register for an account** so that **I can view my profile and purchasing history**
  - US102 : login and logout
      - As a **site user** I can **easily login or logout** so that **I can access my personal account information**
  - US103 : reset password
      - As a **site user** I can **easily reset my password in case I forget** so that **I can recover access to my account**
  - US104 : confirm registration via email
      - As a **site user** I can **receive an email confirmation after registering** so that **I can verify that my account registration was successful**
  - US105 : access user profile
      - As a **site user** I can **access my personalized user profile** so that **I can view my personal order history and order confirmations and my payment information**

  </details>

* EPIC 02 : Viewing and Navigation
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US201 : View a list of products
      - As a **site user** I can **view a list of products** so that **I can select some to purchase**
  - US202 : View individual product details
      - As a **site user** I can **view details for a specific product** so that **I can see the description, rating, available sizes and pricing**
  - US203 : View discounted items
      - As a **site user** I can **easily identify discounted items** so that **I can take advantage of savings on product I want to purchase**
  - US204 : View shopping cart total
      - As a **site user** I can **easily view the total of my purchases at any time** so that **I can avoid over-spending**
  - US205 : Like a product
      - As a **site user** I can **'like' a product** so that **it is added to my  wishlist in my personal profile**
  - US206 : Easily understand purpose of website and how to navigate
      - As a **site user** I can **quickly identify what the website is selling and easily navigate the pages** so that **I can quickly find the information and functionality I am looking for**
  - US207 : View wishlist / liked items
      - As a **site user** I can **view my wishlist** so that **I can see prints I have 'liked'**
  - US208 : View products by category
      - As a **site user** I can **view a specific category of product** so that **I can quickly narrow down the range of product I am interested in**
  - US209 : Handle 404 and 500 errors 
      - As a **site user** I can **return to Home after http 404 or 500 response** so that **I feel I am still working within the website and can navigate easily**

  </details>

* EPIC 03 : Sorting and Searching
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US301 : Sort list of available products
      - As a **site user** I can **sort the list of available products** so that **I can easily identify the best rated and categorically sorted products**
  - US302 : Sort a specific category of product
      - As a **site user** I can **sort a specific category of product** so that **I can find the best-rated product in a specific category or sort the products in the category or sort the products in that category by title**
  - US303 : Sort multiple categories of products simultaneously
      - As a **site user** I can **sort multiple categories of products simultaneously** so that **I can find the best-rated product in a specific category, or sort the products across broad categories**
  - US304 : search for a product by price or raw material
      - As a **site user** I can **search for a product by price or raw material** so that **I can find a specific product to purchase**
  - US305 : view search results and the number of items found
      - As a **site user** I can **easily view what I've searched for and the number of results** so that **I can quickly decide whether the product I want is available**

  </details>

* EPIC 04 : Purchasing and Checkout
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US401 : Add items to shopping cart
      - As a **site user** I can **add items to my shopping cart** so that **I can choose multiple items to purchase**
  - US402 : Modify cart contents and remove items from the cart
      - As a **site user** I can **modify cart quantities and remove items from the shopping cart** so that **manage the contents of my shopping cart and rectify any mistakes in selecting purchases**
  - US403 : View notifications of user interactions
      - As a **site user** I can **get notifications on screen of my actions** so that **I can easily understand my interactions with the website and their consequences**
  - US404 : Finalize order through the checkout page
      - As a **site user** I can **complete my order by going through the checkout page** so that **I can see a final total, a summary of my order and I can specify a delivery address and payment details**
  - US405 : Implement a secure payment process
      - As a **site user** I can **enter my payment details** so that **my payment is secure**
  - US406 : View an order confirmation after checkout
      - As a **site user** I can **view an order confirmation after checkout** so that **I can see what was ordered and total costs**
  - US407 : Receive an email confirmation after checking out
      - As a **site user** I can **receive an email confirmation after checking out** so that **I have a record of my purchases**

  </details>

* EPIC 05 : Admin and Store Management
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US501 : Add a product
      - As a **site admin** I can **add a product** so that **I can sell new items in my store**
  - US502 : Edit / update details for a product
      - As a **site admin** I can **edit / update details for a product** so that **I can change or amend the title, image, discount setting and other attributes**
  - US503 : Delete a product
      - As a **site admin** I can **delete a product** so that **I can remove the product for sale**
  - US504 : Edit / update details for a product size option
      - As a **site admin** I can **edit / update details for a product size option** so that **I can change or amend the price**


  </details>

* EPIC 06 : SEO and Web Marketing
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US601 : Subscribe to newsletter
      - As a **site user** I can **subscribe to the company newsletter** so that **I can keep up with company news and offers**
  - US602 : View company facebook page
      - As a **site user** I can **find the company on facebook** so that **I can keep up to date with company posts**
  - US603 : SEO
      - As a **site user** I can **find the site through web searches** so that **I can easily access the site**
  - US604 : View privacy policy
      - As a **site user** I can **view the company privacy policy** so that **I can see the company is GDPR compliant**

  </details>


## Features

### Existing Features

Below are descriptions of the main features of the application.  Many of the features are based on the Boutique Ado walkthrough project and SEO and Web Marketing modules of the course.  

The WearSani products application uses a B2C e-commerce model, selling directly to end customers with single online payments to cover purchases.

- **UX Related Features**
    
    
- **Authentication and Role-based Authorisation Related Features**
    
    
- **E-Commerce Related Features**
    
    
- **Data Administration Related Features**
    
    
- **SEO, GDPR and Marketing Related Features**


### Features which could be implemented in the future


## Design

-   ### Wireframes

    The wireframe diagrams below describe the application web pages.  

    <details>
    <summary>Desktop Wireframes</summary>

    <!-- ![Desktop Wireframes](wireframes-desktop) -->
    </details>
    <details>
    <summary>Tablet Wireframes</summary>

    <!-- ![Tablet Wireframes](wireframes-ipad) -->
    </details>
    <details>
    <summary>Smartphone Wireframes</summary>

    <!-- ![Smartphone Wireframes](wireframes-smartphone) -->
    </details>


-   ### Entity-Relationship diagram for DBMS


    <details>
    <summary>ER Diagram</summary>

    <!-- ![ER Diagrams1](entity-relationship-diagrams) -->
    </details>

## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project.  User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board.  All of the User Stories were linked to 'parent' Epic issues to show how they all supported the over-arching goals of the project.

The Epic, User Stories and Kanban board can be accessed here : [WearSani Agile Tool]<!-- (Link to project of github) -->


## Technologies Used

### Languages Used 

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/) 
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used  

-   [Google Fonts:](https://fonts.google.com/) used for the Lato and Old Standard TT fonts.
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-   [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web pages
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication (version 0.41.0 installed because of project dependencies).
-   [jquery library](https://code.jquery.com/jquery-3.4.1.min.js) - for various pieces of functionality including adding and removing items from the shopping cart and handling the increment and decrement of the quantity control.
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering.
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow database urls to connect to the postgres db.
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db.
-   [Heroku](https://www.heroku.com) - used to host the deployed application.
-   [Heroku Postgres](https://www.heroku.com/postgres) - SQL database service provided by Heroku used to store models and data.
-   [dbdiagram.io](https://dbdiagram.io/home) was used to create the Entity Relationship diagrams for the application data model
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.


## Testing

### Validator Testing 

- [HTML Validator](https://validator.w3.org/)


- [CSS Validator](https://jigsaw.w3.org/css-validator/)

### Manual Testing Test Cases and Results 

### Known bugs

## Deployment 

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application.  

1. How to Clone the Repository
2. Create Application and Postgres DB on Heroku
3. Connect the Heroku app to the GitHub repository 
4. Configure Amazon Web Services S3 to store static files and images
5. Configure STRIPE config vars and webhooks


<details>
<summary>How to Clone the Repository</summary>

- Go to the https://github.com/nofursad/pp5-wearsani.git repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- To install the packages required by the application use the command : pip install -r requirements.txt
- When developing and running the application locally set DEBUG=True in the settings.py file
- Changes made to the local clone can be pushed back to the repository using the following commands :

  - git add *filenames*  (or "." to add all changed files)
  - git commit -m *"text message describing changes"*
  - git push

- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku
- N.B. Be careful not to upload DEBUG=True in the settings.py file to GitHub - this setting should only be used locally.
</details>

<details>
<summary>Create Application and Postgres DB on Heroku</summary>

- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate 
- Set up and admin user in the postgres db using the command : python3 manage.py createsuperuser
- Set DEBUG flag to False in settings.py
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py
</details>

<details>
<summary>Connect the Heroku app to the GitHub repository</summary>

- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/nofursad/pp5-wearsani.git) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://pp5-wearsani.herokuapp.com/)
</details>

<details>
<summary>Configure Amazon Web Services S3 to store static files and images</summary>

- Log on to AWS account on aws.amazon.com - create an account if necessary
- From the dashboard access the S3 services
- Create a new 'bucket', it is recommended to give this a name similar to your application to make it easy to remember and use, choose a region close to you, uncheck "Block all public access" and acknowledge that the bucket will be public.  Next, click on the new bucket to configure it.
- Go to the properties tab and turn on static website hosting, fill in default values for index and error document settings - e.g. index.html and error.html and click on Save.
- Go to the permissions tab and make 3 changes to configure the bucket :

    - Step 1 Configure CORS : 
        - Paste the following CORS configuration string : <br>
    	[ { "AllowedHeaders": ["Authorization"],<br>
                "AllowedMethods": ["GET"],<br>
                "AllowedOrigins": ["*"],<br>
                "ExposeHeaders": [] } ]<br>

    - Step 2 Generate Policy:
        - Go to the bucket policy area, click on Edit and click on policy generator.  
        - Choose S3 bucket policy from drop-down
	    - Put asterisk in Principal field
	    - Select get object from Actions drop-down
	    - Copy ARN and paste into ARN box on the policy generator page
	    - Click Add Statement
	    - Click Generate Policy then copy the policy into the policy editor window
        - Add /* to the end of the Resource key
	    - Click Save

    - Step 3 ACL :
        - Go to the Access Control List area
		- Set the list objects permission for everyone under the Public Access section and
		check the box to confirm you want this permission setting

- Create a user to access the bucket through IAM as follows :
    - Return to the services menu on the dashboard and access the IAM area
    - Create a group
    - On the same page click on Policies, then Create Policy, go to JSON table and select Import Managed Policy
    - Click on Import managed policy on rhs
	- Search for S3 and select AmazonS3FullAccess and click on Import
	- Go back and get the Bucket Policy ARN (generated when bucket was created)
	- Change the Resource value from * to ARN bucket and its contents - e.g : <br>
        "Resource": [<br>
                    "arn:aws:s3:::pp5-wearsani",  (sensitive)<br>
                    "arn:aws:s3:::pp5-wearsani/*"<br>
                ]<br>
	- Click Next and then Review Policy
	- Give the policy a name and click Create Policy
    - Attach the policy to the group you created as follows : Go to groups, click on your group, go to the Permissions tab, click Add permissions and select Attach policies, select the policy created on previous step and click Attach permissions
    - Create user to put into the group. Click Users on lhs, click Add User, assign name check the programmatic access checkbox, click on Next:Permissions.  Add user to group, click through to the end and click Create User.

- Download and save the generated csv which contains the users access and secret access keys
- Update the AWS section of the settings.py file - replace the bucket name and region with the values you set up in the previous steps :

			if 'USE_AWS' in os.environ:
				# Bucket Config
				AWS_STORAGE_BUCKET_NAME = 'pp5-wearsani'    <------ bucket name and region
				AWS_S3_REGION_NAME = 'eu-west-1'
				AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
				AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

- Add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY config vars to heroku using the values from the downloaded cvs
- Add USE_AWS = True to the Heroku config vars
- Remove the DISABLE_COLLECTSTATIC config var at this point from Heroku
- The custom_storages.py file that is part of this project will tell Django to use S3 to store static and media files when collectstatic is run
- The remaining AWS configuration settings needed are already configured in this projects settings.py file
- Go to the S3 dashboard and create a folder called media in the new bucket.  Specify grant public-read access on the folder and tick the checkbox to confirm.
</details>

<details>
<summary>Configure STRIPE config vars and webhooks</summary>

- Log in to your Stripe account - create one if necessary
- Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to the Heroku config vars, assign these variables values from your Stripe account dashboard
- Create a webhook endpoint for use with your applications.  On the stripe dashboard go to the Developers -> Webhooks area, click add endpoint, use the url of your Heroku application with '/checkout/wh/' tagged onto the end of the url string.  When configuring the endpoint, the events to register to listen to are payment_intent_succeeded and payment_intent_failed
- Once the endpoint is set up get the signing secret for the webhooks and save this value as a Heroku config var called STRIPE_WH_SECRET.
</details>

#### The live link to the application can be found here - [P5 WearSani](https://pp5-wearsani.herokuapp.com/) 

## Credits 

### Code 

### Content 

### Media 

### Acknowledgments
