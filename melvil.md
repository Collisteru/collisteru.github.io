# On Melvil, The Bookish CLI Database

[Melvil](https://github.com/Collisteru/Melvil) is a minimal CLI database for managing content. It started out as a booklist
app, but now it can handle any type of media.

## The Problem:

Before Melvil, there were no open-source personal library tools. For a picture of what the status quo looked like, here are the major
options for book management software today:

|                | Features                                                             | Platform    | Owner          |
|----------------|----------------------------------------------------------------------------|-------------|----------------|
| GoodReads      | Public and Private Booklists, Universal Catalog, Recommendations, Reviews  | Web         | Amazon         |
| LibraryThing   | Public and Private Booklists, Universal Catalog, Recommendations, Reviews  | Web         | LibraryThing   |
| Bookly         | Reading Habit Tracking                                                     | Web         | Bookly         |
| Libib          | Catalogue Management                                                       | Web, Mobile | Libib          |
| The Storygraph | Recommendations                                                            | Web, Mobile | The Storygraph |

These apps all have their merits, but none of them is open source. They all require either a mobile phone or internet connectivity.
I like tools that users can understand and operate independently, and Melvil fills that gap for content management. As a CLI app, you can run it on anything with a command line.
Because Melvil stores your data in a minimal JSON format, there are no mysteries surrounding data storage. 

The tradeoff you make for Melvil is a lack of features. Melvil may never totally replace GoodReads, but for a camping trip or a long flight, it's a great tool to have.

---
## Features:

Melvil has all the features you'd expect in a database. You can:

* Add and remove books.
* Change attributes like authors, priority, and tags.
* Search the database by priority and by tag.
* List the highest-priority book in the database that has a specific, given tag.

There are also many UX enhancements. With Melvil's fuzzy search, for example, you can type only part of your target title and the software will know your desires.

[Insert GIF of smart search here]

As you can see, typos are also not a problem.

## Lessons Learned:

This was the largest open-source project I've worked on; its scope brought many interesting elements and challenges
I hadn't encountered before. For example, the decision to add continuous user-software interaction made for a better user experience but also made testing a headache. Finding no way to spin off a subprocess and continuously
pass data in and out, friends and I tested by hand.

<small>Come to think of it, an Inquirer testing framework would make a great future project...</small>

Melvil relies on great open-source projects, such as [Typer](https://typer.tiangolo.com/) to handle the command line interface and [Inquirer](https://github.com/magmax/python-inquirer) for the nice user questions.
[Python-Levenshtein](https://pypi.org/project/python-Levenshtein/) powers smart search.

## Future Improvements:

Melvil is a work in progress. I plan to add at least the following features:

* Enhanced list view that doesn't tear when the terminal is resized.
* Custom Fields
* Add hash and parity features to the path and the text file to defend against hackery.

If you'd like to track Melvil's progress, [here's the GitHub link again.](https://github.com/Collisteru/Melvil)

**All the best,**

Collisteru