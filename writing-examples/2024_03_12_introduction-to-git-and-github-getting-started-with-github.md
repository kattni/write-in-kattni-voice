Title: Introduction to Git and GitHub: Getting Started with GitHub
Date: 2024-3-12 14:20
Author: Kattni
Tags: Getting Started, Programming, Tutorials
Slug: introduction-to-git-and-github-getting-started-with-github
Summary: In which you'll learn some basics of GitHub
HideTOC: Yes
Status: published

Welcome to a series of tutorials that will introduce you to a minimal, yet powerful, toolset that will help you feel comfortable getting started with Git and GitHub. The first tutorial familiarised you with some of the basics of Git. You learned how to get set up, and the steps to follow to get started using Git. This second tutorial will show you some GitHub basics, and how Git and GitHub fit together. 

GitHub is a cloud-based platform where you can store, share, and work together with others on various projects. You learned about creating a local repository using Git. GitHub allows you to post that repository to the web, where you can work on it across multiple computers. It also enables others to view it and collaborate on it with you, and enables you to collaborate on others' projects. GitHub integrates smoothly with Git, so using them together is quite straightforward.

This tutorial will introduce you to GitHub. You'll learn how to interact with GitHub using Git, and the fundamentals of updating projects on GitHub. 

## Tutorial Format Note
This tutorial provides terminal commands and terminal command _output_ as code snippets. The commands are preceded by the instructions to "run" the command. The output is preceded by text indicating that it is "results" you should be looking for. Blindly pasting every code snippet in this tutorial into your terminal program will end with sadness. Ensure that you read the text around the code snippets along with the code snippets themselves to avoid sadness.

## The kBits: Terminology
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

## The kBits: Git Commands
This is a list of the Git commands detailed in this tutorial, in order of appearance.

* `git remote add`
* `git remote -v`
* `git push`

