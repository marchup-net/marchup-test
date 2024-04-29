# DEVELOPMENT PROCESS

* The main development branch where all code finally needs to be merged is devel. We use feature branch-based development under devel.
* Clone the marchup repo and the submodule repos using
	git clone --recursive https://git-codecommit.us-west-2.amazonaws.com/v1/repos/marchup 

* Create a separate git branch under devel for each effort (feature/bugfix)
	git checkout -b new-feature-branch

* Push branch to remote every day
	git add <list of files changed>
	git commit -m "Description for the commit"
	git push origin new-feature-branch

* Update the feature branch with latest devel regularly and before pull request
	git fetch origin
	git merge origin/devel 

* Create PULL REQUEST in AWS Codecommit, once the Definition of Done for your changes

** Before the first pull request
** Install aws CLI. Refer to https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
** Run “aws configure” with AWS Access Key ID and Secret Access Key given by project lead. Set default region to us-west-2 and default output format to json
** aws codecommit create-pull-request --title "New Feature" --description "Adding a new feature required for FEATURE_DESCRIPTION" --targets repositoryName=marchup-test,sourceReference=new-feature-branch,destinationReference=devel
** The project lead will review and approve the code for merge into devel




# DEFINITION OF DONE

* Functionality is demoed (either in a meeting or in a recording)
* Testing is complete
* Documentation: The code has adequate and clear inline comments
* Code is checked into feature branch

