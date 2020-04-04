# array and linked list

start with a discussion of a very general structure, a collection.

## collection
**properties of collection**

- Don't have a particular order (so you can't say "give me the 3rd element in this collection")
- Don't have to have objects of the same type

## lists
**Properties of lists**

- Have an order (so you can say things like "give me the 3rd item in the list")
- Have no fixed length (you can add or remove elements)

## Arrays vs. lists vs. Python lists
The distinction between arrays and lists can be a little confusing, especially because of how Python implements the data structure it calls a "list". Below, we'll go over some key points that should make this clearer.

## Arrays
An array has some things in common with a list. In both cases:

- There is a collection of items
- The items have an order to them


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)