## Resources
* [GitHub Documentation](https://docs.github.com/en)
* [Git Documentation](https://git-scm.com/doc)

## Terminal Program
This tutorial uses the Git CLI, which means working from the command line in a terminal program. MacOS and Linux have terminal programs installed by default. When installing Git for Windows, it includes Git Bash which will allow you to access the Git CLI and standard Bash commands. 

## Installing Git and the Git Credential Manager, and Creating a GitHub Account
There is already extensive documentation on [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), as well as [creating a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github). As such, I will not cover the details in this tutorial.

If you completed the previous tutorial in this series, then you should already have Git installed.

If you have not already, you should create a GitHub account.

To authenticate to GitHub from the Git CLI, you will need to [install the Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md).

A few notes:

* On MacOS, make sure to install Git _before_ installing the Git Credential Manager. Otherwise, if you install the GCM before installing Git, to ensure the GCM is configured properly, you will need to run the following command:
     * `git credential-manager configure`
* On Windows, the Git Credential Manager is included with Git for Windows. You should have configured its use during setup.
* On Linux, you will need to do a bit of configuration after installing. Follow the instructions on the install page linked above to install for your distro. Then, ensure you run the following commands to complete configuration:
     * `git-credential-manager configure`
     * `git config --global credential.gitHubAuthModes oauth`
     * `git config --global credential.credentialStore cache`
     * Optional: `git config --global credential.cacheOptions '--timeout 86400'` (This increases the cache timeout to 24 hours. You can set this number to any amount of time above 300 in seconds.)
* Git Credential Manager is not supported on ARM Linux. Don't bother. Don't ask why I know, but, I promise you, it doesn't work. I'm sure it'll be compatible eventually, but save yourself ordeal for now.

This tutorial assumes you have installed Git and the Git Credential Manager successfully, and have a GitHub account.

## Git and GitHub Will Help You if You Read What They Say
As discussed in the first tutorial in this series, Git regularly provides suggestions in its various outputs on how to continue on to the next step. GitHub doesn't necessarily provide terminal output, but it does provide assistance through the web interface. There is important information available throughout GitHub, whether it be details on each setting while creating your repository, or exactly what you're authorising a third-party entity to access on your GitHub account.

**Git and GitHub will help you along the way, if you pay attention to everything they say.**

This is some of the most important advice you'll receive here. This tutorial covers the things you need to know to get started, but you won't refer to the tutorial forever. Not to mention, you'll eventually move beyond the steps covered in this tutorial. As long as you pay attention, you'll find that Git and GitHub will assist you throughout the process. You can think of this tutorial as someone running along side you, holding up the bicycle on your first attempt at riding it. Think of the information Git and GitHub provide as permanent training wheels to help you as you start to figure out using them on your own.

## Create Your GitHub Repository
The first step in putting your content on GitHub is to create a GitHub repository. Head to [GitHub](https://github.com) and, if you are not already signed in, sign in.

This main page is your GitHub Dashboard. The contents will vary depending on the day, whether GitHub is promoting something like an event, and the width of your browser window.

As you have never created a repository before, you'll find a **Create Repository** button towards the top-left, as indicated by the purple arrow. 

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_Dashboard_New.png" class="inline-image center" alt="The GitHub main page, as seen while signed into a new, unused account. The Create Repository button in the left column is highlighted by a purple arrow.">

Note: Once you create a repo, this section will change to list your repo (or repos), and the button will then read **New**. Clicking **New** will take you to the same page as the original **Create Repository** did.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_Dashboard_top_repos_New_button.png" class="inline-image center" alt="The left column of the GitHub main page, as seen after creating a single new repository. The section title changes to Top Repositories, and the button changes to New. The new repo is listed by name below a repository search box.">

You should now be looking at a page titled "Create a new repository". The only item you are required to provide is a name for your repository. It is, however, also convenient to add a description. The rest of the settings should be left as default for now.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_Create_a_new_repository_blank.png" class="inline-image center" alt="The GitHub Create a new repository page with no changes to info or settings.">

You can name your repo "my_first_repo". For the description, you can use, "This is my first repo!"

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_Create_a_new_repo_name_and_desc.png" class="inline-image center" alt="The GitHub Create a new repository page repository name and description sections. The repository name is filled in with my_first_repo, and the description is filled in with This is my first repo!. Both text boxes are highlighted by purple arrows.">

Once you've filled those in, you can click the green **Create repository** button at the bottom-right.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_Create_a_new_repo_Create_repository_button.png" class="inline-image center" alt="The GitHub Create a new repository page final section. It indicates that you are creating a public repository in your personal account. There is a green Create repository button, highlighted by a purple arrow.">

After a moment, you'll be taken to a new page. Congratulations on creating your first GitHub repo!

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_my_first_repo_empty.png" class="inline-image center" alt="The GitHub header, viewed from within a new repository titled my_first_repo, including the repository menus and the first section of repository information.">

You're now ready to push your Git repo contents to GitHub.

## What Shows Up On GitHub When I Share My Content?
The answer: *everything committed on the branch that you push*.

This is incredibly important to keep in mind. If you intend to share your repo on GitHub, you need to be _completely_ certain that _everything_ you included is content that you're ok with being visible to anyone on the internet. NEVER include passwords, tokens, secrets, private information, personal information you want kept private, and so on. 

GitHub is designed around sharing and collaboration. By pushing your content to GitHub, you are making it available to everyone. It's great if you want to share your content, get feedback on it, invite others to collaborate with you, or simply be able to work on it from multiple computers. However, you should always keep in mind the implications of sharing your content on the internet.

You can make private repositories in the same way you make public ones, by changing the setting to "Private" on creation. However, your data is still on the internet, and should still be treated with care. Private repos should be for projects you're working on that perhaps you want to work on or access across different computers, but don't want made public for others to see. They should still not contain sensitive information. 

This may seem like common sense, however, without the details of what information is shared, you have no way to exercise this common sense to begin with. Not to mention, this is always worth a reminder.

## Pushing Your Content from Git to GitHub
The first thing you need to do to push your content to GitHub is tell Git where your repo is on GitHub, by adding a "remote" link to Git. The remote link is the HTTPS link to your GitHub repo, including the _.git_. If you take a look at the webpage for your new repo on GitHub, you'll see a Quick Setup section towards the middle of the page. It should default to HTTPS, and provide a copy button on the right side for the provided URL, indicated by the purple arrow. Click that button to copy the URL.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_my_first_repo_quick_setup.png" class="inline-image center" alt="The Quick setup section found towards the middle of a newly created, but completely empty repository on GitHub, with the copy URL button highlighted by a purple arrow.">

Return to your terminal program, and the local copy of your Git repo, to add the remote link. When you add a remote link, you must provide a name for the remote along with the link. The default name used for HTTPS remotes is `origin`. Personally, I find `origin` to be terribly vague. With only one remote, it's not so bad, however, there are situations where you will include multiple remotes, and that's when it starts to get confusing. Therefore, I always name a remote as the username associated with the remote link so it's clear where that link is going. In this case, you're adding your own link, so you would name it your GitHub username.

To add your GitHub remote to Git, replace `your-github-username` with your GitHub username and the link with your copied remote link, and run:
```commandline
git remote add your-github-username https://github.com/your-github-username/my_first_repo.git
```

Which is to say, you'd type into your terminal program, `git remote add your-github-username`, followed by a space, and then paste the contents of your clipboard. Your link should be the same as listed above with your username included, but, regardless, it's best to paste it directly from the Quick Setup URL copy.

To verify that it was successful by listing all of the available remotes, run:
```commandline
git remote -v
```

Your results should look something like the following:
```text
your-github-username https://github.com/your-github-username/my_first_repo.git (fetch)
your-github-username https://github.com/your-github-username/my_first_repo.git (push)
```

Now, it's time to push your `main` branch to GitHub. The `push` command expects two things: the remote name, and the branch to push. Here, the remote name is your GitHub username, and the branch you'll be pushing is `main`. 

To push your `main` branch to GitHub, using your newly added remote, run:
```commandline
git push your-github-username main
```

As this is the first time you've pushed, the Git Credential Manager will automatically step in at this point. In the window that pops up, click the browser button.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_CM_initial_dialogue.png" class="inline-image center" alt="The Git Credential Manager initial popup when attempting to push for the first time using HTTPS. The Sign in with your browser button is highlighted by a purple arrow.">

In your terminal, you will see:
```text
info: please complete authentication in your browser...
```

Your default browser will open and ask you to authorise the Git Credential Manager, by "Git Ecosystem". You'll see a list of the permissions this authorisation will provide. You can click the arrows for more details on each one, if you are interested. Once you're ready, click the green button at the bottom-right to **Authorise git-ecosystem**.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_CM_OAuth_authentication.png" class="inline-image center" alt="The GitHub dialogue to authorise the Git Credential Manager to access your GitHub account. It includes a list of what access is being authorised. The green Authorise git-ecosystem button is highlighted by a purple arrow.">

You should see a success page in your browser.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_CM_OAuth_authentication_success.png" class="inline-image center" alt="The GitHub Authentication Succeeded window, explaining you may now close this tab and return to the application.">

Note: _Never_ authorise an unknown entity to your GitHub account. If the authorisation window comes up, and you did not instigate it, you feel that the entity is requesting more access than you are comfortable with, or you do not recognise the entity requesting authorisation, do NOT authorise! As you could see in the window that came up, you are providing quite a bit of access to Git through the Git Credential Manager. This is expected and required for Git to integrate with GitHub. There are many other things that integrate with GitHub, and you may eventually be interested in using them. When you're ready for that, you'll see a similar window pop up asking for authentication to access a specified set of things within GitHub. _Always_ read through this thoroughly before authorising any access to your account.

Return to your terminal window. You will see something like the following.
```text
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (12/12), 977 bytes | 977.00 KiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/kattni-tutorial/my_first_repo.git
 * [new branch]      main -> main
```

 Note: You only need to authorise the Git Credential Manager the first time you push. From now on, when you run `git push`, you'll immediately see something similar to the results above in your terminal window. 

The details of what's going on above are beyond this tutorial. Simply know that this is approximately what a successful push output looks like. (Your values may differ.) If this is not what you see, then your push failed. Git output almost always tells you what went wrong, and what you can do to fix it. Chances are you skipped an earlier step, or the authentication failed. Follow the steps above again to resolve both of those issues.

Now you can head back to your browser and refresh the page. Hey! It's your README in its full rendered-Markdown glory! Remember I explained in the Getting Started with Git tutorial that you were creating a README because it plays nice with GitHub? This is what I was referring to.

It's also loaded with a lot of information, and it's probably incredibly overwhelming. For what it's worth, I stared at this page for over an hour while writing this tutorial, trying to figure out what to include and where to start explaining it. It was overwhelming for me, and I have worked with it on a near-daily basis for over six years. So, don't feel bad! It's a lot to process, and it's new to you. The words may look familiar, but they probably don't mean what you might think they mean. 

However, it turns out that's the whole point of this tutorial. I'll help you make sense of the important parts, and once you have those down, you can confidently begin checking out the rest. There are many things here that I will not cover in this tutorial, but you will learn about the parts that are relevant to what you'll be doing with GitHub, and how they relate to what you've learned about Git.

## The GitHub Static Header
Along the very top, you'll find the static GitHub header. This is a series of buttons, links, menus, and elements, which are accessible from anywhere in GitHub. The only exception, as noted below, is that your repo name is only present when you are viewing the repo. Otherwise, this header will be available as you explore GitHub.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_static_header_menu.png" class="inline-image center" alt="The GitHub static header, showing the menus and elements that appear throughout GitHub.">

From left to right, you'll find:

* A general GitHub hamburger menu - This has links to various sections of GitHub; most of this is not helpful to you at the moment, except that it does have a link to your repository. (It's worth noting that as you create more repositories, accessing them via this menu will eventually become unwieldy, and not worth your time.)
* The Octocat GitHub logo - This links to the main page of github.com
* Your username - You can click this to go to your profile page.
* The name of your repo - When you are in your repo, you can click the name of your repo at the top to return to this page. Note that when you are not in your repo, this link will not be present. **This is the only item on the top that changes based on where you are on the GitHub site - all other items are available throughout GitHub.** 
* Search - When you're looking at a repo, the search defaults to searching that repo. Otherwise, with various different syntax options, you can search within different scopes, or search GitHub as a whole.
* The "Add New" dropdown (a **+** symbol) - You can use this dropdown to create a new repo, among other things.
* The Issues button (a circle with a dot in the center) - This links to all GitHub issues associated with your username, including those you create or are mentioned on. This does not apply to you yet.
* The Pull Requests button (two lines, one with an arrow pointing back to the other) - This links to all GitHub pull requests associated with your username, including those you create or are mentioned on. This also does not apply to you yet.
* The Notifications button (an inbox icon) - As you get more involved with GitHub, this will show you all of your notifications in one place. This also probably does not apply to you yet.
* Your account menu - This menu contains everything you can do with your account, as well as links to the GitHub Docs and Support. You can ignore most of it for now. If you're interested in viewing your profile, you can do that in this menu. If you set an avatar, this menu will appear as that avatar, otherwise, it will appear as a default avatar.

## Exploring Your First GitHub Repo
The rest of the content on this page is specific to your repository. The various menus and links are only present while you are viewing a repository. As you explore the rest of GitHub, you'll find different layouts. For now, focus on your new repo.

<img src="../../../../Pictures/kattni-dot-com/2024/github-intro/GitHub_my_first_repo_main_pushed_annotated.png" class="inline-image center" alt="A GitHub repository containing a README.md file, with various elements highlighted by red boxes, each containing a number to identify them.">

Each item described below is numbered in the image. The number of the item is indicated in brackets, e.g. [1] refers to the box in the image numbered "1", etc.

The section below the static GitHub header is the static repository menu header. No matter where you go in your repo, this row of menus will remain visible. For right now, the only one that you'll want to focus on is the **Code** menu [1], at which you are currently looking. The others will come with time. 

Below the repo static header, to the left of your avatar, you'll find another repo-name link to your repo [2]. Next to that, it says "Public" [3]. This indicates that your repo is public, which means it's viewable by anyone. Further to the right, you'll find the **Pin** button [4]. Pinning a repository makes it show up at the top of your profile no matter what. This may seem silly now as you only have the one, but as you get more, there may be repos that are more important to you, or that you want to highlight on your profile, and you can pin those. Next to the Pin button, you'll see a dropdown that currently reads **Unwatch 1** [5]. When you create a repo, you are automatically subscribed to "watch" the repo, which means receiving notifications, including info about changes made, issues filed, comments left, etc. If you click this dropdown, you'll see you can customise what notifications you receive. The "1" indicates that one user is watching this repo, which would be you. In the event that someone else becomes interested in your project, they can also watch your repo, and the number will update to reflect the number of folks watching. 

The rest of the repo is split into two main sections, a left column and a right column. You'll start with the left.

The first item on the left is a dropdown currently showing **main** [6]. This tells you what branch you're currently viewing. If you click it, you'll find there are currently no other branches. That is because you did not push any other branches, and have not created any new ones on GitHub. In the event that you do push another branch, it'll show up here, and you can switch between it and main easily from this menu.

Below that, you'll find a link to your profile through your avatar, followed by your username [7]. Here, your username links to a list of commits you've made. If you click on it, you'll find the four commits you made to your repo, listed out with the commit message and the hash. You can click through the various links here to find detailed information about each of the commits you made to your Git repo.

Next to that, you'll find the last commit message you included when you made your most recent commit, followed by the commit hash and the time since that commit was made [8]. This will always show the latest commit message with its information.

At the end of this row, you'll find the number of commits that have been made to this repository, which links to the same commit list as your username in this row does [9]. This number will update as you add more commits.

Below that, you'll find a list of the files present in your repo, including the file name, latest associated commit message, and time since last associated commit [10]. Right now, the only file included is the _README.md_ file you created and edited. You'll see that, at the moment, the associated commit message matches the latest commit to the entire repo. However, this will not always be the case. Once you have multiple files, you may make a commit that edits only one file, in which case the other files' associated commit messages would not match the latest one above. Once you create, commit and push more files, they will show up in the list with the _README.md_ file 

Below that, you'll find your README rendered [11]. The Markdown you used to write it is interpreted by GitHub and displayed here. Any repo with a *README.md* file will display the contents here.

In the right column, you'll find information about your repo, including the description you added when you created it [12]. If you want to update the description, you can click the gear to the right of "About", and update it there.

That's an overview of your first repo!

## Continuing to Update Your Repo
You can follow all the steps in the previous tutorial, and the steps above in this tutorial to continue updating your repo. Here's a quick recap.

On your local repo, remembering to check `git status` every step of the way, make a new branch, make and commit your changes, repeating until you're happy with the current status, switch to the `main` branch, merge into `main`, and delete your working branch. 

Then, push your changes to GitHub, and refresh the repo page on the web. Your changes will appear!

## Wrap Up
GitHub has a lot of features. The processes and commands covered in this tutorial will get you started using GitHub to share your project content. Once you're comfortable with what you've learned, you can begin to explore the rest of what GitHub has to offer.

In the interest of keeping this tutorial as straightforward as possible, I decided to cover collaboration separately. This future tutorial will cover how to get involved with others' projects through contributing in various ways, and how to work with folks who are interested in contributing to your project.

For now, continue to work through the first two tutorials in this series, Getting Started with Git and Getting Started with GitHub, so that you're ready to incorporate the next tutorials when they're ready.