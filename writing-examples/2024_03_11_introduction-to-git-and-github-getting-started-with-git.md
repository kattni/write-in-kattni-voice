Title: Introduction to Git and GitHub: Getting Started with Git
Date: 2024-3-11 19:11
Author: Kattni
Tags: Getting Started, Programming, Tutorials
Slug: introduction-to-git-and-github-getting-started-with-git
Summary: In which you'll learn some basics of Git
HideTOC:
Status: published

<div class="article-content-core col" markdown="1">

Welcome to series of tutorials that will introduce you to a minimal, yet powerful, toolset that will help you feel comfortable getting started with Git and GitHub. This first tutorial will familiarise you with some of the basics of Git. The second tutorial will show you some GitHub basics, and how Git and GitHub fit together. Two future tutorials will extend your Git and GitHub toolsets with some further handy commands and concepts.

Think about the last time you tried to keep track of changes to a document. You have the original _document.txt_ file. Then, if you're lucky, you have three more copies: _document_updated.txt_, _document_updated_2.txt_, and _document_final.txt_. If you're unlucky, you also have _document_final_1.txt_ and _document_final_2.txt_. This is time-consuming, and begins to get unwieldy when dealing with more than even one file. Not to mention the inevitable tears. It also doesn't give you any information regarding what was changed, when it was changed, or, if working with others, who made the changes. 

Git is a tool designed to track changes to a file or set of files over time so you can recall specific versions later. This type of tool is called a "version control system". At its most basic, Git allows you to create snapshots, called "commits", as you work through your project, which allows you to track your changes over time. You can use Git from the command line using a terminal program. (There are also various applications that allow you to interact with Git; this tutorial will be using the command line as it works the same way across all operating systems.)

This tutorial will introduce you to Git. You'll learn how to configure Git, and the steps to follow to get started using it to track your changes.

# The kBits: Terminology
This is a list of terms that are used throughout this tutorial series. You'll find it in all tutorials in the series. If you get confused by something, you can refer back to this list for clarification.

* Branch - A line of development, independent of other branches. Your primary branch is `main`. Changes in a given branch will not affect other branches until you merge them. This is why you want to work on a separate branch and only merge into `main` when you're happy with the status.
* CLI - Command-line interface. This is what you are using when you are typing into a terminal prompt.
* Commit - A snapshot of your changes at the time of the commit.
* Commit message - A short message (50 characters or less), associated with a commit.
* Git - The name of a version control tool. (Whereas, `git` is the command you use.)
* `git` - The command used with the CLI for the Git version control software. (Whereas, Git is the proper name of the software.)
* Git CLI - The part of Git that provides the `git` command.
* GitHub - A cloud-based platform where you can store, share, and work together with others on various projects.
* Hash - The alphanumeric value that Git assigns to each commit. The hash is typically shown truncated to the first seven characters. 
* `main` - The "main" branch in your repository. It is meant to contain the current, functional, or "final", copy of your project. ("Final" is in quotes because obviously you will continue updating it over time. "Final" refers to whatever you consider to be good-to-go-for-now at a given point in time.) It is best practice not to work directly on `main`, and instead to work on a separate branch, and merge into `main` when you're happy with the status.
* Markdown - A lightweight markup language that allows you to apply formatting elements to plaintext.
* Merge - The process of adding the changes from your working branch to another branch, such as `main`. 
* Push - The process of sharing your local repo to GitHub. You `push` a specific branch, and that branch then shows up on GitHub. If the branch already exists on GitHub, then it is updated with the changes applied to that branch since the last push.
* Repository or repo - A specific directory for storing your project content. Git uses "local" repos, which are a local directory on your computer that you have initialised as a Git repo. GitHub uses "remote" repos, which are hosted on GitHub. Local repos allow for version control, however, features like collaboration and cross-machine development require using remote repos.
* Version control - A tool that records and tracks changes to a file or set of files over time so that you can recall specific versions later.

# The kBits: Git Commands
This is a list of the Git commands detailed in this tutorial, in order of appearance.

* `git config --global user.name`
* `git config --global user.email`
* `git config --global init.defaultBranch main`
* `git config --list`
* `git config --list --show-origin`
* `git init`
* `git status`
* `git add`
* `git commit -m`
* `git switch -c`
* `git branch --show-current`
* `git switch`
* `git branch`
* `git merge`
* `git branch -d`
* `git <command> --help`

