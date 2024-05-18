# DEVELOPMENT PROCESS

* The main development branch where all code finally needs to be merged is main. We use feature branch-based development under main.
* Clone the marchup repo and the submodule repos using
	git clone --recursive https://github.com/marchup-net/marchup-test.git

* Create a separate git branch under main for each effort (feature/bugfix)
	git checkout -b new-feature-branch

* Push branch to remote every day
	git add <list of files changed>
	git commit -m "Description for the commit"
	git push origin new-feature-branch

* Update the feature branch with latest main regularly and before pull request
	git fetch origin
	git merge origin/main 

* Create PULL REQUEST in github, once the Definition of Done for your changes

** The project lead will review and approve the code for merge into main




# DEFINITION OF DONE

* Functionality is demoed (either in a meeting or in a recording)
* Testing is complete
* Documentation: The code has adequate and clear inline comments
* Code is checked into feature branch

