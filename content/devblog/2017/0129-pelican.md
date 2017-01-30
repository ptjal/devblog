Title: Blogging Made Easy with Pelican and GitHub Pages
Date: 2017-01-29
Category: tutorial
Tags: pelican, blog, markdown, disqus, gravatar, github pages

### Overview

This post serves as a quick tutorial on setting up a web site using statically generated pages using
[Pelican](https://blog.getpelican.com/) for static site management, [Markdown](http://daringfireball.net/projects/markdown/syntax) for page authoring, and [GitHub Pages](https://pages.github.com/) for hosting.  These are all steps that I have used already to set up this site.  The intent is to have a web hosting solution that I can easily add content to without having to worry too much about fiddling with standard web development work and maintenance.  Oh, and all of this is free, so that is definitely a plus.

### Pelican

Pelican is an actively maintained static site generator written in python.  The basic idea is that you use a site template that will apply a common theme across all of your content pages.  You write your content using Markdown, reStructuredText, or Ascii and Pelican is run to create an output folder which can then be used as your static site.

Set up is really easy.  You can find more detailed instructions in [Pelican's Quickstart Guide](http://docs.getpelican.com/en/stable/quickstart.html), but it's so simple, I'll copy the steps below.

#### Installing Pelican and Markdown

If you don't already have python3 and pip installed on your system, check out [Python's Download Page](https://www.python.org/downloads/) and [pip's Install Page](https://pip.pypa.io/en/stable/installing/).  The following documentation assumes you have both of these installed as well as git and a decent editor (I like [Atom](https://atom.io/) but of course with my [vim-mode](https://github.com/atom/vim-mode) enabled).

````fish
pip3 install pelican markdown
````

#### Selecting a Theme

I already mentioned the concept of your site theme.  You can think of it as your web template that gets applied to all of your static content as well as creating the look and feel for you main page.  There are a good number of themes that are freely available through [Pelican's Theme Repo](https://github.com/getpelican/pelican-themes) or other public repos if you dig around.  Some seem better than others.  Pelican has a [live theme site](http://www.pelicanthemes.com/) where you can review the *official* themes.  I personally like, and am using [Flex](https://github.com/alexandrevicenzi/Flex).  If you don't like any of the options, you can always create your own.  They are Jinja templates and there are instructions [here](http://docs.getpelican.com/en/stable/themes.html).

By default, when installing Pelican, you only get two themes: notmyidea and simple.  To use any other theme, you need to make pelican aware of that theme.  Easiest way to try different themes out is to pull down the entire pelican-themes repo, then use the *pelican-themes* command line tool to import your selected theme into pelican.

````fish
cd ~/repos
git clone https://github.com/getpelican/pelican-themes.git
pelican-themes -s ~/repos/pelican-themes/Flex
````

The above commands clone the pelican-themes repo into a subdirectory under ~/repos and then creates a symlink (instead of a full copy) of the Flex theme into Pelican's theme directory.  Replace "Flex" with whichever theme you select.

### Building Your Site

The main concept that I am using to manage my site is to use a git repository for the static content pages, Pelican configuration, and related site content like images, etc.  Pelican makes this super simple to get started.  Simply create a new top-level directory for your web site, then run the *pelican-quickstart* on that directory.

````fish
cd ~/repos
mkdir mysite
pelican-quickstart -p mysite
````

The script will ask you some preliminary questions about your site. If you want to follow along
with this guide, pay special attention to the questions I have highlighted below:

````fish
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) https://tylorallison.github.io
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
````

Change out the URL prefix to match your site.  After you have run this script, you should have a few artifacts in your site directory:

* *content* -- This is the subdirectory where you will add all of your static content.
* *output* -- This is the default subdirectory where your generated pages get put.
* *pelicanconf.py* -- This is the main config file for your site.
* *publishconf.py* -- This file is used to create the final version of your output files before publishing.  It basically overwrites and/or appends values from the main config file.  This is useful if you wish to view your local changes first via a localhost web server before publishing live (not a bad idea).
* *develop_server.sh* -- Speaking of testing first, this is a super handy script that builds your site content and starts a simple web server locally.

First thing that you should do is modify the base pelicanconf.py to use your selected theme.  Edit the file via your editor and add the following line:

````
THEME = "Flex"
````

Replacing Flex with whatever theme you have decided to use.  You may want to review any documentation for your selected them as well, as often they may have theme-specific configuration.

### Draft Your Content

Now you should be set to start drafting content.  Just a few organizational things you may want to consider.  Pelican supports both a notion of category and tagging for the articles you create. These are both cool ways to put some structure to the content that you are generating. Most of the Pelican themes include templates for both category and tagging where you can view articles that fall under each type. Finally, you may wish to think about the folder organization of all of your articles.  Basically anything under the content directory will be scanned when you build your site.  And the layout of your site will not be dependent on the folder structure you use to store your articles.  Just something to keep in mind.

Now to draft your first article.  You'll need to decide which content format to use.  I will be demonstrating using Markdown, but feel free to visit the Pelican pages to see about support for other formats.  Next, create a new markdown file by opening a new file in your editor of choice:

````fish
cd ~/repos/mysite/content
vim my-first-article.md
````

Add the following lines to the tope of your new file:

````
Title: Your First Article
Date: 2017-01-31
Category: Blog
Tags: hello, world
````

Then fill in the rest and you are done.  Note, the Tags are comma-separated and can allow for spaces within your tags.

### Generating and Viewing Content Locally

The next step is to build out your content.  The easiest way of doing this is using the supplied *develop_server.sh* script.  Running this script will build a local copy of your site for you and start a python-based web server for you (defaulting to your localhost address on port 8000).  Simply start the script:

````fish
cd ~/repos/mysite
./develop_server.sh start
````

Then point your browser to 'http://127.0.0.1:8000' and view your content.  As long as this script is running you can continue to make local changes to content files, images, etc. and the script will detect those changes, rebuild and make them immediately available for you to view via your web browser.  Pretty handy indeed.

To stop the script, simply use:

````
./develop_server.sh stop
````

### Hosting to GitHub Pages

The final piece is to create a workflow to publish your new content to your personalized [GitHub Pages](https://pages.github.com/) repository.  The steps I am documenting will include instructions for setting up two repositories:

* Your Site Repository -- A repository for the static site content (~/repos/mysite)
* Your GitHub Pages Repository -- A repository for the generated output for your GitHub personal page.

Starting with the site repository, follow these steps to create the git repo:

* Login to your github.com account and create a new repository with a name that matches your
    site directory name (mysite in this example).
* Create a .gitignore file, adding the output directory, __pycache__ files, etc.
* Now locally create your repository using the git command line, adding your content:
````fish
cd ~/repos/mysite
git init
git add *.py content Makefile develop_server.sh
git commit -m "initial commit"
````
* Push your changes to GitHub
````
git remote add origin https://github.com/tylorallison/mysite.git
git push -u origin master
````

Next, create your GitHub Pages repository:

* Login to your github.com account and create a new repository with your appropriate site name.  
    The naming convention needs to exactly match: *youraccountname*.github.io.

The workflow that you will set up to publish changes includes running the final publish make command, updating your site repo's gh-pages branch with the contents of the output directory, then pushing the updated gh-pages branch to your GitHub Pages repository.  It might sound complicated, but it actually can be accomplished with the following three commands:

````fish
make publish
ghp-import output
git push https://github.com/tylorallison/tylorallison.github.io.git gh-pages:master
````

Again, replacing my username with your github account name.  Follow this same workflow any time you have new content to publish. The [GHP Import](https://github.com/davisp/ghp-import) tool is a simple tool that takes some of the more complex git commands and simplifies them for you.  And it is a pip install away:

````
pip3 install ghp-import
````

### Adding User Comment Support

If you want to provide users with the capability to post comments to any of your articles, that's not something static pages can be used for.  However, Pelican integrates with [Disqus](https://disqus.com/), which provides a free hosting service for user comments for any website. And integration is super simple.  Create an account on disqus.com, and create a new site.  You'll need to supply:
* Website Name -- enter a unique name for your site.
* Category -- select from one of their categories.

Then, go to your pelicanconf.py (or publishconf.py if you only want to enable for published pages) and add the following line:

````
DISQUS_SITENAME = "yoursitename"
````

Republish your content and it is as easy as that.

### Personalizing using Gravatar and favicon.ico

If you do happen to use the Flex them for Pelican, you'll want to add your own Site Logo.  I stumbled upon [gravatar.com](http://gravatar.com) and thought it was pretty cool.  The basic idea is that you use this site to automatically link a common avatar for your online presence, carrying over to any of your online discussions you may partake in.  As I want my online presence to be associated with this site, it makes sense to use it as my site logo.  

To integrate w/ Gravatar on your site, create a free gravatar account, upload an image that you want to serve as your global avatar, then update your pelicanconf.py file with the following:

````
SITELOGO = '//s.gravatar.com/avatar/221e6e31de6232bf3175b820a4a961e7?s=120'
````

You will need to replace the hash (221e6e...61e7 value) with your own unique value.  This is the MD5 checksum of the email address you used to sign up for your Gravatar account.  You can either compute this yourself:

````
echo -n <your email address> | md5
````

Or use the [Gravatar Site Check page](http://en.gravatar.com/site/check/) to generate the link for you.

I would also recommend that you select a favicon.ico to use for your site.  This is the little symbol that appears in the top tab in your web browser.  Find or create a favorite icon for your site and save it in your content directory (e.g.: content/images/favicon.ico).  Then add the following to your pelicanconf.py:

````
FAVICON = '/images/favicon.ico'
````

### Conclusion

OK, so maybe this wasn't as quick as I expected.  But really, the steps involved here are pretty easy.  And once setup, you can add new content to your site in as little as 4 commands.  And you haven't had to touch any CSS style sheets, raw HTML, or any of the like.
