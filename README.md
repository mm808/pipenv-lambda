PIPENV-LAMBDA
===========
My first pipenv and Github Workflow project. I want to try out the package management and distribution capabilities of pipenv.    
This project will create a Lambda that puts a json file in an S3 bucket. I wanted to try out using the free tier agents and the Actions feature of Github.    
This proejct includes a .github/workflow directory with a file the Actions feature uses to build and deploy the Lambda.   
If you use the project in your own Github you need to configure your secrets for AWS access. If you use it with another CI?CD tools you need to reconfigure the build process.

### Installation from dist
Because the end product is a Lambda if you install the distribution you do not get something that you can use locally.    
Sorry that the model of using pipenv and creating a dist doesn't make sense in context of creating a Lambda. Better planning next time I guess.    

### For further development    
Follow these steps:    
- ensure 'pip' and 'pipenv' are installed
- clone repo    
- cd to repo directory    
- run 'pipenv shell' to activate the shell   
- run 'pipenv install' to install additional dependencies
