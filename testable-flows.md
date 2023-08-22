## Testable cases

This is a list that includes a small description of possible cases that could be executed on this project.

| # | Name | Description | Acceptance Procedure |
| ------ | ------ | ------ | ------ | ------ |
| 1 | Validate UI Elements | Verify that requested UI elements are present | Should include Header, Search Form, Search Result section |
| 2 | Validate Header | Verify that header is the same as App title | Should compare Header with App Title |
| 3 | Validate Search Form with GO button | Verify that the Search could be executed by clicking the Go button | Should execute a search inserting text then clicking on the Go button |
| 4 | Validate Search Form with Enter key | Verify that the Search could be executed by sending Enter key | Should execute a search inserting text then sending with Enter key |
| 5 | Validate Basic Info for Search Results | Verify that the Search results include the name, the URL and the description of the repo | Should execute a search inserting a valid text and sending, then verifying the info in the results |
| 6 | Validate When Info Description is not available | Verify that the Repo with no Description includes a '-' instead of a Description | Should execute a search inserting a valid text and sending, then verifying the info description with - |
| 7 | Validate Success feedback on top | Verify that when the search was correct, 'Success!' message is displayed | Should send a valid search and verify 'Success!' text.
| 8 | Validate Failure feedback on top | Verify that when the search was not correct, 'Github user not found' message is displayed | Should send an invalid search and verify the 'not found' text.

All scenarios on this list were automated in the given code example. 