# Resources
* [GitHub Documentation](https://docs.github.com/en)
* [Git Documentation](https://git-scm.com/doc)

# Terminal Program
This tutorial uses the Git CLI, which means working from the command line in a terminal program. MacOS and Linux have terminal programs installed by default. When installing Git for Windows, it includes Git Bash which will allow you to access the Git CLI and standard Bash commands. 

# Prerequisites
The following steps only need to be completed once.

## Installing Git and Creating a GitHub Account
There is already extensive documentation on [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), as well as [creating a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github). As such, I will not cover the details in this tutorial.

You can download the latest version of Git for your operating system [here](https://git-scm.com/downloads).

A couple of notes:

* On MacOS, if you install Xcode, you will be provided with an older version of Git. XCode is not included with MacOS by default; you can download it through the App Store. I can only verify the version  of Git available on XCode for MacOS 14 (Ventura), which was last updated April 2023. The download link provided above links to a package manager called Homebrew that allows you to install an updated version of Git on MacOS. All the commands used in this tutorial _should_ be available in the default version of Git included with Xcode. However, if you prefer to be running the latest, I suggest the Homebrew method.
* On Windows, you should be installing Git for Windows, which is available at the link above. Note that it is available in 32 and 64 bit; download the one that matches your system. Once installed, make sure you choose to use the "Git Credential Manager" for authentication. It is a setting available during setup.

I will cover the Git Credential Manager in the next part of this series, Introduction to Git and GitHub: Getting Started with GitHub.

This tutorial assumes you have installed Git successfully.

## Configuring Git
Once Git is installed, you'll need to do some configuration. You'll want to choose a name and email address to associate with your updates. They should be the name and email address you used when creating your GitHub account. You have two options for your configuration file.

1. There is a preferred location for your config file: _~/.config/git/config_. If you are interested, then follow the steps listed below _before_ you begin running the `git config` commands, and `config` will automatically begin using the file you created. This method is more involved than the second.
    * To create the directories, run:

        ```commandline
        mkdir -p ~/.config/git
        ```

    * To generate the config file, run:

        ```commandline
        touch ~/.config/git/config
        ```

     * To verify the file is created, run:

        ```commandline
        ls -a ~/.config/git
        ```
       
         If you were successful, should see the following:
       
         ```text
         config
         ```

2. If you do not follow the steps above, Git will automatically generate a config file for you in your home or user directory if you simply run the `config` commands. This file will be located at _~/.gitconfig_. This method is the less involved route, though not the preferred route.

Both options are acceptable. Note that there will be a concept covered in the future Git tutorial that also uses a file that is located in the _~/.config/git_ directory, so following the first option

Once you decide where you want to keep your configuration, and have completed the steps if you chose option one, you can begin configuring Git.

To complete the initial Git configuration, run the following commands.

To set your username, run the following, replacing `Your Name` with your name:
```commandline
git config --global user.name "Your Name"
```

To set your email, run the following, replacing `your@email.com` with your email:
```commandline
git config --global user.email your@email.com
```

Next, you'll want to set the default branch name to `main`. GitHub defaults to `main` when creating a new repository, and this ensures that you're defaulting to the same. Run the following command.

To set your default branch to `main`, run:
```commandline
git config --global init.defaultBranch main
```

To verify that you've configured Git properly, run:
```commandline
git config --list
```

If you ran the exact commands above, your results would look something like this:
```text
user.name=Your Name
user.email=your@email.com
init.defaultbranch=main
```

You only need to run these commands once, unless you want to change the information you supplied.

You may want to find out the location of your config file, to ensure `git config` used the appropriate file.

To view your Git configuration file location, run:
```commandline
git config --list --show-origin
```

Your results will look similar to the results above, however, they will now include the path to your configuration file as well. 

Note: If you ran the extra steps and you find that your configuration is located in _~/.gitconfig_ and not _~/.config/git/config_, you can run `rm ~/.gitconfig` to remove the autogenerated file, and follow the steps listed in the first option in this section to ensure the _config_ file was created. You can then rerun the rest of the steps redo the configuration in the intended location. Run the `--show-origin` command at any time during the process to verify that your configuration is in the appropriate file. If it is not, it is likely that you did not successfully generate the _config_ file, and should verify the initial steps were successful first.

Now it's time to create your new repository.

# Getting Started

## Initialising Your Git Repository
The next step is initialising your Git repository. This means running a command to create the files necessary for Git to work.

First, create a new directory, and change to that directory by running the following commands.

To create a new directory, run:
```commandline
mkdir my_first_repo
```

To change to that directory, run:
```commandline
cd my_first_repo
```

Now you're ready to initialise the repository. 

To initialise the repo, run:
```commandline
git init
```

This initialises the directory as a Git repo by generating a _.git_ directory with a series of files and directories in it. Git uses these files to, among other things, track your changes as you commit them.

If you want to verify the directory has been created, run:
```commandline
ls -a
```

The results should look something like this:
```text
.		..		.git
```

Never go mucking about in the _.git_ directory. Everything going on in that directory is automatically handled by Git.

You're now ready to begin working with your new repository.

## Keeping Up with the Repository Status
With Git setup and your repo initialised, you're ready to begin working. The first thing you'll want to do is check the status.

To check the current status of your repo, run:
```commandline
git status
```

The `git status` command should be your new best friend. You can run it at any time, and it will tell you the current status of the repo. As you're learning your way around Git, I suggest running it between every command. Not only will you be fully aware of your repo status throughout the process, it will help you get more familiar with the different steps. It also ensures that you really are in the state you think you are before you move on to the next step, which will help you avoid making mistakes. (Though the great thing about Git, and version control in general, is that it is designed to let you deal with mistakes.) Essentially, there's never a downside to running `git status`, and the upsides are numerous. 

The current status of your repo should be the following:
```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

The first line tells you that you are currently working on the `main` branch. The second line tells you that you have not yet made any commits. The third line tells you that there is currently nothing available to commit, and indicates the steps necessary to create content to commit.

You'll see `git status` throughout this tutorial. You'll learn what the different statuses mean, and how they can help you with your next steps. Use this command as often as you like. The more you use it the better!

## Git Will Help You if You Read What It Says
The first Git command you've learned, following configuration, is `git status`. Take another look at the current results.
```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Specifically, take another look at the section of the last line in parentheses: `create/copy files and use "git add" to track`. Over the next few sections, you'll learn how to create a new file and use `add` to begin tracking your updates. However, if you were embarking on this adventure without the help of this tutorial, you can see Git is doing its best to get you started as well.

**Git will help you along the way, if you pay attention to everything it says.**

This is some of the most important advice you'll receive here. This tutorial covers the things you need to know to get started, but you won't refer to the tutorial forever. Not to mention, you'll eventually move beyond the steps covered in this tutorial. As long as you pay attention, you'll find that Git will assist you throughout the process. You can think of this tutorial as someone running along side you, holding up the bicycle on your first attempt at riding it. Think of the information Git provides as permanent training wheels to help you as you start to figure out using it on your own.

## Creating Your First File
Now you need some content. You're going to generate a file called _README.md_. When it's time to learn about using GitHub, this file will come in handy, as GitHub renders this file and displays it as the main page on your GitHub repository. The _.md_ extension makes it a Markdown file. Markdown is a "lightweight markup language", which is a fancy way of saying, it allows you to apply formatting to plaintext documents. Don't worry if you have never heard of or used Markdown. I won't be directly teaching Markdown in this tutorial, but for the purposes of creating your README, I will give you some basics.

To create a new file, run:
```commandline
touch README.md
```

Now you have a new file, and you're ready for the next step.

## Making Your First Commit
You've created your README, and it's time to make your first commit. Where do you start? `git status`, obviously.

Run:
```commandline
git status
```

The results begin similarly, but now you'll notice your new branch and your _README.md_ file. Your results should look like the following:
```text
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

You're still on the `main` branch. There are still no commits yet. There are now, however, untracked files. If there was more than one new file, the others would also be listed here. There is, however, only your _README.md_ file. Above your file, there are instructions on what command to use to include the file for commit. Finally, it indicates that there is nothing added to commit but there are untracked files present, and includes instructions on what command to use to begin tracking the files. This is what the status will look like anytime you create a new repo, add a new file, and check the status.

The next step is to _add_ your file to the staging area. You can also think of the staging area as the list of files to be committed. Adding your file within Git is a completely separate concept from adding the file to the repository. Adding the file to the repository is simply creating the file. Adding the file to Git tells Git to start paying attention to that file. It's important to understand that Git tracks _changes_ you make in a given Git repo, whether that be creating a new file or making changes to a file. When you add a file to the staging area, you begin "tracking" the file, which means that Git is now paying attention to changes made to that file. Adding a file to the staging area adds it in the state it's in at the moment that you add it. Therefore, if you make changes _after_ adding it, but _before_ committing your changes, Git will indicate that there is a modification _not_ in the staging area. If you commit at that point without adding the new changes, your commit will contain only the state of the file when you originally added it.

Practically speaking, when you add a file to the staging area to begin tracking it, the `status` results will show it listed under "Changes to be committed:". If you then make further changes to the file _before_ you commit, the `status` results will indicate both that there is the file staged to be committed, and that there is a modified version of the file _not_ staged to be committed. 

This is a perfect example of why it's important to check `git status` at every step. You want to ensure that all the changes you expect to be included in a given commit, are, in fact, included. The `status` will tell you whether this is the case, and allow you to add further changes to the staging area, if needed, before you commit.

You've already verified the current status, so you can continue on to the next step.

To add the _README.md_ file for commit, run:
```commandline
git add README.md
```

You'll want to check the status again. Run:
```commandline
git status
```

Now your results should look like the following:
```text
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md
```

It begins the same as before, but now it indicates there is a new file called _README.md_, listed under changes to be committed. There are instructions on what command to use to "unstage" a file; unstaging a file will remove it from the staging area, and therefore, the list of files to be committed. If you add a file, but realise you're not ready to commit it, run the provided command to remove it from the staging area.

Now that you've added the file, you're ready to commit it. 

Each commit should be accompanied by a "commit message". This message should be less than 50 characters, and should succinctly explain what is included in the commit. For example, if you finished chapter three in your book, you could say, "Chapter three completed.", or if you're adding the search feature to your website, you could say, "Adding search feature." 

Often in the case of the first commit to a repo, it is customary to include, "Initial commit." I prefer to include additional information if it makes sense, so I've included "Add README.md." in this commit message.

To commit your changes with the suggested message, run:
```commandline
git commit -m "Initial commit. Add README.md."
```

You should see something similar to the following results:
```text
[main (root-commit) 5326742] Initial commit. Add README.md.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

Congratulations! You've made your first commit! 

Now, what about the results? What does all of that mean? Beginning with the first bracketed section of the first line:

* `main` - This is the branch name you committed to.
* `(root-commit)` - This indicates that this is the initial commit to this repo.
* `5326742` - This is the end of the commit hash. A commit hash is a long alphanumeric string associated with each commit. This will be different for yours, and for every commit you make. The information provided typically refers to only the final seven digits of the string.

The rest of the first line is your commit message.

The second line shows you some details about the changes you've committed. This commit includes 1 file changed, but no insertions or deletions. Insertions and deletions occur when you make changes to the contents of a file; insertions are additions to the file, and deletions are items removed from the file.

The final line indicates that you have created the file _README.md_. The included number is a Git internal reference indicating that this is a normal, non-executable file. (This number is not something you need to know, and is really only helpful if you look it up, so don't concern yourself with it too much.)

This is a good time to check your repo status again. Run:
```commandline
git status
```

The results should be:
```text
On branch main
nothing to commit, working tree clean
```

This indicates that there are no available changes to commit, which is as expected, because you've made your initial commit and haven't made any further changes.

Now that you've made the initial commit, you should create a new branch before making any further changes.

# Making Changes

## Branching Out from `main`
You saw from running `git status` that you are currently on the `main` branch. The initial commit in an empty repository needs to be made to the `main` branch. Once you've made that initial commit, it's time to begin making further changes on a separate branch.

Following the initial commit, you'll want to think of `main` as the final location for your project. This is where your work will end up once you consider it done for the time being. (Obviously you can always add to it in the future.) For changes you're actively working on, you'll want to create a new branch, separate from `main`. This may not seem like a necessary step now, however, as you begin to build up your core content, you'll begin to better understand why it is an important part of the workflow. 

Here's the thing. You _can_ work directly on `main`, but it's not best practice. Remember, `main` is meant to be the current, functional version of your project. It is quite simple to make changes directly to `main`, but it can lead to frustrating issues as you get further into your project. Here are a couple of examples to give you a better picture of why a separate branch is important.

In software development, you should have two separate servers, "production" and "development". "Production" contains the user-facing version of your software, the version that is currently functioning properly. "Development" is where you work on all of your changes because you will inevitably introduce bugs during the development process. Once you have everything working exactly as intended, you add it to "production", where it is now available to your users. There are plenty of software development folks who work directly on a "production" server. There are therefore plenty of instances of someone deploying a catastrophic failure directly to the user-facing version of the software, which is immediately followed by the required scramble to revert or fix the issue. That doesn't, however, avoid the unintended outage or interruption of service caused by the issue. These incidents can avoided by testing all your changes on a "development" server before deploying to "production".

Consider a factory floor. You don't do your product research and development there, you do it in a side lab. If your R&D leads you down a path that fails catastrophically, and the whole factory catches fire, it's harder to rebuild. If your separate lab catches fire, worst case scenario, you can always brick off the lab and build a new one in another room. Your factory production would remain uninterrupted and functional. On the other hand, when your R&D results in a well-tested successful new addition to your product, you can add the capability to the factory floor, and begin producing the updated product without issue.

Using a separate branch in Git is like your "development" server or your R&D lab. A safe space to work through whatever you want or need to, without worrying about damaging your existing content. So, as you work with your project, remember that it's best to work on a separate branch until you know for sure it's what you want to include in the existing content. Yes you can be a renegade and toss aside this best practice, but you do so at the risk of irritating many programmers who haven't had their morning coffee yet. 

## Creating a New Branch
Since you're about to begin making changes, it's time to create a new branch. Branch names can be any string of text without spaces. That said, to avoid confusing yourself later, you should always pick a name that clearly indicates what work the branch is intended to hold. For example, if you're writing a book, and you're beginning chapter three, you could call the branch `chapter-three`, or if you're adding a search feature to your website, you could call the branch `add-search`. The use of dashes is a personal preference; you could use underscores if you prefer. This tutorial will assume you've called your new branch `git-tutorial`.

To create a new branch called `git-tutorial`, run:
```commandline
git switch -c git-tutorial
```

This command _creates_ (`-c`) a new branch with the name provided and _switches_ to it.

To verify which branch you're currently on, run:
```commandline
git branch --show-current
```

Your results should look like the following:
```text
git-tutorial
```

This confirms that you are on the `git-tutorial` branch. If you see the `main` branch instead, run the `switch -c` command to create it, and verify again.

You're now in a new branch and ready to make changes.

## Updating Your README
Now, open a file explorer window and navigate to your _my_first_repo_ directory. You should find the your _README.md_ file. Open it into an editor. 

TextEdit on MacOS and Notepad on Windows will both open Markdown files. The editors available on Linux are specific to which distro you're using. Full-featured editors like VSCode and PyCharm will also open Markdown files, and will actually render them as you edit, which is super convenient when you're first learning to use Markdown. Command line editors, such as Vim and Nano, will also work.

Once you have the file open, type the following into it, and save.
```markdown
# My New Repo
```

In Markdown, beginning a line with a single `#` makes it a level 1 header. This is the title of your README.

Make sure you saved the file, and you're ready to commit again.

## Committing Your Changes
The process for committing your changes is exactly the same as the process for your initial commit.

First, check the repo status:
```commandline
git status
```

The results should be:
```text
On branch git-tutorial
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

You're still on the `git-tutorial` branch, and you have changes not staged for commit. This time, however, _README.md_ is showing as modified. This is because the file existed before the changes, as you already made your initial commit. This is how files appear that have already been committed but have new changes associated with them. There are instructions on how to add the file to be committed. It indicates there are no changes added to commit and explains how to add them. 

There are also instructions on how to discard the changes in the working directory. This command does exactly what it sounds like, and throws away your changes. That may not sound like a big deal at the moment, as all you've done is add a title to your README. However, there are times when you'll add a significant amount of work to your project, and running this command **wipes every change you've made since the last commit**. It's basically a method to burn your changes since the last commit to the ground. Why would you ever want to do this? You may have had working code at the last commit, and headed down a rabbit hole that messed everything up and didn't even come close to what you wanted to do. This command would return you to the last working state without having to undo hundreds of changes in your code file. It has its purpose, but should only be used in dire circumstances. Best to avoid it for now.

Now that you know the status, it's time to add the file to the commit list. Run:
```commandline
git add README.md
```

To check the status again, run:
```commandline
git status
```

The results should be:
```text
On branch git-tutorial
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
```

Same branch as before, and you now have changes to be committed. It shows that _README.md_ has been modified. You're ready to commit.

To commit your file with the following commit message, run:
```commandline
git commit -m "Add title to README."
```

The results are a bit different this time.
```text
[git-tutorial 116616c] Add title to README.
 1 file changed, 1 insertion(+)
```

The bracketed section shows the branch name and the new commit hash. The rest of the first line is your commit message. The second line indicates that one file was changed, and there was one insertion, which is to say, one line added.

Congratulations on committing your first change! Now you are ready to continue working on your README file, and track the changes as you go.

# When Should I Commit?
You might be thinking, "All I did was add a title, why would I want to track that change separately from adding more content?" The fact is, you probably wouldn't. But for the purposes of this tutorial, it made sense to use a quick change to demonstrate. 

That said, Git is designed to let you commit as early and as often as you like. Regardless of the type of content you're working on, be it a book, a shopping list, a Python program, or a list of names for your new cat, you'll find that tracking smaller chunks of changes can be really helpful. 

It's like a savepoint in a video game. Some games have many, some only a few. If you have only a few save points as you're grinding your way to the big boss, and die when you meet the boss, you have a significant amount of gameplay to redo to get back to the boss. While that might give you a lot of time to rethink your strategy, it's pretty devastating if you have to do it repeatedly. If you have many available save points, and the big boss kills you, you can come up with something new to try, and quickly find out if it's going to work or not. 

Practically speaking, consider a shopping list. Say you decide you want to make tacos for dinner tomorrow. So you add all the ingredients for tacos to the list. This would be a good time to commit, before continuing on to the next day's dinner idea. Perhaps you decide not to commit, and choose stir-fry for dinner the following day. You add all the ingredients for stir-fry to your list, but then you decide you'd really rather have chicken parmesan instead. You can run the undo command enough times to remove all of the stir-fry ingredients and get back to where you were. However, you can't use Git to help you because you still want the taco ingredients included. If you had committed after adding the taco ingredients, you could use Git to return you to that state in one command, so you could begin adding the chicken parmesan ingredients instead.

That is a rather simplified example, but there are plenty of situations where you may wish you had made a snapshot of a previous state that you could return to, and those moments come out of nowhere. Trust me. You'll thank yourself later when you have a point to return to from not long ago, versus having to piece together a way to get your project back to a desirable state after a significant amount of work that perhaps didn't end up working out the way you wanted it to. 

The best time to commit is early and often.

# Practicing with Your README
You can add some more updates to your README to practice making commits. First, you can add a sentence about your new repo. Open your README, and below the title, add a note.

For example, you could include:
```markdown

This is my first Git repository.
```

You should include the extra line between the title and your text. Some things that render Markdown care about the extra whitespace, so it's best to include it.

Save the file, and follow the steps to make a commit with the suggested commit message.
```commandline
git status
git add README.md
git status
git commit -m "Add description."
```

Next, you can add a new section to your README that lists the contents.

To add a level 2 header with a bullet list beneath it, indicating the current contents of your repo, add the following below your last sentence:
```markdown

# Repo Contents

* README.md
```

Save the file again, and follow the steps to make a commit with the suggested commit message.
```commandline
git status
git add README.md
git status
git commit -m "Add repo contents."
```

The README is in a good place now, and you're ready to move on to the next steps.

# Merging Back into `main`
You've created an excellent initial README for your repository. This means you're ready to _merge_ your work back into the `main` branch. Remember, the `main` branch is meant to be your completed work, in its current iteration. 

The first step is, as always, checking the current status with `git status`. This is important here because _you should never merge with uncommitted work_. This can cause issues, including the potential for you to lose some of your work. ALWAYS commit your work on your separate branch before initiating a merge into `main`. If all your work is committed, your status results should be:
```text
On branch git-tutorial
nothing to commit, working tree clean
```

Now that you're ready to merge your work into `main`, you first want to ensure that you're on the `main` branch. Currently, you're likely still on your `git-tutorial` branch. So, the first thing you need to do is switch to the `main` branch.

To switch to the `main` branch, run:
```commandline
git switch main
```

Before moving on, take a look at your README. The content is missing! Except that it's not. Don't worry, your content is safe. It's stored in the commits associated with the `git-tutorial` branch. The last commit you made to `main` was an empty README. So, when you switch back to `main`, you return to the last state associated with `main`. This is the case anytime you switch between branches. Until you merge a separate branch into `main`, the work you completed while on the branch remains in the separate branch. You can verify this by switching back to the `git-tutorial` branch temporarily.

To switch back to the `git-tutorial` branch, run:
```commandline
git switch git-tutorial
```

Check out your README. Everything's back! Perfect. Switch back to `main` again to prepare to merge.

To switch to the `main` branch, run:
```commandline
git switch main
```

As I said, you want to ensure you're on the `main` branch before merging. You can run the previously-discussed `git branch --show-current` to see the specific branch you are currently on. Alternatively, you can see a list of all branches and verify which branch you're on with the `git branch` command.

To see a list of all branches, and verify which branch you're on, run:
```commandline
git branch
```

Your results should look something like this:
```text
  git-tutorial
* main
```

Note the asterisk (`*`) next to `main` in your results. Remember, this indicates that you are on the `main` branch. If the asterisk is next to `git-tutorial`, make sure you run the command to switch to `main` before continuing.

You've verified that all your work was committed, and that you're now on the `main` branch. This means you're ready to merge.

To merge your work from `git-tutorial` into `main`, run:
```commandline
git merge git-tutorial
```

The resulting output will look something like this:
```text
Updating 5326742..a2d594c
Fast-forward
 README.md | 7 +++++++
 1 file changed, 7 insertions(+)
```

Here is the breakdown of the results:

* The first line shows the truncated hash of the last commit made to `main`, and the truncated hash of the last commit made to `git-tutorial`, separated by `..`.
* The second line informs you that it has performed a `Fast-forward`. The details of what this means are outside the scope of this tutorial. Know for now that this is what you're expecting.
* The third line shows you the updated file name, and indicates the number (`7`) and type (`+`, e.g. additions to the file) of change.
* The final line indicates that you have updated one file, with 7 insertions, e.g. additions to the file.

As there were no commits that removed content from the file, there are no `-` indicators in your merge results. As you continue to work on your project, you will definitely be removing content, and at that point, you'll see the `-` indicators on the third and fourth lines.

If you had committed changes to more than one file, the results would be longer and include the names of all files updated with the change indicators for each. The final line will aggregate the total files and changes.

## Cleaning Up Your Branches
Once you merge the work from your separate branch into `main`, the final step is to delete the branch. Deleting branches is not a requirement, however, doing so can avoid potential future mix-ups if you attempt to use the same branch name in the future. Unused branches can get "stale", and can cause major issues if you attempt to begin working from an old branch without realising. You can also end up with a bunch of stale branches to sift through looking for the one you are currently working on if you switch away from it for any reason and forget what you called it. The best way to avoid these issues is to delete branches as you go. 

To delete your `git-tutorial` branch, run:
```commandline
git branch -d git-tutorial
```

To verify that you successfully deleted your working branch, and that the only branch left is `main`, run:
```commandline
git branch
```

Your results should be:
```text
* main
```

You're all set! Congratulations on completing your first exploration into the fundamentals of Git!

# Continuing to Update Your Repo
You can follow all the steps above to add new content to your repo. Here's a recap.

Remembering to check `git status` every step of the way, make a new branch, make and commit your changes, repeating until you're happy with the current status, switch to the `main` branch, merge into `main`, and delete your working branch.

Then, when you're ready, begin again!

# Reading into the Details
The Git documentation is linked above, and has information on all the Git commands you've learned here. A quicker way to view the documentation for a given command is to run the command with `--help` after it. This opens the documentation for that specific command in your terminal program. You can navigate it using the up and down arrows, or the page-up and page-down keys, and you can exit by typing `q`.

For example, to learn more about `git config`, run:
```commandline
git config --help
```

You can do this with any Git command to learn more about it. 

# Wrap Up
Git is capable of many things. That said, the toolset provided in this tutorial will take you a long way. I've been working with Git since 2017, and the commands detailed here cover most of the commands I run in my day-to-day usage. 

In the interest of keeping this tutorial as straightforward as possible, I decided to cover the rest of my Git arsenal separately. This future tutorial will cover some further Git commands that, while not required to use the fundamentals of Git, definitely work together to make the experience a little smoother and give you more control over your environment. 

The next tutorial in this series will show you some fundamentals of GitHub, and how Git interacts with it. 

</div>