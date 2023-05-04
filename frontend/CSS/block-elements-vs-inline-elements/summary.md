# Block Elements vs. Inline Elements

In CSS, every element is either a block-level element or an inline-level element, and this affects how the element is displayed and how it interacts with other elements on the page.

## **Block-level elements**
These are elements that take up the full width of their container by default and start on a new line. They create a rectangular block on the page, and you can set their width, height, margin, padding, and border properties. Some common block-level elements include:

- `<div>`: a generic container element
- `<p>`: a paragraph of text
- `<ul>` and `<ol>`: unordered and ordered lists
- `<h1>` to `<h6>`: headings of different levels
- `<form>`: a form for user input

Example:

```
<div>
  <h1>Welcome to my website!</h1>
  <p>This is a paragraph of text.</p>
  <ul>
    <li>List item 1</li>
    <li>List item 2</li>
    <li>List item 3</li>
  </ul>
</div>
```

**Inline-level elements** are elements that flow within the text of a document and do not start on a new line. They do not create a rectangular block on the page and you cannot set their width, height, margin, padding, or border properties. Some common inline-level elements include:

- `<span>`: a generic inline-level container element
- `<a>`: a hyperlink
- `<strong>` and `<em>`: emphasized text
- `<img>`: an image
- `<input>`: a form input field

Example:

```
<p>This is a paragraph of text with an <a href="#">inline link</a>.</p>
```

It's important to note that you can change an element's display type using CSS. For example, you can set a `<div>` element to display as an inline element, or an `<a>` element to display as a block element. This gives you more control over how your page is laid out and how your elements interact with each other.
