<h1 align="center">WearSani - Genuine Quality Pashmina Scarves and Blankets</h1>

[View the live project here](https://pf5-iomha-prints.herokuapp.com/)

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