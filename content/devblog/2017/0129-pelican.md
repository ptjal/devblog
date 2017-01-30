Title: Blogging Made Easy with Pelican and GitHub Pages
Date: 2017-01-29
Category: tutorial
Tags: pelican, blog, markdown, disqus, gravatar, github

### Overview

This post serves as a quick tutorial on setting up a web site using statically generated pages using
[Pelican](https://blog.getpelican.com/) for static site management, [Markdown](http://daringfireball.net/projects/markdown/syntax) for page authoring, and [GitHub Pages](https://pages.github.com/) for hosting.  These are all steps that I have used already to set up this site.  The intent is to have a web hosting solution that I can easily add content to without having to worry too much about fiddling with standard web development work and maintenance.  Oh, and all of this is free, so that is definitely a plus.

### Pelican

Pelican is an actively maintained static site generator written in python.  The basic idea is that you
use a site template that will apply a common theme across all of your content pages.  You write your content
using Markdown, reStructuredText, or Ascii and Pelican is run to create an output folder which can then be used as your static site.

Set up is really easy.  You can find more detailed instructions in [Pelican's Quickstart Guide](http://docs.getpelican.com/en/stable/quickstart.html), but it's so simple, I'll copy the steps below.

#### Installing Pelican and Markdown

If you don't already have python3 and pip installed on your system, check out [Python's Download Page](https://www.python.org/downloads/) and [pip's Install Page](https://pip.pypa.io/en/stable/installing/).  The following documentation assumes you have both of these installed as well as git and a decent editor (I like [Atom](https://atom.io/) but of course with my [vim-mode](https://github.com/atom/vim-mode) enabled).

````fish
pip install pelican markdown
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
> What is your URL prefix? (see above example; no trailing slash) http://ptjal.github.io
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
````

Change out the URL prefix to match your site.  After you have run this script, you should have a few artifacts in your site directory:

* *content* -- This is the subdirectory where you will add all of your static content.
* *output* -- This is the default subdirectory where your generated pages get put.
* *pelicanconf.py* -- This is the main config file for your site.
* *publishconf.py* --
* *develop_server.sh* -- Super handy script that builds your site content and starts a simple web server locally.  This is great for reviewing your content before publishing.

### Hosting

### Adding User Comment Support

### Personalizing using Gravatar and favicon.ico
