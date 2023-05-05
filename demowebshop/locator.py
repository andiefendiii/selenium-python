class elem():

##### Register Page #####
    tab_regist = "ico-register"
    rb_male = "gender-male"
    firstname = "FirstName"
    lastname = "LastName"
    email_regist = "Email"
    pwd_regist = "Password"
    confirm_pwd_regist = "ConfirmPassword"
    regist_btn = "register-button"
    error_msg_existingemail = "//li[text()='The specified email already exists']"
    error_msg_emptyfirstname = "//span[text()='First name is required.']"
    error_msg_emptylasttname = "//span[text()='Last name is required.']"
    error_msg_emptyemail = "//span[text()='Email is required.']"
    error_msg_emptypassword = "//span[text()='Password is required.']"
    error_msg_notmatchpassword = "//span[text()='The password and confirmation password do not match.']"

##### Login Page #####    
    tab_login = "ico-login"
    email = "Email"
    password = "Password"
    login_btn = "(//input[@type='submit'])[2]"
    tab_logout = "ico-logout"
    error_msg_login = "//span[text()='Login was unsuccessful. Please correct the errors and try again.']"

##### Shopping Cart ####
    tab_book = "//a[@href='/books']"
    book_card = "//img[@alt='Picture of Computing and Internet']"
    addtocart_btn = "add-to-cart-button-13"
    tab_shoppingcart = "//span[text()='Shopping cart']"

    # cart_product = "//img[@title='Show details for $25 Virtual Gift Card']"
    # addtocard_btn = "add-to-cart-button-31"
   
    # cb_shopcahrt = "//input[@type='checkbox']"
    # cb_agree_shopcart = "termsofservice"
    # checkout_btn = "checkout"
    # billing_address_city = "BillingNewAddress_City" #ID
    # billing_address1 = "BillingNewAddress_Address1" #ID
    # postalcode = "BillingNewAddress_ZipPostalCode" #ID
    # phonenumber = "BillingNewAddress_PhoneNumber" #ID
    # continue_checkout_btn = "//input[@title='Continue']" #XPATH
    # checkout_title = "//h1[text()='Checkout']"
    # recipient_name = "giftcard_2_RecipientName" #ID
    # recipient_email = "giftcard_2_RecipientEmail" #ID

