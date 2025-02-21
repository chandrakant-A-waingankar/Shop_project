*** Settings ***
Resource    ../Resources/HolyGrail.robot
Test Tags    All


*** Test Cases ***
TC-01 Create New Cloud Quote 
    [Documentation]   To verify that a user can create a new cloud quote successfully
    [Tags]    Quotes
    User ${USER} Creates A New cloud Quote
    User ${USER} Selects Subscription: pre-paid
    User ${USER} Selects Pre-paid Tenure: 14 Months (12 <= Tenure <= 36)
    #User ${USER} Selects Currency: dollar
    User ${USER} selects data center city: Mumbai
    User ${USER} Selects Plan: Business
    User ${USER} Selects Disocunt: 5 %
    User ${USER} Selects Free Period: 1 Month(s)
    User ${USER} Selects Expiry As Today
    User ${USER} Fills His Company Details
    User ${USER} Submits The Quote


TC-02 Create New SaaS Quote
    [Documentation]    To verify that a user can create a new SaaS quote successfully
    [Tags]    Quotes
    User ${USER} Creates A New SaaS Quote
    User ${USER} Selects Currency: dollar
    User ${USER} Selects Subscription: pre-paid
    User ${USER} Selects Pre-paid Tenure: 14 Months (12 <= Tenure <= 36)
    #User ${USER} selects data center city: Mumbai
    User ${USER} Selects Plan: Business
    User ${USER} Selects Disocunt: 5 %
    User USER Selects Trial (free Period) Period: 1 Month(s)
    User ${USER} Selects Expiry As Today
    User ${USER} Fills His Company Details
    User ${USER} Submits The Quote

TC-03 Create New Lead #1
    [Documentation]    To verify that user can create a new Lead sucessfully
    [Tags]    Leads
    User ${USER} Creates New Lead
    User ${USER} Selects Assigns To radio Option As: Partner
    User ${USER} Selects Source Option As: Website
    User ${USER} Selects Stage Option As: Open
    User ${USER} Selects Country Option As: India
    User ${USER} Enters Description: Give me Liberty or Give me coins
    User ${USER} Selects Name On Field 1 And Enters Value As: My_Name_is_khan
    User ${USER} Submits The Lead Creation Form

TC-04 Create New Lead #2
    [Documentation]    To verify that user can create a new Lead sucessfully
    [Tags]    Leads
    User ${USER} Creates New Lead
    User ${USER} Selects Assigns To radio Option As: Partner
    User ${USER} Selects Source Option As: Website
    User ${USER} Selects Stage Option As: Open
    User ${USER} Selects Country Option As: India
    User ${USER} Enters Description: Give me Liberty or Give me coins
    User ${USER} Selects Name On Field 1 And Enters Value As: My_Name_is_khan
    User ${USER} Adds Item To User Details
    User ${USER} Selects Company On Field 2 And Enters Value As: My_Name_is_khan_Company
    User ${USER} Submits The Lead Creation Form



TC-05 Open Royalties page from leftmenu
    [Documentation]    To verify that user is able to open Royalties page from left menu
    [Tags]    pages
    User ${USER} Opens Royalties Page From Left Menu
    Log    Page is opened succesfully
    Sleep    10s

TC-06 Open new Lead Page from leftmenu
    [Documentation]    To veirfy that user is able to open new Lead page from left menu
    [Tags]    pages
    User ${USER} Opens Page New Under Leads Dropdown From Left Menu
    Log    Page is opened successfully
    Sleep    10s


TC-07 Create new service order
    [Documentation]    To verify that user is able to create new service order
    [Tags]    serviceOrder
    User ${USER} Opens Page New Under Services Dropdown From Left Menu
    Sleep    2s
    User ${USER} Selects Service Item As SSL Certificate
    Sleep    5s
    User ${USER} Selects Billing Country As Afghanistan
    User ${USER} Enters certificate item name As Mycertificate
    User ${USER} Enters certificate Item Description As This is my test certificate
    User ${USER} Selects Discount For Item SSL Certificate As 2 %
    User ${USER} Fills His Company Details On Service Order
    User ${USER} Submits The Service Order

TC-08 Create new User
    [Documentation]    To verify that user is able to create new user
    [Tags]    newuser
    ${timestamp}    Get Unit Timestamp
    User ${USER} Opens Page New Under Users Dropdown From Left Menu
    User ${USER} Uploads Avatar Image test_data/cat.png
    User ${USER} Enters name As Eric james
    User ${USER} Enters email As Eric.james_${timestamp}@ice.com
    User ${USER} Enters position As QA_tester
    User ${USER} Enters password As Mail@123
    User ${USER} Enters password_confirmation As Mail@123
    User ${USER} Assigns The Role Admin To The New User
    User ${USER} Assigns Permission For Clouds To Overview
    User ${USER} Submits The New User Data

TC-09 check whether desired record is present in Leads or not
    [Documentation]    To verify that whether desired record is present in Leads or not
    [Tags]    leadSearch
    User ${USER} Opens Page Overview Under Leads Dropdown From Left Menu
    User ${USER} Searches the leads By company As Preferr
    User ${USER} Searches the leads By company As cgnfgn


TC-10 Create new Partner
    [Documentation]    To verify that user is able to create new partner
    [Tags]    Partner
    User ${USER} Opens Page New Under Partners Dropdown From Left Menu
    User ${USER} Verifies The Create New Partner Page
    User ${USER} Fills In The New Partner Data
    User ${USER} submits the new partner data


TC-11 User deletes a specific lead
    [Documentation]    To verify that user is able to delete a specific lead
    [Tags]    deleteLeads
    User ${USER} Opens Page Overview Under Leads Dropdown From Left Menu
    User ${USER} Searches The Leads By company As ABC
    User ${USER} Selects The Displayed Record(s) In Leads
    User ${USER} Deletes The Selected Records In Leads












    
    
    
