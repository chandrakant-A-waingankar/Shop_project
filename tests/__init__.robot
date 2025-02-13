*** Settings ***
Resource    ../Resources/HolyGrail.robot
Suite Setup    Run Keywords    
...            User ${USER} Opens The Browser    AND    
...            User ${USER} Navigates To The Url    AND    
...            User ${USER} Logs In To The Shop    AND    
...            User ${USER} Verifies Homepage

Suite Teardown    Run Keywords    User ${USER} Logs Out The Shop



Test Tags    Test1