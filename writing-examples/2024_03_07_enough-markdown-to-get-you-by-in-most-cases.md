Title: Enough Markdown to Get You By in Most Cases
Date: 2024-3-7 14:15
Author: Kattni
Tags: Tutorials, Documentation, Getting Started, Programming, Web Development
Slug: enough-markdown-to-get-you-by-in-most-cases
Summary: An introduction to some basic Markdown features
HideTOC: Yes
Status: published

Markdown is a "lightweight markup language", which is a fancy way of saying, it's a relatively straightforward way to apply formatting to plaintext. Markdown is already relatively widely used, and is becoming more so. I learned it initially because Discord renders Markdown in messages, and GitHub renders Markdown in posts. I've found it in many more places since, and have appreciated being able to use it elsewhere. Another excellent feature is the ease with which Markdown can be rendered into HTML. All content on this blog is written entirely in Markdown, which Pelican then renders to the HTML that you are viewing now.

There are plenty of thorough guides on using Markdown that cover everything Markdown can do. My intent here is to give you a tour of some basics to provide you with enough knowledge to get started using Markdown. I've been using Markdown for about six years now, and there's an essential set of elements that cover pretty much everything I need. Markdown is capable of far more than I will cover here, but this post will provide you with a solid place to start.

## The kBits
Here are the Markdown features covered in this tutorial.

* Headings - Text preceded by between one and six `#` symbols, corresponding to the header level desired.
* Paragraphs - Text blocks between blank lines to create paragraphs.
* Text formatting - Text nested between `*` for italics, `**` for bold, or `~~` for strikethrough, or a combination thereof to combine multiple formats.
* Links - A standalone link is the URL enclosed by `<>`, as in `<URL>`. Text linked follows the format of `[text](URL)`.
* Images - With alt text, use the format: `![Alt text here](image_path_or_URL)`.
* Lists - Create ordered lists by using sequential numbers at the beginning of each line in the list, and unordered lists by using `*` at the beginning of each line in the list. You can also indent items under list items in both formats, and any combination thereof.
* Code - Format text as inline code within a sentence by enclosing the code in single backticks (`` ` ``). Format a codeblock by including three backticks (`` ``` ``) on the line before and after the block.

## Headings
You can create headings of up to six different levels. The heading level corresponds to the number of `#` that precede the heading text, e.g. a level one heading begins with a single `#`, and a level six heading begins with six `######`. 

For example, to create a level one heading, you would type the following:
```markdown
# Heading One Text
```

Which ends up rendered as:

---

# Heading One Text

---
<br>

To create a level three heading, you would type the following:
```markdown
### Heading Three Text
```

Which ends up rendered as:

---

### Heading Three Text

---
<br>

It's best practice to always include a blank line before and after a heading that occurs within the page. If the first line of your document is a heading, you only need a blank line after it. Some Markdown compatible software will render headings and text properly without a blank line, however, it's best to include it as there are some that don't.

<br>

## Paragraphs
Text in Markdown is pretty straightforward. To begin a paragraph, simply type some text with no tabs or spaces before it. Always keep text left-aligned, or you will encounter unexpected formatting. To move on to a new paragraph, include a blank line between it and the section of text above it.

For example, to include a single sentence paragraph in your document, you could include the following:
```markdown
This is my first sentence, in my first paragraph.
```

Which ends up rendered as:

---

This is my first sentence, in my first paragraph.

---
<br>

To add a second paragraph, you would include:
```markdown
This is my first sentence, in my first paragraph.

Here is my second sentence. This is my second paragraph.
```

Which ends up rendered as:

---

This is my first sentence, in my first paragraph.

Here is my second sentence. This is my second paragraph.

---
<br>

## Text Formatting
There are three modifications you can make to text formatting: italic, bold, and strikethrough. You can also use any combination of the three. You can modify single words or strings of words by adding the appropriate symbols before and after single words or entire strings of text.

For example, to apply each format individually, you would include:
```markdown
This is *italic*, **bold**, and ~~strikethrough~~ text formatting in action.
```

Which ends up rendered as:

---

This is *italic*, **bold**, and <s>strikethrough</s> text formatting in action.

---
<br>

Combining them is as simple as combining the symbols decorating the text. Note that you need to nest the symbols at the same location on both sides, from the outside heading inward, e.g. if you begin with `**~~`, then you should end with `~~**`. 

For example, to make bold, italic text, you would include:
```markdown
This is ***bold italic*** text.
```

Or to include bold, strikethrough text, you would include:
```markdown
This is **~~bold strikethrough~~** text.
```

