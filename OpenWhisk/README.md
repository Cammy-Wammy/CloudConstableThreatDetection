## How to Deploy

### Create Docker container with all dependencies
In the docker folder run (replace cammywammy with your own docker hub account):
- docker login
- docker build -t emailclassifier-image .
- docker tag emailclassifier-image cammywammy/emailclassifier-image
- docker push cammywammy/emailclassifier-image

### Deploy the code to OpenWhisk
In the deploy-pkg folder, zip up all three files into classifier.zip then run (note: add --web true to expose as a REST API):
- wsk action create score-text --docker cammywammy/emailclassifier-image classifier.zip

Test with (may take a wee bit of time to deploy, so you may need to reun the test a few times):
- wsk action invoke score-text --param text "I'm gonna kick your ass" -b

Or test the REST API with (named as score-text-rest):
https://openwhisk.ng.bluemix.net/api/v1/web/CloudConstable.com-AI%20XPRIZE%20competitor_ccdev/default/score-text-rest.json?text=i%27m+gonna+kick+you%27re+ass
