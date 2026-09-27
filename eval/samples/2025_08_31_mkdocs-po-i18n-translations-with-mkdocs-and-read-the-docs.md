Title: MkDocs PO I18n: MkDocs translations with PO files and Read the Docs
Date: 2025-8-31 16:40
Author: Kattni
Tags: Open Source, Documentation, Programming, Tutorials
Slug: mkdocs-po-i18n-mkdocs-translations-with-po-files-and-read-the-docs
Summary: 
HideTOC: True
Status: published

I am currently working through the process of considering the possibility of switching the BeeWare documentation from Sphinx to MkDocs. There are a few requirements that were provided at the outset, in terms of features that absolutely need to work for this project to move forward. I decided to begin with getting the obvious potential blockers out of the way, as any one of those features not working would mean the switch wasn't possible. One of the biggest necessary features is translations. The BeeWare tutorial is currently translated using [gettext PO files](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html) via [Weblate](https://weblate.org/en/), and it is hosted on [Read the Docs](https://about.readthedocs.com/) (RTD), in all available languages. Therefore, the same setup would need to be possible for us to consider MkDocs as an option. 

I began researching what options were available; I'll be doing a second post with what I found that didn't work and why. To say the least, the existing translation methods were less than ideal, and, for the most part, did not use PO files. Continued research led me to the [Translate Toolkit](https://docs.translatehouse.org/projects/translate-toolkit/en/latest/index.html), which is a set of tools designed to convert between a number of file formats, including Markdown, to and from PO files. My hunch that I now had everything necessary to create a translation solution for my needs would prove to be accurate. From these pieces, I successfully created a Read-the-Docs-, PO-file-, and Weblate-compatible, dynamic translation solution for MkDocs that I've called [MkDocs PO I18n](https://github.com/kattni/mkdocs-po-i18n/). 

I used three tools from the Translate Toolkit (`md2po`, `pot2po`, and `po2md`), and wrote four custom Python scripts, optionally combined into a set of commands run using [`tox`](https://tox.wiki) (with [`tox-uv`](https://github.com/tox-dev/tox-uv#tox-uv)), to ensure the same experience locally as on RTD. 

BeeWare had existing translations, and we did not want to lose all the work folks had put into translating the Sphinx version of the documentation. To that end, I wrote a separate script that converted the reStructuredText syntax to Markdown syntax, and then used another Translate Toolkit tool called `pomerge` to merge the existing translations with the new Markdown-generated PO files. The script is mostly effective, however, it turns out machine translation tools don't necessarily understand rST link and inline code syntax, so there were a significant number of broken links that caused trouble. I spent the time to search the files for various rST link syntax elements, and manually updated what was missed. The script worked well enough, but I could not rely on it to work perfectly.

I don't intend to explain everything necessary to work with MkDocs here; it is well documented. However, the configuration file, build, and serve setup matter to the translation workflow. So I will be including the relevant parts of my documentation setup.

## The kBits

* Create Markdown documentation, and save it to a `docs/language-code` directory, where `language-code` is the primary documentation langauge code. In my case, the primary language is English, so the documentation resides in `docs/en`.
* Include, in your repo, `requirements.dev.txt` and `requirements.docs.txt` files OR a `.pyproject.toml` file with dependency groups with the following:
    * Add `"mkdocs-po-i18n @ git+https://github.com/kattni/mkdocs-po-i18n#desiredhash"` to `requirements.docs.txt` or to a `docs` dependency group in `pyproject.toml`. Always specify a hash on when installing from a GitHub repo; otherwise, you may be in for a surprise when things are updated.
    * Optionally, add `"tox-uv==version"` to `requirements.dev.txt`, or to a `dev` dependency group in `pyproject.toml`.
* Create a set of `mkdocs.language-code.yml` files, where `language-code` in each file is the language code for every language you intend to include. You need at least one of these files for your primary language to build any documentation. My initial config file is `mkdocs.en.yml`. 
* Create a `config.yml` file to be the base MkDocs configuration file.
* Generate initial POT files from the Markdown in the primary language, and save them to the `docs/locales/templates` directory.
* Generate the various language PO files from the POT files and output them to the `docs/locales` directory, containing a `language-code/LC_MESSAGES` subdirectory for each language.
* If applicable, create and set up a `tox.ini` file.
* If you intend to publish to RTD, complete the following:
    * Create and populate a `.readthedocs.yaml` file, and push it to your repo.
    * Set up the project on RTD for the primary language version to build the documentation from your GitHub repo.
    * Add a translation to the project on RTD, for each desired language.
* Push the configuration files and documentation content to your GitHub repo.
* Verify the documentation is building in all languages.

## Markdown documentation

MkDocs PO I18n expects the Markdown documentation to be maintained in a `/docs/language-code/` subdirectory, where `language-code` is the primary documentation langauge code. In my case, the primary langauge is English, so Markdown content resides in `/docs/en/`.

## Required prerequisites

The following setup is required by MkDocs PO I18n.

### Project configuration

MkDocs PO I18n is currently installable directly from GitHub. You will need to include project configuration in your repo, using a `requirements.txt` file, or a `pyproject.toml` file.

The following can be added to either setup, where `desiredhash` is the commit hash you wish to install:

```
"mkdocs-po-i18n @ git+https://github.com/kattni/mkdocs-po-i18n#desiredhash"
```

**Note: Always pin to a commit hash when installing a package directly from GitHub!** Doing so serves the same purpose as pinning a package to a specific release; in the event that the API changes or a bug is introduced, you won't be caught by surprise when your workflow breaks.

### MkDocs configuration files

MkDocs requires a configuration file. My setup uses two; a base `config.yml` file, and a set of `mkdocs.language-code.yml` files that inherit the base configuration. This allows for specifying language-specific configuration for each language, and while not duplicating the rest of your base configuration.

You will create an `mkdocs.language-code.yml` file for the primary language and each language for which you intend to provide translations; this configuration is required for Read the Docs to build successfully. The settings contained in this file should be only options that are language-specific.

You will also create a base configuration file called `config.yml` that contains all configuration shared by all languages; this allows you to apply further options to all builds without duplicating information.

An example `mkdocs.en.yml` would contain the following:

```yaml
INHERIT: config.yml
site_name: My Amazing Docs
site_url: https://example.com
docs_dir: en

theme:
  language: en
```

Details:

* The first line will be the same across the board.
* The `site_name` will be the name of your project.
* The `site_url` will be the base URL to your project.
* The `docs_dir` will be the same language code as the filename.
* The `theme: language:` will also be the same language code as the filename. Note: the Material theme sometimes expects a [different language code](https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/) based on locale.

Therefore, the associated `mkdocs.fr.yml` file would contain:

```yaml
INHERIT: config.yml
site_name: Mon Incroyable Docs
site_url: https://example.com/fr
docs_dir: fr

theme:
  language: fr
```

Additional content in the `config.yml` file is only necessary if you intend to add further configuration to your MkDocs setup. Any options added to it will apply to both. This tool expects `config.yml` to exist, so even if you don't intend to add any other options at this time, you need to generate an empty file.

Note: Given the brevity of what is provided here, you may wonder what the point is of a separate `config.yml` file. There are a massive number of options for configuring MkDocs, including themes, plugins, extensions, and more. The following is a bare-bones configuration; it's enough to get you through the translation workflow. You will need to have the option available to add further modifications, and to avoid duplicating content, you will need to use a separate file.

The `config.yml` for my setup would minimally require the following, as the Material theme language is specified in the `mkdocs.language.yml` files:

```yaml
theme:
  name: material
```

### PO file, POT file, and locales directory structure

The `locales/` directory is expected to be in the `/docs/` directory.

The POT files should reside in the `/docs/locales/templates/` directory.

The PO files for each language should reside in a `/docs/locales/language-code/LC_MESSAGES/` directory. The demo translation language for this documentation is French. The French PO files are in `/docs/locales/fr/LC_MESSAGES/`.

**Important: Create new language code directories in `locales` before attempting to create PO files!** To avoid unnecessary incorrect directories being created if an invalid language code is provided in error, the method MkDocs PO I18n uses to verify if the provided language code is an existing language checks for the existence of the language code directory in the `/docs/locales/` directory. If the language code directory doesn't exist, the tool will fail to run with an error. Therefore, you must create the desired language code directories manually before running the translation tools.

## Recommended prerequisites

It is highly recommended to use `tox` for managing usage of this tool. It is not required, however, it creates a consistent environment locally and on Read the Docs, which makes troubleshooting issues much more straightforward.

### `tox` configuration

The following is an example `tox.ini`, similar to the one found in this repo. It accounts for English as a primary language, and French as the only available translation. You will need to make changes to it for a different setup.

```{.ini hl_lines="8 11-12 14 16-20" linenums="1"}
[tox]
envlist = docs-all

[docs]
docs_dir = {tox_root}{/}docs
templates_dir = {tox_root}{/}docs{/}locales{/}templates

[testenv:docs{,-translate,-all,-live,-en,-fr}]
base_python = py313
skip_install = true
dependency_groups =
    dev
commands:
    !all-!translate-!live-!en-!fr : build_md_translations {posargs} en
    translate : build_pot_translations
    translate : build_po_translations fr
    live : live_serve {posargs}
    all : build_md_translations {posargs} en fr
    en : build_md_translations {posargs} en
    fr : build_md_translations {posargs} fr
```

Yours should look the same through the line 7. That's where the dynamic configuration options begin. 

* Line 8 will differ based on the translation languages you have; each language code must be added to the `testenv` line, in the same manner as `-en` and `-fr`.
* Lines 11-12 will need be the following if you are using `requirements.txt`:
    
    ```ini
    deps = 
        -r {tox_root}{/}requirements.txt
    ```
    
* Line 14 will need to include all translation language codes in section before the `:`, in the same manner as `!en` and `!fr`. This line provides the command that will be run if you run `tox -e docs` with no specifiers. This line builds the English translations.
* Line 16 will need to have all translated language codes included in the same manner as `fr`.
* Line 17 requires a language code if your primary language is not English.
* Line 18 will need to include all translation language codes, in the same manner as `en` and `fr`. This line provides the command that will be run if you run `tox -e docs-all`, which will build all the documentation in all languages.
* Lines 19 and 20 are basically the same as `all`, however each one builds only one specific language. Line 19 will build the English documentation if you run `tox -e docs-en`. This is how Read the Docs builds the various translations. If you wish to add another language, you would need to add another line like these two, beginning and ending with the new language code.

## Optional Prerequisites

The following is required if you intend to use Read the Docs to host your documentation site.

### Read the Docs configuration

Read the Docs requires [a `.readthedocs.yaml` configuration file](https://docs.readthedocs.com/platform/stable/config-file/v2.html) be present in your repo. If you are using `tox` and `pyproject.toml` with dependency groups, your `.readthedocs.yaml` file should contain the following:

```{.yaml linenums="1"}
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
  jobs:
    pre_install:
      - python -m pip install --upgrade pip
      - python -m pip install --group 'dev'
    build:
      html:
        - python -m tox -e docs-$READTHEDOCS_LANGUAGE -- --output=$READTHEDOCS_OUTPUT/html/
```

If you are using `requirements.txt`, you will need to update line 10 to `- python -m pip install -r requirements.txt`.

If you are not using `tox`, you will need to update line 13 to `- python -m build_md_translations $READTHEDOCS_LANGUAGE -- --output=$READTHEDOCS_OUTPUT/html/`.

Here's what's happening in the rest of the file:

* The `os` and `tools` options set up your dev environment.
* The `pre_install` option runs the commands below it before the build, and `pip install`s the necessary requirements for the build.
* The `build` option runs the command below it to build the documentation.
    * The build command uses two Read the Docs environment variables: `$READTHEDOCS_LANGUAGE` and `$READTHEDOCS_OUTPUT`.
    * `$READTHEDOCS_LANGUAGE` is used to complete build command to build each language separately, which is necessary for Read the Docs.
    * `$READTHEDOCS_OUTPUT` is used to ensure that the build output ends up in the right directory. Read the Docs is expecting your primary `index.html` to be in `html/language`, so you specify the proper output path into an `html` directory here, and the configuration adds the language directory for you.

### Read the Docs primary and translation project creation and set up

[Create the primary Read the Docs project](https://docs.readthedocs.com/platform/stable/intro/add-project.html) for your repo. If you have already added the `.readthedocs.yml`, connecting a RTD project can be done automatically. This will act as the "parent project".

To add a translation project, navigate back to the Projects dashboard and click "+ Add project". Search for the repo you added as the primary project, and choose it. RTD will tell you that it's already been configured, but click "Continue" and it will still take you to the configuration page. Update the "Name"; adding `-language-code` is the simplest way to handle it, i.e. for French, update `project-name` to `project-name-fr`. Below that, there is a dropdown for "Language"; choose the associated language from this menu. Clicking "Next" will create the project.

To associate the translation project with the parent project, click on the parent project in the dashboard, and navigate to Settings > Translations. Click "+ Add translation", choose the translation project from the dropdown, and click "Save".

## Generating POT files from Markdown

PO Template (POT) files act as the templates for updating the translated PO files, as the Markdown content is updated, so you don't lose existing translations as you make changes to your content. The POT files must be generated once in the beginning, and then regenerated when there are updates to the Markdown content. As well, Weblate requires POT files, as it is possible to create a new translation through the Weblate interface, and the PO files for that new translation are generated from the template files. 

So, the first step is to generate the POT files from the Markdown content. The tool for this is called [`md2po`](https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/md2po.html). This tool runs recursively on a provided input directory, and if the `--pot` flag is included, creates in the provided output directory, a set of POT files in the same directory layout in the input directory.

The command has been incorporated into the `build_pot_translations` script. The command that is run, is provided the `--input` directory, which contains your English Markdown, the `--output` directory, which is `docs/locales/templates`, the `--pot` flag, and sets `--duplicates=merge`. The last flag ensures that if a given string is present in more than one place, it is only shown once with multiple locations, instead of being shown three different times with three separate locations.

After the initial run, this command must be run every time you update existing content or add new content. It is from the PO template files that the PO files are generated, and therefore if this step is not completed, your updated content won't be present in the translations. This can lead to build errors involving missing content; this should be the first thing you check if the translations fail in that way.

You will want to push the initial POT files to GitHub. After that, you have two options. If you are manually updating translations locally, and pushing the results to GitHub, you need to include the POT files. If you are using CI to handle translation updates, you should add `.pot` files to `.gitignore`, and not push them after the initial generation.

## Usage with `tox`

The following commands assume you have set up your [`tox.ini` configuration](#tox-configuration) as shown above.

To do a local build of the site in English, run the following:

```console
$ tox -e docs
```

You can also run:

```console
$ tox -e docs-en
```

To live serve the build of your site in English, run the following:

```console
$ tox -e docs-live
```

If your primary language is not English, you need to add a language code. For example, to live serve the site with German as your primary langauge, run the following:

```console
$ tox -e docs-live de
```

The first step towards translating content is to generate the PO template files, followed by generating the desired language PO files. To invoke this process, run the following:

```console
$ tox -e docs-translate
```

To build the site in a language other than your primary language, you'll run the language-specific command, by including the language code. For example, to build in French, run the following:

```console
$ tox -e docs-fr
```

To build in all available languages, including your primary language, run the following:

```console
$ tox -e docs-all
```

## Usage

The following covers how to use MkDocs PO I18n directly.

To do a local build of the site in English, run the following:

```console
$ build_md_translations en
```

To live serve the build of your site in English, run the following:

```console
$ live_serve
```

If your primary language is not English, you need to add a language code. For example, to live serve the site with German as your primary langauge, run the following:

```console
$ live_serve de
```

The first step towards translating content is to generate the PO template files. To generate the POT files, run the following:

```console
$ build_pot_translations
```

The next step is generating the desired language PO files. You can run this command with one or more language codes. For example, to generate the PO files for French, run the following:

```console
$ build_po_translations fr
```

To build the site locally with translated content, you can run this command with one or more language codes. For example, to build in French, run the following:

```console
$ build_md_translations fr
```

## Push content and configuration files to GitHub

Once you have everything working locally, you'll want to push your changes. You'll need to update your `main` branch, unless you specified a different branch when you set up the RTD projects. Once pushed, RTD should automatically build the documentation.

## Verify all languages are building successfully

You can verify whether all languages have built successfully by either checking the RTD project dashboard, or by viewing the documentation and using the RTD flyout menu to view all available languages.

## Final notes and thoughts

Internationalisation and localisation are key accessibility features for any documentation. I find Markdown to be far more approachable than reStructuredText. Coming up with a translation solution for MkDocs that fulfilled our needs, and worked with the tools we were already using, was critical to moving forward with replacing our reStructuredText documentation with Markdown. I'm incredibly pleased with what I've put together here. The version BeeWare intend to use is heavily modified to handle BeeWare-specific workflow elements. I decided to publish a more generalised version to share. That said, there is a lot of room for adding features to work with your specific workflow.

It is quite straightforward to add Markdown linting to the process, especially if you're using a `tox` configuration. As well, this process can be added to CI, ensuring automatic updates of translations.

I don't have a good answer as to how much maintenance will be happening with this project. If you have feedback or suggestions, feel free to [file an issue](https://github.com/kattni/mkdocs-po-i18n/issues), and I'll see what I can do.

I hope this tool helps you with translating your MkDocs documentation, using PO files, on Read the Docs.