Which ends up rendered as:

---

This is ***bold italic*** text. This is **<s>bold strikethrough</s>** text.

---
<br>

You can also apply the formatting in the middle of a word. This works for all three, or any combination thereof.

For example, to bold part of a word, you would include:
```markdown
This is an im**port**ant syllable.
```

Which ends up rendered as:

---

This is an im**port**ant syllable.

___
<br>

## Links
You can add standalone links to your document. To do so, you include the URL enclosed in `<>`.

For example, to link to Wikipedia, you would include:
```markdown
<https://www.wikipedia.org>
```

Which ends up rendered as:

---

<https://www.wikipedia.org>

---
<br>

You can also create email links using the same method.

For example, to create a `mailto:` email link, you would include:
```markdown
<email@example.com>
```

Which ends up rendered as:

---

<email@example.com>

---
<br>

You can also add hyperlinked text to your document. To do so, you include the desired text enclosed in brackets, `[]`, and the target link enclosed in parentheses, `()`. On the off chance that it will help you, a mnemonic for remembering the order is that they are in alphabetical order: *B*rackets followed by *P*arens. 

For example, to link to Wikipedia as text, you would include:
```markdown
[Wikipedia](https://www.wikipedia.org)
```

Which ends up rendered as:

---

[Wikipedia](https://www.wikipedia.org)

---
<br>

You can include hyperlinked text in the middle of a sentence, as shown here:
```markdown
You can find all sorts of related information by searching [Wikipedia](https://www.wikipedia.org), and then following the "See Also" links included on a a given page.
```

Which ends up rendered as:

---

You can find all sorts of related information by searching [Wikipedia](https://www.wikipedia.org), and then following the "See Also" links included on a a given page.

---
<br>

You can also format links by wrapping the link formatting with the text formatting symbols.

For example, to bold and italicise a link in a sentence, you would include:
```markdown
You can find all sorts of related information by searching ***[Wikipedia](https://www.wikipedia.org)***, and then following the "See Also" links included on a a given page.
```

Which ends up rendered as:

---

You can find all sorts of related information by searching ***[Wikipedia](https://www.wikipedia.org)***, and then following the "See Also" links included on a a given page.

---
<br>

## Images
You can include images in your document using Markdown. You need to prepare alt text, and to know the path if the image is local to your computer, or the URL if you're using an image from the web.

For example, to add an image from Wikimedia with the alt text "Biene auf lavendel", you would include:
```markdown
![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)
```

Which ends up rendered as:

---

![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)

---
<br>

You can make an image into a link by combining the link formatting with the image formatting.

For example, to link the above image to its location on the web, you would include:
```markdown
[![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)
```

Which ends up rendered as:

---

[![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)

---
<br>

## Lists
You can create both ordered and unordered lists, with indented items under any list item.

To create an ordered list, you would include:
```markdown
1. Item one
2. Item two
3. Item three
```

Which ends up rendered as:

---

1. Item one
2. Item two
3. Item three

---
<br>

To create an unordered list, you would include:
```markdown
* Item thirty
* Item eleven
* Item forty-two
```

Which ends up rendered as:

---

* Item thirty
* Item eleven
* Item forty-two

---
<br>

You can add an indented item to any member of a list by including a list item below the desired list member indented four spaces or a tab. Different editors will render indented list items at different indentation levels, but four spaces or a tab should render the same regardless.

Lists require a blank line before and after them to render properly. Always include a blank line between text and lists.

For example, to add an ordered indented list to an ordered list item, you would include:
```markdown
1. Item one
2. Item two
   1. Item two point one
   2. Item two point two
3. Item three
```

Which ends up rendered as:

---

1. Item one
2. Item two
    1. Item two point one
    2. Item two point two
3. Item three

---
<br>

To add an unordered indented list to an unordered list item, you would include:
```markdown
* Item thirty
* Item eleven
   * Item eleven point twelve
   * Item eleven point five
* Item forty-two
```

Which ends up rendered as:

---

* Item thirty
* Item eleven
    * Item eleven point twelve
    * Item eleven point five
* Item forty-two

---
<br>

You can also combine the list formats with indented items of the other format.

For example, to add an _unordered_ indented list to an _ordered_ list item, you would include:
```markdown
1. Item one
2. Item two
    * Item two point whatever
    * Item two point something else
3. Item three
```

Which ends up rendered as:

---

1. Item one
2. Item two
    * Item two point whatever
    * Item two point something else
3. Item three

---
<br>

To add an _ordered_ indented list to an _unordered_ list item, you would include:
```markdown
* Item thirty
* Item eleven
    1. Item eleven point one
    2. Item eleven point two
* Item forty-two
```

Which ends up rendered as:

---

* Item thirty
* Item eleven
    1. Item eleven point one
    2. Item eleven point two
* Item forty-two

---
<br>

You can also include other elements in lists. 

For example, to include a separate paragraph under the first list item, you would include:
```markdown
1. Item one

    This is a paragraph.

2. Item two
```

Which ends up rendered as:

---

1. Item one
   <p>This is a paragraph.</p>
2. Item two

---
<br>

To add an image to a list, you would include:
```markdown
1. Item one

    ![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)

2. Item two
```

Which ends up rendered as:

---

1. Item one

    ![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)

2. Item two

---
<br>

This works with various other elements as well, not covered in this tutorial. Simply indent the element four more spaces or a tab, surrounded on top and bottom by blank lines, between list items.

<br>

## Code
There are two ways to format code: inline and blocks. Inline code is code-formatted text in the middle of a sentence, paragraph, or other text. Codeblocks are separately highlighted, standalone sections of code.

To format inline code, you surround the text with one backtick (`` ` ``) on either side.

For example, to include inline code in a sentence, you would include:
```markdown
To access the features of Git from the command line, you run various `git` commands.
```

Which ends up rendered as:

---

To access the features of Git from the command line, you run various `git` commands.

---
<br>

To format a codeblock, you simply indent the begin the code content with four spaces, or a tab. You can indent further below that for code indentation.

For example, to create a codeblock, ensuring the whitespace is as shown, you would include the following:

```markdown
    while True:
        pass
```

Which ends up rendered as:

---

    while True:
        pass

---
<br>

Alternatively, you can create a "fenced" codeblock by placing three backticks (`` ``` ``) on the line before and the line after the code.

For example, to add a fenced codeblock, you would include:
~~~
```
while True:
    pass
```
~~~

Which ends up rendered as:

---

```
while True:
    pass
```
<br>

The neat thing about fenced codeblocks is that they allow for syntax highlighting, as long as it's supported by the Markdown processor or editor that you're using.

For example, to highlight a fenced codeblock as Python, you would include the following:

~~~
```python
while True:
    pass
```
~~~

Which ends up rendered as:

---

```python
while True:
    pass
```

---
<br>

## Markdown in Action
The following is a short Markdown document, containing many of the concepts discussed above. This is the Markdown before rendering.
```markdown
# Heading 1

Introductory sentence.

## Heading 2

Further text. A second sentence.

A second paragraph of text. A sentence containing a link to [Wikipedia](https://www.wikipedia.org). A sentence containing inline `code`.

A code block:

    while true:
        pass

### Heading 3

A sentence with formatting including **bold**, *italics*, ***bold and italic***, and ~~strikethrough~~.

#### Heading 4

This section contains an image.

![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)

##### Heading 5

This section contains an ordered list:
1. Item one
2. Item two
3. Item three
   1. Item three, point one

###### Heading 6

This final section contains a bullet list:
* Item forty-two
* Item ninety-one
  * Item ninety-one point something
```
<br>

Here is the document rendered.

---

# Heading 1

Introductory sentence.

## Heading 2

Further text. A second sentence.

A second paragraph of text. A sentence containing a link to [Wikipedia](https://www.wikipedia.org). A sentence containing inline `code`.

A code block:

    while true:
        pass

### Heading 3

A sentence with formatting including **bold**, *italics*, ***bold and italic***, and ~~strikethrough~~.

#### Heading 4

This section contains an image.

![Biene auf lavendel](https://upload.wikimedia.org/wikipedia/commons/5/5e/200x133px-Biene_auf_lavendel.png)

##### Heading 5

This section contains an ordered list:

1. Item one
2. Item two
3. Item three
   1. Item three, point one

###### Heading 6

This final section contains a bullet list:

* Item forty-two
* Item ninety-one
  * Item ninety-one point something

---
<br>

## Wrap Up 
The features I detailed here make up easily 90% of the Markdown I use day-to-day. However, Markdown is capable of many more things than were covered in this tutorial. That said, these features are plenty to get you started and working towards getting comfortable with Markdown. There are plenty of guides available across the web that delve into more detail, so when you're ready, check those out for more information.

## Attribution
*"Biene auf lavendel" image captured by [Mattes](https://commons.wikimedia.org/wiki/User:Mattes), used here under [CC BY-SA 3.0 license](https://creativecommons.org/licenses/by-sa/3.0)*