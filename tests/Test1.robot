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


    
    
    
